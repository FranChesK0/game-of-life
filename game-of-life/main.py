import flask
from werkzeug import Response

from core import config
from game import GameOfLife
from forms import WorldSizeForm


class FlaskConfig:
    SECRET_KEY = config.secret


app = flask.Flask(__name__)
app.config.from_object(FlaskConfig)
app.jinja_env.filters["zip"] = zip


@app.route("/", methods=["GET", "POST"])
def index() -> str | Response:
    if flask.request.method not in ("GET", "POST"):
        flask.abort(405, "Only 'GET' and 'POST' methods")
        return

    form = WorldSizeForm()
    if flask.request.method == "POST" and form.validate_on_submit():
        GameOfLife(form.width.data, form.height.data)
        return flask.redirect(flask.url_for("life"))

    return flask.render_template(
        "index.html",
        form=form,
    )


@app.route("/life")
def life() -> str:
    game = GameOfLife()
    game.form_new_generation()
    return flask.render_template(
        "life.html",
        life_count=game.life_count,
        world=game.world,
        prev_world=game.previous_world,
    )


if __name__ == "__main__":
    app.run(host=config.addr, port=config.port, debug=config.debug)
