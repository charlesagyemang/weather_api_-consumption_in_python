import requests

def get_weather_condition_on_my_dat_of_birth(date, city, api_key):
	url = 'http://api.wunderground.com/api/' + api_key + '/history_'+ date +'/q/CA/' + city + '.json'
	r = requests.get(url)
	observations = r.json()['history']['observations']
	return observations



date = str(raw_input("date of birth in this format yearMonthDay: "))
city = str(raw_input("birth city start with a capital letter: "))
api_key = 'bf26229602942324'

observations =  get_weather_condition_on_my_dat_of_birth(date, city, api_key)
print observations