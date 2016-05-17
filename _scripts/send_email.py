#! /usr/bin/python
# coding: utf-8

import smtplib
import sys
from mailer import Mailer
from mailer import Message
import yaml
import html2text
import codecs
# me == my email address
# you == recipient's email address

FROM="contact@onsensouviendra.fr"
PASS=sys.argv[1]
HOST="ssl0.ovh.net"
PORT=587

def sendEmail(to, subject, html) :
	
	try:
		print "Envoi à %s ..." % to
		message = Message(From=FROM, To=to, charset="utf-8")
		message.Subject = subject
		message.Html = html
		message.Body = html2text.html2text(html)

		sender = Mailer(HOST, use_tls=True, port=587, usr=FROM , pwd=PASS)
		sender.send(message)
		print "Envoi à %s réussi" % to
	except:
		print "Erreur à l'envoir pour %s : " % to, sys.exc_info()[0]

deputes = yaml.safe_load(sys.stdin)
for depute in deputes :
	with codecs.open ("_site/lettres/%s.html" % depute["id"], "r", encoding='utf8') as f:
		html = f.read()
	subject = u"Lettre ouverte à %s, publiée sur onsensouviendra.fr" % (depute["nom"])
	if "email_1" in depute and depute["email_1"] is not None :
		sendEmail(depute["email_1"] , subject, html)
	if "email_2" in depute and depute["email_2"] is not None :
		sendEmail(depute["email_2"], subject, html)
