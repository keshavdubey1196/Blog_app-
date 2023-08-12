from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, \
     BooleanField, PasswordField
from wtforms.validators import InputRequired, Length, \
      Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password',  [InputRequired(), EqualTo(
        'confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(
            username=username.data
        ).first()
        if user:
            raise ValidationError('That username is taken. Chose a different.')

    def validate_email(self, email):
        user = User.query.filter_by(
            email=email.data
        ).first()
        if user:
            raise ValidationError('That email is taken. Chose a different.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    picture = FileField(
        'Update profile pic', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(
                username=username.data
            ).first()
            if user:
                raise ValidationError(
                    'That username is taken. Chose a different.'
                    )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(
                email=email.data
            ).first()
            if user:
                raise ValidationError(
                    'That email is taken. Chose a different.'
                    )


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request Passowrd Reset')

    def validate_email(self, email):
        user = User.query.filter_by(
            email=email.data
        ).first()
        if not user:
            raise ValidationError(
                'There is no account with this email. You must register first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',  [InputRequired(), EqualTo(
        'confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Reset Password')
