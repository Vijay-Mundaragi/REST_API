from my_app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')


# to run the application in in stand alone mode
if __name__ == '__main__':
    app.run(debug=True)