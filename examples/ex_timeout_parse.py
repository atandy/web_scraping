import requests
import bs4
import json

panels = [2,3,4]
url = "http://www.timeout.com/newyork/restaurants/100-best-new-york-restaurants#tab_panel_{}"

restaurant_list_of_dicts = []
for panel in panels:
	requests.get(url.format(url.format(panel))).content
	soup = bs4.BeautifulSoup(r)
	 #TODO: iterate through all panels. 
	for link in soup.findAll('a'):
		data_tracking = link.get('data-tracking')
		if data_tracking:
			dt_json = json.loads(data_tracking)
			content_name =  dt_json['attributes'].get('contentName')
			if content_name and content_name.count(' ') < 4:
				d = {'restaurant_name': content_name }
				restaurant_list_of_dicts.append(d)

# write the results to a CSV.
with open('restaurants.csv', 'w') as csvfile:
    fieldnames = restaurant_list_of_dicts[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for restaurant in restaurant_list_of_dicts:
        writer.writerow(restaurant)