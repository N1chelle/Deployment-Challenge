from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from sqlalchemy.sql.schema import Index, PrimaryKeyConstraint




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'

db = SQLAlchemy(app)


class Gaming(db.Model):
    __tablename__ = 'Gaming_Data'
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    required_age = db.Column(db.Integer)
    is_free = db.Column(db.Integer)
    currency = db.Column(db.String)
    final = db.Column(db.Float)
    total_reviews = db.Column(db.Integer)
    review_score = db.Column(db.Integer)
    



@app.route('/')
def home():

    return render_template('home.html')

@app.route('/data')
def data():
    try:
        games = Gaming.query.all()
        return render_template('table_template.html', games=games)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/visuals')
def visuals():
    # engine = sqlalchemy.create_engine('sqlite:///game.db')
    # with engine.connect() as connection:
    #   df = pd.read_sql("game", connection)
    #   plt.figure(figsize=(12,8))
    #   g = df['is_free'].value_counts().plot(kind='pie', legend=True, autopct='%1.1f%%',explode=(0, 0.2), shadow=True, startangle=0)
    #   #img = io.BytesIO()
    #   g.savefig('plot.png')
    return render_template('visuals.html')



if __name__ == '__main__':
   app.run(debug=True)