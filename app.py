#se quiere que la pagina sea invocada
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect
from flask import Flask, render_template, request, redirect, url_for


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
def diccionario():
    reg_language = forms.IdiomasForm(request.form)
    esp = ""
    eng = ""
    opc = ""
    bus = ""
    palabra = ""
    idioma = ""
    if request.method == 'POST':
        esp = reg_language.esp.data
        eng = reg_language.eng.data
        opc = reg_language.opc.data
        bus = reg_language.bus.data
        if esp != None and eng != None:
            add_dictionary(eng, esp)
        if opc != None and bus != None:
            palabra = search_dictionary(opc, bus)
            if opc == "eng":
                idioma = "English"
            else:
                idioma = "Español"
    return render_template('traductorh.html',form = reg_language, palabra = palabra, idioma = idioma)


@app.route('/Resistencias', methods=['GET', 'POST'])
def calcular_resistencia():
    form = forms.Resistencias(request.form)
    valor = 0
    valor_max = 0
    valor_min = 0
    band1_valor = 0
    band2_valor = 0
    band3_valor = 0
    tolerancia_valor = 0
    if request.method == 'POST' and form.validate():
        band1_valor = int(form.band1.data)
        band2_valor = int(form.band2.data)
        band3_valor = float(form.band3.data)
        tolerancia_valor = float(form.tolerancia.data)
        valor = ((band1_valor * 10) + band2_valor) * band3_valor
        valor_min = valor * (1 - (tolerancia_valor / 100))
        valor_max = valor * (1 + (tolerancia_valor / 100))
        
        # Guardar los datos en un archivo de texto
        with open("resistencias.txt", "a") as archivo:
            archivo.write(f"{band1_valor},{band2_valor},{band3_valor},{tolerancia_valor},{valor},{valor_min},{valor_max}\n")
    
    # Leer los datos del archivo de texto y mostrarlos en la tabla
    datos = []
    with open("resistencias.txt", "r") as archivo:
        for linea in archivo:
            datos.append(linea.strip().split(","))
            
    return render_template('resistencias.html', form=form, datos=datos)


def add_dictionary(eng, esp):
    file = open('traduccion.txt','a')
    file.write(eng.lower())
    file.write("\n")
    file.write(esp.lower())
    file.write("\n")
    file.close()

def search_dictionary(opc, bus):
    file = open('traduccion.txt','r')
    resultado = file.read()
    datos = resultado.lower().split() # convertir todo a minúsculas
    i = 0
    palabra = ""
    
    if opc == "eng":
        for x in datos:
            if x == bus.lower(): # comparar en minúsculas
                palabra = datos[i-1] 
                if i%2 == 0:
                    palabra = "Term in English"
            if palabra == "":
                palabra = "Word not found"
            i += 1
    else:
        for x in datos:
            if x == bus.lower(): # comparar en minúsculas
                palabra = datos[i+1]
                if i%2 != 0:
                    palabra = ""
            if palabra == "":
                palabra = "Palabra no encontrada"
            i += 1
            
    return palabra

@app.route('/limpiar', methods=['POST'])
def limpiar():
    with open("resistencias.txt", "w") as archivo:
        archivo.write("")
    return redirect(url_for('calcular_resistencia'))

                


if __name__ == "__main__":
    
    app.run(debug=True,port=3000)
