import json
import urllib.parse
import webbrowser

import requests
from bs4 import BeautifulSoup


class apiClient:

    @staticmethod
    def send(host, header, request, endpoint):
        response = requests.post(url=host + endpoint, headers=header, json=request)
        return response.json()

    @staticmethod
    def get(host, request, endpoint):
        # response = requests.post(url=host + endpoint, data=request)
        data = urllib.parse.urlencode(request)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # form = soup.find('form')
        # inputFields = form.find_all('input')
        # data = {}
        # for field in inputFields:
        #     name = field.get('name')
        #     value = field.get('value')
        #     if name:
        #         data[name] = value
        # jsonData = json.dumps(data, indent=4)
        # cleanJson = jsonData.replace('\n', '').replace('\\', '').replace('', '').strip()

        # NON-3DS
        # soup = BeautifulSoup(response.text, 'html.parser')
        # input_fields = soup.find_all('input')
        #
        # data = {}
        # for field in input_fields:
        #     name = field.get('name')
        #     value = field.get('value')
        #     if name:
        #         data[name] = value
        # clean_data = {k.strip(): v.strip() for k, v in data.items()}
        # json_data = json.dumps(clean_data, separators=(',', ':'))
        # json_data = json.dumps(clean_data, separators=(',', ':'), indent=4)
        # endJson = json.loads(json_data)

        # print(response.text)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # form = soup.find('form', attrs={'name': 'mpgsAuthFrm'})
        # action = form.get('action')
        #
        # inputFields = form.find_all('input')
        # data = {}
        # for field in inputFields:
        #     name = field.get('name')
        #     value = field.get('value')
        #     if name:
        #         data[name] = value
        # response = requests.post(url=action, data=data)
        # print(inputFields)

        # Open the URL in a web browser
        # webbrowser.open(action)
        webbrowser.open(f"{host}{endpoint}?{data}")
        # return endJson

    @staticmethod
    def sendUrl(host, request, endpoint):
        response = requests.post(url=host + endpoint, data=request)
        return response.json()
