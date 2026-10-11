import requests


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url

    # метод для отправки post запроса
    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    # метод для отправки get запроса
    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    # метод для отправки put запроса
    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response




