from flask import Flask, render_template, redirect, url_for
from api import CatApi, DogApi


app = Flask(__name__)

@app.route('/')
def Home():
    return redirect(url_for('Cat'))

@app.route('/cat')
def Cat():
    img_link =  CatApi()
    return render_template("index.html", img_link=img_link, animal="cat", sound="meow")

@app.route('/dog')
def Dog():
    img_link =  DogApi()
    return render_template("index.html", img_link=img_link, animal="dog", sound="woof")

if __name__ == '__main__':
    app.run(debug=True)