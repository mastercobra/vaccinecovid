"""
	@author: javiern_n@ciencias.unam.mx
"""

import requests
import time
import smtplib

#Unlock recaptcha, create app password
#https://support.google.com/accounts/answer/185833?hl=es-419&ctx=ch_b%2F0%2FDisplayUnlockCaptcha

success = True

while success:
	try:
		payload = {'curp': ''}#Aqui va el curp
		r = requests.post('https://mivacuna.salud.gob.mx/bcurps.php', verify=False, data=payload)
		status_code = r.status_code
		respuesta = r.text

		print(status_code)
		if "Sin respuesta" not in respuesta and 'The server encountered a temporary error' not in respuesta:
			success = False
			print("Sin respuesta" not in respuesta)
			print('The server encountered a temporary error' not in respuesta)
			gmail_user = ''#Correo remitente
			gmail_password = ''#Contrasenia remitente

			sent_from = gmail_user
			to = ['javiern_n@ciencias.unam.mx'] #Arreglo de destinatarios
			subject = 'OMG Super Important Message'
			body = "Hey, what's up?\n\nCovid Vaccine is ready"

			email_text = """\
			From: %s
			To: %s
			Subject: %s 

			%s""" % (sent_from, ", ".join(to), subject, body)

			try:
			    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			    server.ehlo()
			    server.login(gmail_user, gmail_password)
			    server.sendmail(sent_from, to, email_text)
			    server.close()

			    print('Email sent!')
			except Exception as e:
				print(e)
				print('Something went wrong...')
		else:
			print("Sin respuesta exitosa, durmiendo como panda")
			time.sleep(5)
	except Exception as e:
	 print("Intentando de nuevo: " + str(e))

