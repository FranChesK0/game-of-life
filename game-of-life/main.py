from flask import Flask, render_template

from game import GameOfLife

app = Flask(__name__)


@app.route("/")
def index() -> str:
    GameOfLife(25, 25)
    return render_template("index.html")


@app.route("/live")
def live() -> str:
    game = GameOfLife()
    game.form_new_generation()
    return render_template("live.html", world=game.world)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
