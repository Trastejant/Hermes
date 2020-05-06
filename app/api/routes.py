from flask import abort, render_template,jsonify, request
import json
from . import api

@api.route("/test")
def test():   
	mensaje = "OK"
	return json.dumps(mensaje)

@api.route("/echo", methods=['POST'])
def echo():   
	if not request.form:
		return "Error de parámetros",403

	if not "for" in request.form:
		return "El destinatario es un parámetro requerido",403

	if not "mensaje" in request.form:
		return "El mensaje es un parámetro requerido",403

	print(request.form['name'])
	return json.dumps(request.form['name'])


@api.route("/recibir", methods=['POST'])
def recibir(): 
	content = request.get_json(force=True)
	print(content)

	if not "for" in content.keys():
		return "El destinatario es un párametro requerido",403

	return json.dumps(content)
