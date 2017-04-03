import pytest
from wrapper import ReqMixin


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestConnect(ReqMixin):
    '''
        Хост reqres.in/api/ отдаёт 404
        https://reqres.in/api/anywords 200 в случае успеха
    '''
    url = '!'
    a_msg_title = 'Check connect'
    
    def test_check_connect(self, req):
        r = self.make_req(req.get, url=self.url, 
            a_msg=self.a_msg_title)
        assert r.status_code == 200