class ReqMixin():
    '''
    Формирует request целиком, отдаёт в req_fixtures и возвращает результат
    '''
    url = ''
    a_msg_title = ''

    def make_req(self, req_instans, **kwargv):
        '''
        :req_instans: инстанс requests
        :return: requests.response
        '''
        return req_instans(kwargv['url'], a_msg = kwargv['a_msg'], 
            params=kwargv.get('params', None), data=kwargv.get('data', None))
