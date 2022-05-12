from flask import Flask, render_template, abort, request
app = Flask(__name__)

import json
import os

from operator import  eq
with open("msx.json") as fichero:
    datos_json=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("inicio.html")
    
@app.route('/juegos',methods=["GET","POST"])
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
        nombre=request.form.get("juego")
        categoria=request.form.get("categoria")
        for i in datos_json:
            if (nombre == "" or str(i["nombre"]).startswith(nombre)) and (categoria == "" or categoria == i["categoria"]):
                return render_template('juegos.html',juegos=datos_json,nombre=nombre,categoria=categoria,categorias=categorias)
        return render_template('juegos.html',nombre=nombre,categoria=categoria,categorias=categorias)

@app.route('/juego/<int:identificador>')
def juego(identificador):
    for ide in datos_json:
        if ide["id"] == identificador:
            return render_template('juego.html',juego=ide)
    abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)