


import os
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from flask import Flask, render_template, request


load_dotenv()
sec_key = os.getenv('sec_key')
repo_id=os.getenv('repo_id')

sec_key = sec_key
repo_id=repo_id
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)


app = Flask(__name__,template_folder='.')
@app.route('/')
def index():
    print(os.getcwd())
    return render_template('index.html')

@app.route('https://emailp.onrender.com//fun', methods=['POST'])
def processEmailData():
  data = request.get_json()
  print("processing. . .",data)
  print("processing data . . .")
  prompt = f"""
  You are an email response predictor. Your task is to predict one response that will highly match the response from the receiver's side.

  User Input:

  Subject: {data['subject']}

  {data['mail']}

  Example output format:
  {{
    Subject: Re: Offer Letter Acknowledgement

    Dear [Hiring Manager's Name],

    Thank you for extending the offer for the [Job Title] position at [Company Name]. I am thrilled to accept this opportunity and am excited to join your team.

    Please let me know if there are any further steps or paperwork required before my start date.

    Thank you once again.

    Best regards,
    Mohan Singh }}


  Note :- Generate the output according to example output format only:
  """

  response = llm.invoke(prompt)
  print("llm output",response)
  try:
    if "{" in response:
        first = response.index("{")+1
    else:
        first = response.index("S")
  except:
    print("distroted output in starting index")
    first = 0

  try :
    last = response.index("}")
  except:
    print("distroted output in last")
    last = len(response)

  response = response[first:last]
  print("acutal output",response)
  return {"response":response}

app.run(host='0.0.0.0', port=4000)