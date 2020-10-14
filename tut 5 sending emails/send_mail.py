# Library
import smtplib

def send_mail(sender, reciever) :
	# creates SMTP session 
	session = smtplib.SMTP('smtp.gmail.com', 587) 
	
	# start TLS for security 
	session.starttls() 
	
	# message to be sent 
	message = 'from python mail'
	
	# Authentication
	password = input("Enter your password : ")
	session.login(sender, password)

	# sending the mail
	session.sendmail(sender, reciever, message) 
	
	# terminating the session 
	session.quit()

if __name__ == '__main__':
	sender = 'smagni1002@gmail.com'
	reciever = 'chhabraashish123@gmail.com '
	send_mail(sender, reciever)