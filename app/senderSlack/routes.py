from flask import abort, render_template,jsonify, request
import json
from . import senderSlack
import slack
import configparser
import os
#config = configparser.ConfigParser()
#config.read('config.ini')

#with open('config.json', 'r') as file:
#    config = json.load(file)

#client = slack.WebClient(token='xoxb-290501828145-824715819074-N27pIGwNg8RbyVKGa8DS95Td')
client = slack.WebClient(token=os.environ.get('SLACK_TOKEN', None))

@senderSlack.route("/slack/test")
def test():   
	return "ok",200

@senderSlack.route("/slack/send", methods=['POST'])
def enviar(): 
	content = request.get_json(force=True)

	if not "channel" in content.keys():
		return "El canal es un párametro requerido",403

	if not "message" in content.keys():
		return "No puedes enviar un mensaje vacio",403

	response = client.chat_postMessage(
    	channel=content['channel'],
    	text=content['message'])	

	return {"Status":response["ok"]}


@senderSlack.route("/slack/ask", methods=['POST'])
def ask(): 
	content = request.get_json(force=True)

	if not "task_id" in content.keys():
		task_id = '0'
	else:
		task_id = content['task_id']

	if not "color" in content.keys():
		color = "#CC0000"
	else:
		color = content['color']

	if not "url_return_btn1" in content.keys():
		return "debe indicar una URL de retorno",403

	if not "url_return_btn2" in content.keys():
		return "debe indicar una URL de retorno",403

	if not "txt_btn1" in content.keys():
		ask1 = "Sí"
	else:
		ask1 = content['txt_btn1']

	if not "txt_btn2" in content.keys():
		ask2 = "No"
	else:
		ask2 = content['txt_btn2']

	attachments = [
	    {
	        "fallback": "Upgrade your Slack client to use messages like these.",
	        "color": color,
	        "actions": [
	            {
	                "type": "button",
	                "text": ":red_circle: " + ask1,
	                "url": content['url_return_btn1'] + task_id,
	            },
	            {
	                "type": "button",
	                "text": ":red_circle: " + ask2,
	              	"url": content['url_return_btn2'] + task_id,
	            }
	        ]
	    }
	]
	response = client.chat_postMessage(
    	channel=content['channel'],
    	text=content['message'],
    	attachments=attachments)
	
	return {"Status":response["ok"]}
