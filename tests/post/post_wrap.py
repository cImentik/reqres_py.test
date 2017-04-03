import pytest
from wrapper import ReqMixin

class WrapPost(ReqMixin):
    '''
    Обёртка для тестов 
        Register - successful
        Register - unsuccessful
        Login - successful
        Login - unsuccessful
    '''

    @pytest.mark.parametrize('data', [
        {'email': 'peter@klaven','password': 'cityslicka'},
        {'email': 1,"password": 2}
    ])
    def test_success(self, req, data):
        '''
        Символьные и цифровые логины и пароли
        :post: инстанс request
        :data: входной набор
        '''
        r = self.make_req(
            req.post, 
            url=self.url, 
            a_msg=self.a_msg_title+' success (200,201)',
            data=data
        )
        assert r.status_code in (200,201)
        assert 'token' in r.json()

    @pytest.mark.parametrize('data,error', [
        ({'email': 'peter@klaven'},'Missing password'),
        ({'email': None,'password': None}, 'Missing email or username'),
        ({'password': 'pistol'},'Missing email or username'),
    ])
    def test_unsuccess(self, req, data, error):
        '''
        Попытки с неполными или пуcтыми парами логин/пароль
        :post: инстанс request
        :data: входной набор
        :error: ожидаемый ответ для каждого нового набора
        '''
        r = self.make_req(
            req.post, 
            url=self.url, 
            a_msg=self.a_msg_title+' unsuccess (400)',
            data=data
        )
        assert r.status_code == 400
        assert 'error' in r.json() and r.json()['error'] == error