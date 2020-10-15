# Library
import smtplib

def email(sender, reciever, subject, message, password) :
	final_msg = f"Subject: {subject}\n\n{message}"

	# creates SMTP session
	session = smtplib.SMTP('smtp.gmail.com', 587) 
	
	# start TLS for security 
	session.starttls() 
	
	# Authentication
	session.login(sender, password)

	# sending the mail
	session.sendmail(sender, reciever, final_msg)
	
	# terminating the session 
	session.quit()