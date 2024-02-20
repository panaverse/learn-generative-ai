from dotenv import load_dotenv, find_dotenv
from database import Database
from openai import OpenAI
from typing import Any

class BotModel:
    def __init__(self, name:str, model:str = "gpt-3.5-turbo-1106") -> None:
        self.name: str = name
        self.model: str = model
        load_dotenv(find_dotenv()) 
        self.client : OpenAI = OpenAI()
        self.db = Database()
        self.messages = self.load_chat_history()

    def load_chat_history(self)->[]:
        return self.db.load_chat_history()

    def save_chat_history(self):
        print("Model: Save", self.messages)
        self.db.save_chat_history(messages=self.messages)

    def delete_chat_history(self):
        print("Model: Delete")
        self.messages = []
        self.save_chat_history()

    def get_messages(self)->[dict]:
        return self.messages
    
    def append_message(self, message: dict):
        self.messages.append(message)

    def send_message(self, message: dict)->Any:
        self.append_message(message=message)
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True,
        )
        return stream

    
