#https://flask.palletsprojects.com/en/2.3.x/
print("Hello world!")
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
  return "<p> Hello Kai <p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
  