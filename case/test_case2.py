import unittest
from PublicMethod import GetDemo
import json


#事件配置
class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    # @unittest.skip('调试跳过')
    def test_01(self):
        '''新增父级事件配置'''
        uri='http://192.168.211.17:12811/eventType/addeventtype'

        data={
                "eventName": "1",
                "showName": "",
                "content": "",
                "startTime": "1",
                "endTime": "5",
                "imageSrc": "/static/upload/images/eventType/eventImage/1594014909543.png",
                "eventColor": "#1e8bde",
                "soundSrc": "/static/upload/images/eventType/sound/1594014912679.png",
                "pid": "00000000-0000-0000-0000-000000000000"
        }
        heares={
            'Authorization':'Bearer '+ GetDemo.RunMain().send_token(),
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.res=GetDemo.RunMain().run_main('POST',url=uri,data=json.dumps(data),headers=heares)
        print(self.res)
        self.assertEqual(self.res['code'],0,'状态码错误应该为：0')
        self.assertEqual(self.res['msg'],'请求成功','提示消息不正确应该为：请求成功')
    def test_02(self):
        '''修改父级事件配置'''
        uri = 'http://192.168.211.17:12811/eventType/updateeventtype'
        data={
              "id":"46eafa21-c1d3-4754-bf5a-ac75fdfcc87e",
              "pid":"00000000-0000-0000-0000-000000000000",
              "eventName":"2121",
              "showName":"",
              "content":"",
              "startTime":"1",
              "endTime":"5",
              "imageSrc":"/static/upload/images/eventType/eventImage/1630911228070.png",
              "eventColor":"#1e8bde",
              "soundSrc":"/static/upload/images/eventType/sound/1594014912679.png"
              }
        heares = {
            'Authorization': 'Bearer ' + GetDemo.RunMain().send_token(),
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.res=GetDemo.RunMain().send_post(url=uri,data=json.dumps(data),headers=heares)
        print(self.res)
    def test_03(self):
        pass
if __name__ == '__main__':
    unittest.main(verbosity=2)