#se quiere que la pagina sea invocada
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect

import forms
app=Flask(__name__)

app.config['SECRET_KEY'] = 'esta es tu clave encriptada'
csrf = CSRFProtect()

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cookie", methods = ['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', form = reg_user))
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        pasw = reg_user.password.data
        datos = user + "@" + pasw
        succes_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(succes_message)
    return response


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method == 'POST' and reg_alum.validate():
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data
    return render_template('Alumnos.html', form = reg_alum, mat = mat, nom = nom)


@app.route('/Traductor', methods=['GET', 'POST'])
def traductor():
    reg_tra = forms.UseForm3(request.form)
    ing = ''
    esp = ''
    if request.method == 'POST' and reg_tra.validate():
        ing = reg_tra.Ingles.data
        esp = reg_tra.Español.data
        file = open('palabras.txt','a')
        file.write('\n' + ing)
        file.write('\n' + esp)
        file.close()
    return render_template('Traductor.html', form = reg_tra, ing = ing, esp = esp)



if __name__ == "__main__":
    
    app.run(debug=True,port=3000)
