import json
from datetime import datetime, timedelta

import requests

from evo_larksuite.config import LARK_BASE_URL, LARK_APP_ID, LARK_APP_SECRET


class GatAccessToken:
    def __init__(self):
        self.__access_token_data: dict = None
        print(self.access_token_data)

    @property
    def access_token(self):
        return self.access_token_data.get("tenant_access_token")

    def is_expired(self):
        return self.expire_at < datetime.now()

    def __load_access_token(self):
        """
        Get all access token
        """
        url = LARK_BASE_URL + "auth/v3/tenant_access_token/internal/"
        headers = {"Content-Type": "application/json"}
        param = {"app_id": LARK_APP_ID, "app_secret": LARK_APP_SECRET}
        token_res = json.loads(requests.post(url, param, headers).text)
        code = token_res.get("code")
        assert code == 0, token_res
        self.__access_token_data = token_res
        expire = token_res.get("expire")
        self.expire_at = datetime.now() + timedelta(seconds=expire)
        return token_res

    @property
    def access_token_data(self):
        is_none = self.__access_token_data is None
        if is_none:
            return self.__load_access_token()
        is_expired = self.is_expired()
        if is_expired:
            return self.__load_access_token()
        return self.__access_token_data
