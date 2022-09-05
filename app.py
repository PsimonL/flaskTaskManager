from turtle import title
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # https://flask-sqlalchemy.palletsprojects.com/en/2.x
# /config/
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():  # put application's code here
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    # return render_template("base.html", todo_list=todo_list)
    return render_template("base.html")


if __name__ == '__main__':
    db.create_all()
    new_todo = Todo(title="todo 1", complete=False)
    db.session.add(new_todo)
    db.session.commit()
    app.run(debug=True, port=80)

    #https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=1207s
    #https://www.youtube.com/watch?v=yKHJsLUENl0&t=389s