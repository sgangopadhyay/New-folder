
import requests

class Guvi:
   def __init__(self, web_url):
       self.url = web_url
   
   def fetch_data(self):
       response = requests.get()
       return response.json()   
   
   def fetch_name(self):
       for data in self.fetch_data():
           print(data['name'])


   # fetch data based on ID
   def based_on_id(self, id):
       id = str(id)
       for data in self.fetch_data():
           if data['id'] == id:
               print(data['id'])
               print(data['name'])
               print(data['location'])
               print(data['country'])




url = "https://6412feab3b710647375bdc8d.mockapi.io/suman_api_testing"


s = Suman(url)


print(s.fetch_data())
