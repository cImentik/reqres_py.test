import pytest
from wrapper import ReqMixin


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @pytest.mark.skip()
class TestCreate(ReqMixin):
    '''
    Тесты
        успешное создание пользователя
    '''
    url = 'users'
    a_msg_title = 'Create '

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus','job': 'leader'},
        {'name': '','job': ''},
    ])
    def test_create_success(self, req, data):
        '''
        :post: инстанс request
        :data: входной набор
        '''
        r = self.make_req(
            req.post, 
            url=self.url, 
            a_msg=self.a_msg_title+' user (201)',
            data=data
        )
        assert r.status_code == 201
        assert int(r.json()['id']) > 0 and r.json()['name'] == data['name']
