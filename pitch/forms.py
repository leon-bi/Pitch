from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from pitch.models import User
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()] )
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username is taken please choose a different one')
    
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken please choose a different one')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()] )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email= StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset',)

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no Account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('password',validators=[DataRequired()] )
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')