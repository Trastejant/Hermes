from flask import abort, render_template,jsonify

from . import public

@public.route("/")
def index():   
	opciones = [1,2,3,4,5,6]
	return render_template("index.html", opciones=opciones)