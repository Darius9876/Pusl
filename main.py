from flask import Flask, render_template
# app = Flask(__name__)
# @app.route("/")
# def home():
#  return "Čia Dariaus  puslapis <h1></h1>"
# if __name__ == "__main__":
#  app.run(debug=True)

from dictionary import data
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', data=data)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)