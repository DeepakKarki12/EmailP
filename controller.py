# !pip install langchain-huggingface
# !pip install huggingface_hub
# !pip install transformers
# !pip install accelerate
# !pip install  bitsandbytes
# !pip install langchain

import os
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv



load_dotenv()
sec_key = os.getenv('sec_key')
repo_id=os.getenv('repo_id')

sec_key = sec_key
repo_id=repo_id
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)

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
print("response",response)
