import pytest
from .post_wrap import WrapPost


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @pytest.mark.skip()
class TestRegister(WrapPost):
    '''
    Тесты 
        Register - successful
        Register - unsuccessfulы
    '''
    url = 'register'
    a_msg_title = 'Register'
