pytest_plugins = ['req_fixtures']

def pytest_addoption(parser):
    parser.addoption('--testing-stand', action='store',
                     default=False,
                     help="Stand on which to run tests")

def pytest_report_header(config):
    '''
        Добавить в заголовок содержимое параметра --testing-stand
        если оно есть
    '''
    if config.getoption("--testing-stand"):
        print('Testing stand: '+config.getoption("--testing-stand"))