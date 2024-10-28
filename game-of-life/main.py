import flask
from werkzeug import Response

from core import config
from game import GameOfLife
from forms import WorldForm


class FlaskConfig:
    SECRET_KEY = config.secret


app = flask.Flask(__name__)
app.config.from_object(FlaskConfig)
app.jinja_env.filters["zip"] = zip


@app.route("/", methods=["GET", "POST"])
def index() -> str | Response:
    if flask.request.method not in ("GET", "POST"):
        flask.abort(405, "Only 'GET' and 'POST' methods allowed")
        return

    form = WorldForm()
    if flask.request.method == "POST" and form.validate_on_submit():
        GameOfLife(form.width.data, form.height.data, form.velocity.data)
        return flask.redirect(flask.url_for("life"))

    return flask.render_template(
        "index.html",
        form=form,
    )


@app.route("/life", methods=["GET", "POST"])
def life() -> str | Response:
    if flask.request.method not in ("GET", "POST"):
        flask.abort(405, "Only 'GET' and 'POST' methods allowed")
        return

    if flask.request.method == "GET":
        return flask.render_template("life.html")

    game = GameOfLife()
    game.form_new_generation()
    return flask.jsonify(
        {
            "life_count": game.life_count,
            "world": game.world,
            "prev_world": game.previous_world,
        }
    )


if __name__ == "__main__":
    app.run(host=config.addr, port=config.port, debug=config.debug)
