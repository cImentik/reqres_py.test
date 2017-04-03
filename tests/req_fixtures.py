import pytest
import requests
from requests_toolbelt.utils import dump


class BaseRequest():

    base_url = 'https://reqres.in/api/'

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain',
        'User-Agent': 'Mozilla/5.0'
    }

    timeout = 5

    def get_response(self, method_name, url, **kwargv):
        response = requests.request(
            method=method_name,
            url=url, 
            headers=self.headers, 
            params=kwargv.get('params', None), 
            json=kwargv.get('data', None),
            timeout=self.timeout
        )
        if 'a_msg' in kwargv:
            pytest.allure.attach(kwargv['a_msg'], 
                dump.dump_all(response).decode('utf-8'))
        return response

    def get(self, url='', **kwargv):
        return self.get_response(method_name='GET', 
            url=self.base_url+url, **kwargv)

    def post(self, url='', **kwargv):
        return self.get_response(method_name='POST', 
            url=self.base_url+url, **kwargv)

    def put(self, url='', **kwargv):
        return self.get_response(method_name='PUT', 
            url=self.base_url+url, **kwargv)

    def patch(self, url='', **kwargv):
        return self.get_response(method_name='PATCH', 
            url=self.base_url+url, **kwargv)

    def delete(self, url='', **kwargv):
        return self.get_response(method_name='DELETE', 
            url=self.base_url+url, **kwargv)

@pytest.fixture()
def req():
    return BaseRequest()