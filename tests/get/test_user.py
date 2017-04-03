import pytest
from .get_wrap import SingleGet, ListGet


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
# @pytest.mark.skip()
class TestSingleUser(SingleGet):
    '''
    Тесты
        Single user
    '''
    url = 'users/'
    a_msg_title = 'Single user'


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
# @pytest.mark.skip()
class TestListUser(ListGet):
    '''
    Тесты
        List user
    '''
    url = 'users'
    a_msg_title = 'List users'
