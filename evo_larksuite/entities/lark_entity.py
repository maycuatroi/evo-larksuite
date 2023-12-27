import json

import requests

from evo_larksuite.entities.acess_token import GatAccessToken


class LarkEntity:
    table_id = ""  # this is a class variable

    def __init__(self):
        self.__access_token = GatAccessToken()

    @property
    def access_token(self):
        return self.__access_token.access_token

    def send_api(self, url, data=None, method="GET"):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }
        data = {} or data
        if method == "GET":
            res = requests.get(url, headers=headers, params=data)
        elif method == "POST":
            res = requests.post(url, headers=headers, json=data)
        token_res = json.loads(res.text)
        code = token_res.get("code")
        assert code == 0, token_res
        return token_res
