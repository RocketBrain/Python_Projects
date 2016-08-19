import requests

def get_weather_forecast():
        # Getting the weather api
	url = 'http://api.openweathermap.org/data/2.5/weather?q=Seattle&units=imperial&appid=f1b81dde8a3d3bdd586fcca0eb43f61a'	
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	
        # Parsing_JSON
	description = weather_json['weather'][0]['description']
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']
	
        # Creating forecast string
	forecast = "The forecast in Seattle for today is" + " " 
	forecast += description + " " + "with a minimum temperature of " + str(int(temp_min)) 
	forecast += " and a high of " + str(int(temp_max))
	forecast += "."

	return forecast
	 

	
