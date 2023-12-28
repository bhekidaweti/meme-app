from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import json



app = Flask('app')

#memes_archive = []  This code store generated memes temporaly in memory in a list

##The following code stores generated memes in a SQLIte database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memes.db'  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#class represents the structure of the database table
class ArchivedMeme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meme_url = db.Column(db.String(255), nullable=False)
    subreddit = db.Column(db.String(255), nullable=False)

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
   # memes_archive.append((meme_pic, subreddit))  # Save the meme to the archive temporaly
    save_to_database(meme_pic, subreddit)
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/archives")
def archives():
    memes = ArchivedMeme.query.all()
    return render_template("archives.html", memes=memes)

@app.route("/about")
def about():
    return render_template("about.html")

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

def save_to_database(meme_pic, subreddit):
    archived_meme = ArchivedMeme(meme_url=meme_pic, subreddit=subreddit)
    db.session.add(archived_meme)
    db.session.commit()




if __name__ == '__main__':
    db.create_all()  # Create database tables before running the app
    app.run(host='0.0.0.0', port=5000)



