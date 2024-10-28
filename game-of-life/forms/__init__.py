"""
Forms for Game of Life Application

This module contains forms used for receiving user data. It utilizes Flask-WTF and
WTForms to create forms that allows users to input and submit user data.

Classes:
--------
WorldForm(FlaskForm):
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
        A float input field for specifying the velocity of the generation world.
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
            velocity = form.velocity.data or 1.0
            # Proceed to create the game with specified dimensions
        return render_template("index.html", form=form)
```
"""

from .form import WorldForm

__all__ = ["WorldForm"]
