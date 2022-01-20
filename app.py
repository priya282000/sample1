from datetime import datetime

from flask import Flask, render_template, url_for
import smtplib
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired

from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Padma2000!@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    assignee = db.Column(db.String(50), nullable=False)
    assignee_email = db.Column(db.String(50), nullable=False)
    reporter = db.Column(db.String(50), nullable=False)
    due = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(30), default='Pending')

class SampleForm(FlaskForm):
    task = StringField("Enter task", validators=[DataRequired('task required')])
    assignee = StringField("Enter assignee", validators=[DataRequired('assignee required')])
    email = StringField("Enter assignee email", validators=[DataRequired('email required')])
    reporter = StringField("Enter reporter", validators=[DataRequired('reporter required')])
    due = StringField("Enter due", validators=[DataRequired('due required')])
    # submit = SubmitField("Submit")

@app.route("/", methods=['GET','POST'])
def index():
    form = SampleForm()
    if form.validate():

    return render_template("home.html", form=form)

# @app.route("/task",methods=["GET","POST"])
# def test():
#     form = SampleForm()
#     # task=None
#     # assignee=None
#     # email=None
#     # reporter=None
#     # due=None
#     # if form.validate_on_submit():
#     #     task = form.task.data
#     #     assignee = form.assignee.data
#     #     email = form.email.data
#     #     reporter = form.reporter.data
#     #     due = form.due.data
#     return render_template("home.html", form=form)


# @app.route('/')
# def index():
#     email = "vindhya2377@gmail.com"
#     message = "Hi"
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("padmamurugesh2000@gmail.com", "padma2000!")
#     server.sendmail("padmamurugesh2000@gmail.com",email,message)
#     return render_template("home.html")
#
#
# if __name__ =="__main":
#     app.run(debug=True)





