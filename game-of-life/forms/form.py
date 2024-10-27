from wtforms import SubmitField, IntegerField  # type: ignore[import-untyped]
from flask_wtf import FlaskForm  # type: ignore[import-untyped]
from wtforms.validators import NumberRange, InputRequired  # type: ignore[import-untyped]


class WorldSizeForm(FlaskForm):  # type: ignore[no-any-unimported]
    width = IntegerField(
        "World width",
        validators=[NumberRange(4, 30), InputRequired()],
    )
    height = IntegerField(
        "World height",
        validators=[NumberRange(4, 30), InputRequired()],
    )
    submit: SubmitField = SubmitField("Create")  # type: ignore[no-any-unimported]
