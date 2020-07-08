from flask import Flask
from threading import Thread
import logging
import sys

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask('')
app.logging = False
logging.disabled = True
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
    return "Bot Online"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()