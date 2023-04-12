
### ЗАДАНИЕ 1 
#### Супергерои
import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)

names_dict = {}

# сортируем, оставляя только имена и ум
for persons in response.json(): 
    name = persons['name'] 
    names_dict[name] = persons["powerstats"]["intelligence"]
# составляем список нужный участников
sort_list = ['Hulk', 'Captain America', 'Thanos']
# сортируем по нужным участникам
names_dict = {key: names_dict[key] for key in names_dict if key in sort_list}
# выявляем самого сильного
most_strong = (max(names_dict, key=names_dict.get))

print(f'Самый умный супергерой: {most_strong}')  

### ЗАДАНИЕ 2
#### Запрос в Яндекс

import requests
from pprint import pprint

TOKEN = "____________________"

class YandexDisk:

    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    data = ya.get_files_list()
    pprint(data)
    
    #### Запрос в Яндекс и отправка файла

    import requests
from requests import get, post, put, delete
from pprint import pprint

token = "____________________"

headers = {"Authorization": token}
r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
pprint(r.json())
# создадим папку на Яндекс Диске
params = {"path": "TEST NETOLOGY"}
r = put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
# print(r)
# делаем запрос на место записи Диска
params = {"path": "TEST NETOLOGY/file.txt"}
r = get("https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=headers, params=params)
href = r.json()["href"]
# открываем файл и делаем запрос PUT на размещение файла
files = {"file": open("file.txt", "r")}
r = put(href, files=files)
print(r)