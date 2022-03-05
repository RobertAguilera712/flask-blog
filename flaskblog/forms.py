from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', 
                            validators=[DataRequired("Please provide a username"), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm password', 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sing Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(label='Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', 
                            validators=[DataRequired()])
    remember = BooleanField(label='Remember me')
    submit = SubmitField(label='Log In')