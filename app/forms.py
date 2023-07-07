from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import SubmitField, TextAreaField, fields, DecimalRangeField
from wtforms.validators import DataRequired, NumberRange


class VoiceForm(FlaskForm):
    file = fields.FileField('Voice', validators=[DataRequired()])
    slider = DecimalRangeField('Slider', default=0.5, validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Submit')


class OcrForm(FlaskForm):
    img = fields.FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    slider = DecimalRangeField('Slider', default=0.5, validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Submit')


class DocumentForm(FlaskForm):
    document = fields.FileField('Document', validators=[DataRequired()])
    slider = DecimalRangeField('Slider', default=0.5, validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Submit')


class TxtForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    slider = DecimalRangeField('Slider', default=0.5, validators=[DataRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Submit')
