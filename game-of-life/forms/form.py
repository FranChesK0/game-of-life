from wtforms import FloatField, SubmitField, IntegerField  # type: ignore[import-untyped]
from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms.validators import NumberRange, InputRequired  # type: ignore[import-untyped]


class WorldForm(FlaskForm):  # type: ignore[no-any-unimported]
    """
    A form that allows users to specify the width and height of the game world and
    the velocity of the world generation.
    Both fields have input validation to ensure the values are within a valid range.

    Attributes:
    -----------
    width: IntegerField
        An integer field for specifying the width of the game world.
        It accepts values between 4 and 30 (inclusive) and is required.

    height: IntegerField
        An integer input field for specifying the height of the game world.
        It accepts values between 4 and 30 (inclusive) and is required.

    velocity: FloatField
        A float input field for specifying the velocity of the generation new world.
        It accepts values between 0.1 and 5 (inclusive) and defaults to 1.0.

    submit: SubmitField
        A button to submit the form and create the game world based on the provided
        dimensions.

    Usage:
    ------
    The `WorldSizeForm` can be used in a Flask application to gather user input for
    configuration the game world. For example:

    ```python
    from forms import WorldForm


    @app.route("/", methods=["GET", "POST"])
    def index():
        form = WorldForm()
        if form.validate_on_submit():
            width = form.width.data
            height = form.height.data
            # Proceed to create the game with specified dimensions
        return render_template("index.html", form=form)
    ```
    """

    width = IntegerField(
        "World width (from 4 to 30)",
        validators=[NumberRange(4, 30), InputRequired()],
    )
    height = IntegerField(
        "World height (from 4 to 30)",
        validators=[NumberRange(4, 30), InputRequired()],
    )
    velocity = FloatField(
        "Generation velocity (from 0.1 to 5.0)",
        validators=[NumberRange(0.1, 5.0)],
        default=1.0,
    )
    submit: SubmitField = SubmitField("Create life")  # type: ignore[no-any-unimported]
