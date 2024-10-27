from wtforms import SubmitField, IntegerField  # type: ignore[import-untyped]
from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms.validators import NumberRange, InputRequired  # type: ignore[import-untyped]


class WorldSizeForm(FlaskForm):  # type: ignore[no-any-unimported]
    """
    A form that allows users to specify the width and height of the game world.
    Both fields have input validation to ensure the values are within a valid range.

    Attributes:
    -----------
    width: IntegerField
        An integer field for specifying the width of the game world.
        It accepts values between 4 and 30 (inclusive) and is required.

    height: IntegerField
        An integer input field for specifying the height of the game world.
        It accepts values between 4 and 30 (inclusive) and is required.

    submit: SubmitField
        A button to submit the form and create the game world based on the provided
        dimensions.

    Usage:
    ------
    The `WorldSizeForm` can be used in a Flask application to gather user input for
    configuration the game world. For example:

    ```python
    from forms import WorldSizeForm


    @app.route("/", methods=["GET", "POST"])
    def index():
        form = WorldSizeForm()
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
    submit: SubmitField = SubmitField("Create life")  # type: ignore[no-any-unimported]
