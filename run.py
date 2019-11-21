from flask import Flask
from flask import render_template
from flask_restful import Resource, Api
import slack

#Librebrias para el envio de correo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

client = slack.WebClient(token='')

app = Flask(__name__)
api = Api(app)

def senderMail(password,From,to, subject, message,SMTP_server,port):
	# create message object instance
	msg = MIMEMultipart()
	 
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
	 
	#create server
	server = smtplib.SMTP('%s:%s' % SMTP_server, port)
	 
	server.starttls()
	 
	# Login Credentials for sending the mail
	server.login(From, password)
	 
	 
	# send the message via the server.
	server.sendmail(From, to, message.as_string())
	 
	server.quit()


@app.route('/')
def index():
    return render_template("index.html")


class Hello(Resource):
    def get(self, name):
        return {"Hello":name}

#ToDo: Enviar mensajes que estén pendientes en bbdd
class sendMail(Resource):
	def get(self):
		return{"Enviando...":"ok"}

class sendSlack(Resource):
	def get(self,message,channel):
		response = client.chat_postMessage(
    		channel=channel,
    		text=message)
		print(response)
		return {"Status":response["ok"]}

#ToDo terminar de parametrizar
class sendAskSlack(Resource):
	def get(self, message,channel):

		task_id = 'LB-2375'
		attachments = [
		    {
		        "fallback": "Upgrade your Slack client to use messages like these.",
		        "color": "#CC0000",
		        "actions": [
		            {
		                "type": "button",
		                "text": ":blue_circle:   SI",
		                "url": "https://roach.ngrok.io/workflow/" + task_id,
		            },
		            {
		                "type": "button",
		                "text": ":red_circle:   NO",
		                "url": "https://roach.ngrok.io/workflow/" + task_id,
		            }
		        ]
		    }
		]
		response = client.chat_postMessage(
		    channel=channel,
		    text=message,
		    attachments=attachments)
		return {"Status":response["ok"]}

@app.errorhandler(404) 
def page_not_found(error):
    return 'Web no encontrada'    

#Rutas de la API
api.add_resource(Hello, '/hello/<name>')
api.add_resource(sendSlack, '/sendSlack/<message>/<channel>')
api.add_resource(sendAskSlack, '/sendAskSlack/<message>/<channel>')
api.add_resource(sendMail, '/sendMail')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
