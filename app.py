from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rsyonbjjapxoux:ae2e7a8266842b524c12ab22bc998831de29a32da98e48f36f3897b022005e7c@ec2-54-235-240-92.compute-1.amazonaws.com:5432/d7i4evh2mijbkp?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(120), unique = False)
    user_email = db.Column(db.String(120), unique = True)
    user_message = db.Column(db.String(1000), unique = False)

    def __init__(self, user_name, user_email, user_message):
        self.user_name = user_name
        self.user_email = user_email
        self.user_message = user_message
    



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        send_email(name, email, message)
        if db.session.query(Data).filter(Data.user_email == email).count() == 0:
            data = Data(name, email, message)
            db.session.add(data)
            db.session.commit()
            return render_template('index.html')
    return render_template('index.html',
    text = "Seems like we've got something from that email address already!")


if __name__ == '__main__':
    app.run(debug=True)