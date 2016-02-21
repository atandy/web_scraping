import requests
import bs4
import json

#panels = [2,3,4]
url = "http://www.timeout.com/newyork/restaurants/100-best-new-york-restaurants#tab_panel_1"
restaurant_list_of_dicts = []

requests.get(url.format(url)).content
soup = bs4.BeautifulSoup(r)
 #TODO: iterate through all panels. 
for i in soup.findAll('a'):
	data_tracking = i.get('data-tracking')
	if data_tracking:
		dt_json = json.loads(data_tracking)
		content_name =  dt_json['attributes'].get('contentName')
		if content_name and content_name.count(' ') < 4:
			d = {'restaurant_name': content_name }
			restaurant_list_of_dicts.append(d)