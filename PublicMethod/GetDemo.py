import requests
import unittest
import time
import json
# headers={
            # 'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZGxheF9yZXNvdXJjZXMiXSwiZXhwIjozN
# zUzMzQzNjY3LCJ1c2VyX25hbWUiOiJ7XCJpc1N1cGVyXCI6MSxcInBlcnNvbklkXCI6XCI5MGM2OTU0MC0yOGI5LTRmMjEtYWE0Yy04OTFlODIwMTFkYzh
# cIn0iLCJqdGkiOiI3ZDZmMTBhZS05YzBmLTRiMmUtODc3My1mMzVkYzEwY2ZmZWEiLCJjbGllbnRfaWQiOiJkbGF4ZDFmYWZkYWFlMThkNGY2Iiwic2NvcG
# UiOlsiZGxheGQxZmFmZGFhZTE4ZDRmNiJdfQ.yl0ZwNbKG19G7rioWLcTmzS-NH1lRhk5Gu6tg_z6JRI'
        # }
class RunMain:
    def send_get(self,url,data,headers):
        res = requests.get(url=url, params=data,headers=headers).json()
        return res
        # return json.dumps(res,indent=2,sort_keys=True)
    def send_post(self,url,data,headers):
        res=requests.post(url=url,data=data,headers=headers).json()
        return res
        # return json.dumps(res,indent=2,sort_keys=True)
    def send_token(self):
        url='http://192.168.211.17:12811/dsrp/token'
        data={
            'grant_type':'password',
            'client_id':'dlaxdb562cd62763430',
            'client_secret':'d8ea0d0fbe1d411090423b4fe01baaf9',
            'username':'dladmin',
            'password':'simp@2017'
        }
        header={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
                }
        res=requests.post(url=url,data=data,headers=header).json()
        # print(res)
        token=res['data']['accessToken']
        return token
    def run_main(self,method,url,data=None,headers=None):
        res=None
        if method=='GET':
            res=self.send_get(url,data,headers)
            return res
        elif method=='POST':
            res=self.send_post(url,data,headers)
            return  res
if __name__ == '__main__':
    print(RunMain().send_token())