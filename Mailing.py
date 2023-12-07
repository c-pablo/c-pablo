# -

"""# ENVIAR IMAGENES POR CORREO"""

#enviar email al interesado

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# create message object instance
msg = MIMEMultipart()
message= 'Se adjuntan las imagenes de test pasadas por el modelo entrenado'
# setup the parameters of the message
password = "*********"
msg['From'] = ""
msg['To'] = ""
msg['Subject'] = ""
msg.attach(MIMEText(message, 'plain'))
for i in range(6):
#Abrir imagen que se desea enviar
    imagen = open("gif_frame_" + ('%02d' % i) + ".jpg",'rb')
    img = MIMEImage(imagen.read())
# add in the message body
    msg.attach(img)
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))