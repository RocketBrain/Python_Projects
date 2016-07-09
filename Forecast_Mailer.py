
import requests
import smtplib

def get_emails():
	emails = {}
	try:
	    email_file = open('emails2.txt', 'r')

	    for line in email_file:
		    (email,name) = line.split(',')
		    emails[email] = name.strip()

	except IOError:
	    print("File does not exist.")		
		
	return emails

def get_schedule():
	try:
	    schedule_file = open('schedule.txt', 'r')
	    schedule = schedule_file.read()
	except IOError:
	    print("File does not exist.")    

	return schedule

def get_weather_forecast():
	url = 'http://api.openweathermap.org/data/2.5/weather?q=Seattle&units=imperial&appid=f1b81dde8a3d3bdd586fcca0eb43f61a'	
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	print(weather_json)

	description = weather_json['weather'][0]['description']
	

	temp_min = weather_json['main']['temp_min']
	

	temp_max = weather_json['main']['temp_max']
	

	forecast = "The forecast in Seattle for today is" + " " 
	forecast += description + " " + "with a minimum temperature of " + str(int(temp_min)) 
	forecast += " and a high of " + str(int(temp_max))
	forecast += "."

	return forecast
	 

	print(forecast)

def send_emails(emails, schedule, forecast):
	# Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    #Start TLS encryption
    server.starttls()

    # Login
    password = raw_input("What is your password?")
    from_email = "my_email@gmail.com"
    to_email = "your_email.com"
    server.login(from_email, password)
    
    #Send email
    message = "Subject: Seattle forecast using Python\n"
    message += "What's up Josh. I am testing a forecast mailer using Python,\n"
    message += "which retrieves a weather API and sends an e-mail to people on my list.\n\n "
    message += "This entire e-mail is being generated using Python code.\n\n"
    message += "(cue forecast variable!)\n\n" + forecast
   
            
    server.sendmail(from_email, to_email, message)

    
    server.quit()


def main():
	emails = get_emails()
	print(emails)

	schedule = get_schedule()
	print(schedule)

	forecast = get_weather_forecast()
	print(forecast)

	send_emails(emails, schedule, forecast)

main()	
