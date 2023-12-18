import shelve

# Replace shelve and Connect your data to a
# external data source
# https://discuss.streamlit.io/t/best-practices-for-storing-user-data-in-a-streamlit-app-and-deploying-it-for-a-variable-number-of-users/39197
class Database:
    def __init__(self, dbName: str = "chat_history") -> None:
        self.dbName = dbName

    # Load chat history from shelve file
    def load_chat_history(self)->[dict]:
        with shelve.open(self.dbName) as db:
            return db.get("messages", [])


    # Save chat history to shelve file
    def save_chat_history(self, messages: [dict]):
        print("Database: Save", messages)
        with shelve.open(self.dbName) as db:
            db["messages"] = messages

