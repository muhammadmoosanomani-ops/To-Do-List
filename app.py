# imports 
from flask import Flask, render_template, redirect, request

#from flask_scss import Scss # (Vercel doesn't support runtime SCSS compilation natively)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# My App Setup
app = Flask(__name__)
#Scss(app) # (Disabled for production deployment)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Data Class ~ Row of Data
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Karachi")))

    def __init__(self, content: str, complete: int = 0):
        self.content = content
        self.complete = complete

    def __repr__(self) -> str:
        return f"Task {self.id}"


with app.app_context():
    db.create_all()
        

#Routes to Webpages
#Home page
@app.route("/", methods=["POST", "GET"])
def index():
    #ADD a Task
    if request.method == "POST":
        current_task = request.form['content']
        new_task= MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
         #See all current tasks
    else: 
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)


#Delete an item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"


#Edit an item
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id:int):
    task= MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template('edit.html', task=task)

#rRunner & Debugger
if __name__ == "__main__":
    app.run(debug=True)
