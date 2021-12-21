from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from sqlalchemy.sql.schema import PrimaryKeyConstraint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'

db = SQLAlchemy(app)


class Gaming(db.Model):
    __tablename__ = 'Gaming_Data'
    name = db.Column(db.String,primary_key=True)
    required_age = db.Column(db.Integer)
    is_free = db.Column(db.Integer)
    review_score = db.Column(db.Integer)


@app.route('/')
def steam_games():
    try:
        games = Gaming.query.all()
        return render_template('table_template.html', games=games)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
   app.run(debug=True)