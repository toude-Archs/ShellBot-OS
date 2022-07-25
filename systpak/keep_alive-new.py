from flask import Flask
from threading import Thread

app = Flask('')
host = '0.0.0.0'
port = 26343
@app.route('/')
def home():
  return "status:server shellOS bot online"

def run():
  app.run(host=host,port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
