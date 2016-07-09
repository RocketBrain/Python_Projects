
import requests

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
	url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=f1b81dde8a3d3bdd586fcca0eb43f61a'	
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	

	description = weather_json['weather']
	print (description)

def main():
	emails = get_emails()
	print(emails)

	schedule = get_schedule()
	print(schedule)

	get_weather_forecast()

main()	