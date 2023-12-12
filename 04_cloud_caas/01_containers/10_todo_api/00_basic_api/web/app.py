# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello from Zia'