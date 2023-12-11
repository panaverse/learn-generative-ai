# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello from Zia'
 
# main driver function 
# https://realpython.com/if-name-main-python/
if __name__ == "__main__":
    app.run()