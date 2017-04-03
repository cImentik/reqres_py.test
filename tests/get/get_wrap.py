import pytest
from wrapper import ReqMixin


class SingleGet(ReqMixin):
    '''
        Mixin для тестов Single User, Resource
    '''
    @pytest.mark.parametrize('tid', [-1, 0, 100])
    def test_not_found_for_digit(self, req, tid):
        '''
            :get: инстанс requests
            :tid: id для подстановки в url
        '''
        r = self.make_req(req.get, url=self.url+str(tid), 
            a_msg=self.a_msg_title+' not found (404)')
        assert r.status_code == 404

    @pytest.mark.parametrize('tid', ['foo', 'bar'])
    def test_not_found_for_string(self, req, tid):
        r = self.make_req(req.get, url=self.url+str(tid), 
            a_msg=self.a_msg_title+' not found (404)')
        assert r.status_code == 404

    @pytest.mark.parametrize('tid', [1,12])
    def test_found(self, req, tid):
        r = self.make_req(req.get, url=self.url+str(tid), 
            a_msg=self.a_msg_title+' found (200)')
        assert r.status_code == 200
        assert r.json()['data']['id'] == tid


class ListGet(ReqMixin):
    '''
        Mixin для тестов List User, Resource
    '''
    @pytest.mark.parametrize('page', [-1,0,2,4])
    def test_list_found_page_for_digit(self, req, page):
        '''
            :get: инстанс requests
            :page: page для подстановки в url
        '''
        r = self.make_req(
            req.get, 
            url=self.url,
            params={'page': page},
            a_msg=self.a_msg_title+' found (200)'
        )
        assert r.status_code == 200
        assert int(r.json()['page']) == page 

    @pytest.mark.parametrize('page', ['foo','bar'])
    def test_list_found_page_for_string(self, req, page):
        r = self.make_req(
            req.get, 
            url=self.url,
            params={'page': page},
            a_msg=self.a_msg_title+' found (200)'
        )
        assert r.status_code == 200
        assert r.json()['page'] == page 

    def test_list_found_page_not_param(self, req):
        r = self.make_req(
            req.get, 
            url=self.url,
            a_msg=self.a_msg_title+' found (200)'
        )
        assert r.status_code == 200
        assert int(r.json()['page']) == 1 

    @pytest.mark.parametrize('page', [10,10000])
    def test_list_not_found_data(self, req, page):
        r = self.make_req(
            req.get, 
            url=self.url,
            params={'page': page},
            a_msg=self.a_msg_title+' found (200) and not data'
        )
        assert r.status_code == 200
        assert not len(r.json()['data'])