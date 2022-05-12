from flask import Flask, render_template, abort, request
app = Flask(__name__)

import json

from operator import  eq
with open("msx.json") as fichero:
    datos_json=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("inicio.html")
    
@app.route('/juegos')
def juegos():
    categorias=[]
    categorias.append("")
    for i in datos_json:
        if i["categoria"] not in categorias:
            categorias.append(i["categoria"])
    categorias.sort()
    if request.method=="GET":
        return render_template("juegos.html",categorias=categorias)
    else:
        nombre=request.form.get("name")
        categoria=request.form.get("category")
        for i in datos_json:
            if (nombre == "" or str(i["nombre"]).startswith(nombre)) and (categoria == "" or categoria == i["categoria"]):
                return render_template('juegos.html',juegos=datos_json,nombre=nombre,categoria=categoria,categorias=categorias)
        return render_template('juegos.html',nombre=nombre,categoria=categoria,categorias=categorias)

app.run("0.0.0.0",5000,debug=True)