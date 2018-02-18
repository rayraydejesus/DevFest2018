from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Setup Homepage Route
@app.route('/')

def index():
    return render_template('index.html')

app.config['MONGODB_SETTINGS'] = { 'db' : 'data' }
db = MongoEngine(app)


class location(db.Document):
  
  address = db.StringField(required=True)
  coord = db.StringField(required=True)
  lat = db.StringField(required=True)
  long = db.StringField(required=True)
  name = db.StringField(required=True)
  industry = db.StringField(required=True)
  #poster = db.ReferenceField(User)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)