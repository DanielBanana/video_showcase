from flask import Flask, render_template

app = Flask(__name__)

# Sample videos
videos = [
    {"title": "Poster", "filename": "output.mp4", "description": "This is the first video."},
]

@app.route("/")
def index():
    return render_template("index.html", videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
