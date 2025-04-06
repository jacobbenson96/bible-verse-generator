from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

# Load verses once at startup
with open("verses.json") as f:
    verses = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_verse():
    verse = random.choice(verses)
    return jsonify(verse)

@app.route("/romans-road")
def romans_road():
    return render_template("romans_road.html")


if __name__ == "__main__":
    app.run(debug=True)
