from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ : bool = load_dotenv() # read local .env file


import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="My API Key",
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
async for part in client:
    print(part.choices[0].delta.content or "")



