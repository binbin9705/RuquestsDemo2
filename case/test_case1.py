import unittest
import time
import json
from PublicMethod import GetDemo
#行业接口
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # @unittest.skip('跳过')
    def test_01(self):
        '''分页查询行业信息 默认1页、每页10行'''
        url='http://192.168.211.17:12811/industry/getindustryPage'
        headers = {
            'Authorization': 'Bearer ' + GetDemo.RunMain().send_token()
        }
        #请求接口
        self.res= GetDemo.RunMain().run_main('GET',url=url,headers=headers)
        # 判断返回的状态码及请求信息
        self.assertEqual(self.res['code'],0,'返回状态不正确，应该为0')
        self.assertEqual(self.res['msg'],'请求成功','msg消息不对')
    # @unittest.skip('跳过')
    def test_02(self):
        '''新增行业 行业名称为1行业编码为1'''
        url='http://192.168.211.17:12811/industry/addindustry'
        headers = {
            'Authorization': 'Bearer '+ GetDemo.RunMain().send_token(),
            'Content-Type':'application/json;charset=UTF-8'
        }
        data={
            'industryName':'2',
            'industryCode':'1'
        }
        self.res=GetDemo.RunMain().run_main('POST',url=url,data=json.dumps(data),headers=headers)
        # print(self.res)
        self.assertEqual(self.res['code'],0,'返回状态不正确，应该为0')
    # @unittest.skip('跳过')
    def test_03(self,industryName=None):
        '''查询行业信息'''
        url = 'http://192.168.211.17:12811/industry/getindustry'
        headers = {
            'Authorization': 'Bearer ' + GetDemo.RunMain().send_token()
        }
        self.res = GetDemo.RunMain().run_main('POST', url=url, headers=headers)
        #{}下的value名[]下几位 res['data']循环遍历整个data列表
        # print(self.res['data'])
        for x in self.res['data']:
            #判断行业名称为1行业的打印出id
            if x['industryName']==industryName:
                id=x['id']
                return id
            else:
                pass
        self.assertEqual(self.res['code'], 0, '返回状态不正确，应该为0')
        self.assertEqual(self.res['msg'], '请求成功', 'msg消息不对')
    def test_04(self):
        '''修改行业配置'''
        url = 'http://192.168.211.17:12811/industry/updateindustry'
        data = {
            'id': Test1().test_03('2'),
            "industryName": "20332",
            "industryCode": "1",
            "content": ""
        }
        headers = {
            'Authorization': 'Bearer ' + GetDemo.RunMain().send_token(),
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.res = GetDemo.RunMain().run_main('POST', url=url, data=json.dumps(data), headers=headers)
        # print(self.res)
        self.assertEqual(self.res['code'], 0, '返回状态不正确，应该为0')
    # @unittest.skip('跳过')
    def test_05(self):
        '''根据id删除行业信息'''
        url = 'http://192.168.211.17:12811/industry/deleteindustry'
        data={
            #创建行业名=1的行业id
            'id':Test1().test_03('20332')
        }
        headers = {
            'Authorization': 'Bearer ' + GetDemo.RunMain().send_token()
        }
        # print(data)
        self.res = GetDemo.RunMain().run_main('POST', url=url,data=data,headers=headers)
        # print(self.res)
        self.assertEqual(self.res['code'], 0, '返回状态不正确，应该为0')
        self.assertEqual(self.res['msg'], '请求成功', 'msg消息不对')
if __name__ == '__main__':
    unittest.main(verbosity=2)
