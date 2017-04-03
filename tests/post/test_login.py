import pytest
from .post_wrap import WrapPost


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @pytest.mark.skip()
class TestLogin(WrapPost):
    '''
    Тесты
        Login - successful
        Login - unsuccessful
    '''
    url = 'login'
    a_msg_title = 'Login'