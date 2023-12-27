from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_usarname(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuario já existe! Cadastre outro nome de usuário por favor.")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Este E-mail já existe! Cadastre outro E-mail por favor.")

    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Esta senha já existe! Cadastre outra senha por favor.")

    usuario = StringField(label='Username:', validators=[length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Password:', validators=[length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmation of password:', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    usuario = StringField(label='User:', validators=[DataRequired()])
    senha = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Log in')
    
class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label="Buy Product!") 

class VendaProdutoForm(FlaskForm):
    submit = SubmitField(label="Sell Product!")  
    
    