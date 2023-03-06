from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators 

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message = 'El campo es requerido ')])
    amaterno = StringField('Amaterno', [mi_validacion])
    apaterno = StringField('Apaterno')
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])
    password = StringField('password',[
        validators.DataRequired(message = 'El campo es requerido '),
        validators.length(min = 4, max = 10, message = 'lomg de campo 4 min and 5 max')
    ])

class IdiomasForm(Form):
    esp = StringField("Español", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    eng = StringField("Ingles:      ", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    bus = StringField("Palabra", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    opc = SelectField('Lenguaje',choices=[('esp','Español: '),('eng','Ingles')])
    
class Resistencias(Form):
    band1 = SelectField("Banda 1", [
        validators.DataRequired(message='El campo es requerido')
    ], choices=[
        ('0', 'Negro'),
        ('1', 'Marrón'),
        ('2', 'Rojo'),
        ('3', 'Naranja'),
        ('4', 'Amarillo'),
        ('5', 'Verde'),
        ('6', 'Azul'),
        ('7', 'Violeta'),
        ('8', 'Gris'),
        ('9', 'Blanco')
    ])
    
    band2 = SelectField("Banda 2", [
        validators.DataRequired(message='El campo es requerido')
    ], choices=[
        ('0', 'Negro'),
        ('1', 'Marrón'),
        ('2', 'Rojo'),
        ('3', 'Naranja'),
        ('4', 'Amarillo'),
        ('5', 'Verde'),
        ('6', 'Azul'),
        ('7', 'Violeta'),
        ('8', 'Gris'),
        ('9', 'Blanco')
    ])
    
    band3 = SelectField("Banda 3", [
        validators.DataRequired(message='El campo es requerido')
    ], choices=[
        ('1', 'Marrón'),
        ('10', 'Rojo'),
        ('100', 'Naranja'),
        ('1000', 'Amarillo'),
        ('10000', 'Verde'),
        ('100000', 'Azul'),
        ('1000000', 'Violeta'),
        ('10000000', 'Gris'),
        ('100000000', 'Blanco'),
        ('0.1', 'Dorado'),
        ('0.01', 'Plateado')
    ])
    
    tolerancia = SelectField("Tolerancia", [
        validators.DataRequired(message='El campo es requerido')
    ], choices=[
        ('1', 'Marrón'),
        ('2', 'Rojo'),
        ('0.5', 'Verde'),
        ('0.25', 'Azul'),
        ('0.1', 'Violeta'),
        ('5', 'Oro'),
        ('10', 'Plateado')
    ])