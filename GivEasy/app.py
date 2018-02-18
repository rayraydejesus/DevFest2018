from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Setup Homepage Route
@app.route('/')

def index():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)