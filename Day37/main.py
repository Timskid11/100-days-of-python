import requests
import datetime
USERNAME = "timilehin"
TOKEN = "timtheeng"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

'''response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)'''

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {

    "id": ID,
    "name" : "Coding Graph",
    "unit" : "Hours",
    "type" : "float",
    "color" : "ajisai"

}
headers = {
    "X-USER-TOKEN": TOKEN,
}

'''response =requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text )'''

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
today = datetime.datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?  "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"

new_pixel_config = {
    "quantity": "4",
}

'''response1 = requests.put(url=update_endpoint, json=new_pixel_config, headers=headers)
print(response1.text) '''

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
'''response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)'''


