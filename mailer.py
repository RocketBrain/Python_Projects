import smtplib

def send_emails(emails, schedule, forecast):
	# Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    #Start TLS encryption
    server.starttls()

    # Login
    password = raw_input("What is your password?")
    from_email = "from_email@gmail.com"
    to_email = "to_email@gmail.com"
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = "Subject: Forecast mailer using Python\n"
        message += "What's up " + name + ", I am testing a forecast mailer using Python,\n"
        message += "which retrieves a weather API and sends an e-mail to people on my list.\n\n "
        message += "This entire e-mail is being generated using Python code.\n\n"
        message += "(cue forecast variable!)\n\n" + forecast + "\n \n"
        message += "The following code also generates a schedule: \n\n" + schedule
        server.sendmail(from_email, to_email, message)
            

 
   
            
    server.sendmail(from_email, to_email, message)

    
    server.quit()
