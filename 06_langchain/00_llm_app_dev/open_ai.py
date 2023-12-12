import os
import openai
from typing import Dict

from dotenv import load_dotenv, find_dotenv
_ : bool = load_dotenv(find_dotenv()) # read local .env file
openai.api_key: str = os.environ['OPENAI_API_KEY']

llm_model: str = "gpt-3.5-turbo-0613"

def get_completion(prompt: str, model: str=llm_model)->str:
    messages: [Dict[str: str]] = [{"role": "user", "content": prompt}]

    # https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models#2-an-example-chat-api-call
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    
    return response.choices[0].message["content"]


print(get_completion("What is 1+1?"))