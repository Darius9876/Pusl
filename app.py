from dictionary import data # IMPORTUOJAME
app = Flask(__name__)


@app.route('/')

def index():
    return render_template('PSL.html', data=data) # PERDUODAME Į ŠABLONĄ

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)