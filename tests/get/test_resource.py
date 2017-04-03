import pytest
from .get_wrap import SingleGet, ListGet


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
# @pytest.mark.skip()
class TestSingleResource(SingleGet):
    '''
    Тесты
        Single resource
    '''
    url = 'resource/'
    a_msg_title = 'Single resource'


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
# @pytest.mark.skip()
class TestListResource(ListGet):
    '''
    Тесты
        List resource
    '''
    url = 'resource'
    a_msg_title = 'List resource'
    