import json
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
        response = requests.post(url=host + endpoint, data=request)
        print(request)
        print(response.text)
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
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', attrs={'name': 'mpgsAuthFrm'})
        action = form.get('action')

        # Open the URL in a web browser
        webbrowser.open(action)

        return response
