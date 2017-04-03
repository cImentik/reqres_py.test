import pytest
from wrapper import ReqMixin


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @pytest.mark.skip()
class TestUpdate(ReqMixin):
    '''
    Тесты
        успешное обнавлени item
    '''
    url = 'users'
    a_msg_title = 'Put '

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus','job': 'leader'},
    ])
    @pytest.mark.parametrize('tid', [-1, 0, 10, 100])
    def test_update_success(self, req, data, tid):
        '''
        :put: инстанс requests
        :data: входной набор
        :tid: id для подстановки в url
        '''
        r = self.make_req(
            req.put, 
            url=self.url+'/'+str(tid), 
            a_msg=self.a_msg_title+' item (200)',
            data=data
        )
        assert r.status_code == 200
        assert r.json()['name'] == data['name'] and 'updatedAt' in r.json()

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus','job': 'leader'},
    ])
    def test_update_success_not_id(self, req, data):
        '''
        Без подстановки id в url
        :put: инстанс requests
        :data: входной набор
        '''
        r = self.make_req(
            req.put, 
            url=self.url,
            a_msg=self.a_msg_title+' item (200)',
            data=data
        )
        assert r.status_code == 200
        assert r.json()['name'] == data['name'] and 'updatedAt' in r.json()
