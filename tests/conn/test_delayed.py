import pytest
from requests import exceptions
from wrapper import ReqMixin


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestDelayed(ReqMixin):
    '''
        Тесты delayed response
    '''
    url = 'users'
    a_msg_title = 'Delayed'

    @pytest.mark.parametrize('params', [
        {'delay': -1},
        {'delay': 0},
        {'delay': 3},
    ])
    def test_delayed(self, req, params):
        '''
        :get: инстанс requests
        :delay: delay для подстановки в url
        '''
        r = self.make_req(req.get, url=self.url, 
            a_msg=self.a_msg_title, params=params)
        assert r.status_code == 200
        assert len(r.json()['data']) > 0

    @pytest.mark.parametrize('params', [
        {'delay': 10},
    ])
    def test_delayed_fail_readtimeout(self, req, params):
        '''
            Параметр delay будет 6с и должно быть исключение
            ReadTimeout от requests, timeout 5c
            :get: инстанс requests
            :delay: delay для подстановки в url
        '''
        with pytest.raises(exceptions.ReadTimeout, 
            message="Expecting ReadTimeout"):
            r = self.make_req(req.get, url=self.url, 
                a_msg=self.a_msg_title, params=params)