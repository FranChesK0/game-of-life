from flask import Flask, render_template

from core import config
from game import GameOfLife

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip


@app.route("/")
def index() -> str:
    GameOfLife(25, 25)
    return render_template("index.html")


@app.route("/life")
def life() -> str:
    game = GameOfLife()
    game.form_new_generation()
    return render_template(
        "life.html",
        life_count=game.life_count,
        world=game.world,
        prev_world=game.previous_world,
    )


if __name__ == "__main__":
    app.run(host=config.addr, port=config.port, debug=config.debug)
