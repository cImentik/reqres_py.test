import pytest
from wrapper import ReqMixin


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @pytest.mark.skip()
class TestDelete(ReqMixin):
    '''
    Тесты
        успешное удаление item
    '''
    url = 'users'
    a_msg_title = 'Delete '

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus','job': 'leader'},
    ])
    @pytest.mark.parametrize('tid', [-1, 0, 10, 100])
    def test_delete_success(self, req, data, tid):
        '''
        :delete: инстанс requests
        :data: входной набор
        :tid: id для подстановки в url
        '''
        assert self.make_req(
            req.delete, 
            url=self.url+'/'+str(tid), 
            a_msg=self.a_msg_title+' item (204)',
            data=data
        ).status_code == 204

    @pytest.mark.parametrize('data', [
        {'name': 'morpheus','job': 'leader'},
    ])
    def test_delete_success_not_id(self, req, data):
        '''
        Без подстановки id в url

        :delete: инстанс requests
        :data: входной набор
        '''
        assert self.make_req(
            req.delete, 
            url=self.url,
            a_msg=self.a_msg_title+' item (204)',
            data=data
        ).status_code == 204
