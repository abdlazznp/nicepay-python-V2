import requests


class apiClient:

    @staticmethod
    def send(host, header, request, endpoint):
        response = requests.post(url=host + endpoint, headers=header, json=request)
        return response.json()

    @staticmethod
    def get(host, request, endpoint):
        response = requests.get(url=host + endpoint + request)
        return response.json()