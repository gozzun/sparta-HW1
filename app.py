# app.py
# 추가과제 구현을 위해 노력해보았으나, DB 접근에 실패하였음.

from flask import Flask, render_template, request
import random
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # user_choice_receive = request.args.get("choice")
    # computer_choice_receive = request.args.get("cpuChoice")
    # result_receive = request.args.get("result")

    # gamehistory = GameHistory(user_choice=user_choice_receive,computer_choice=computer_choice_receive,result=result_receive)
    # db.session.add(gamehistory)
    # db.session.commit
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
