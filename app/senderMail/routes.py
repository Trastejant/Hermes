from flask import abort, render_template,jsonify, request
import json
from . import senderMail
from flask_mail import Message, Mail

mail = Mail() 

@senderMail.route("/senderMail/test")
def test():   
	return "ok",200

@senderMail.route("/senderMail/send", methods=['POST'])
def enviar(): 
	content = request.get_json(force=True)

	if not "destinatario" in content.keys():
		return "El destinatario es un párametro requerido",403

	if not "asunto" in content.keys():
		return "El asunto es un párametro requerido",403

	if not "mensaje" in content.keys():
		return "No puedes enviar un email sin contenido",403

	msg = Message(content['asunto'],recipients=content['destinatario'])
	msg.body(content['mensaje'])
	mail.send(msg)
	return {"Status":response["ok"]}