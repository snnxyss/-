# import Httpservice
from payload2 import payload


RequestHeader = "GET https://miaomiao.scmttec.com/seckill/seckill/list.do?offset=0&limit=10&regionCode=5101 HTTP/1.1\n" + \
                "Host: miaomiao.scmttec.com\n" + \
                "Connection: keep-alive\n" + \
                "Accept: application/json, text/plain, */*\n" + \
                "Cookie:  {cookie}\n" + \
                "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat\n" \
                "X-Requested-With: XMLHttpRequest\n" + \
                "content-type: application/json\n" + \
                "tk: wxapptoken:10:e0963da6b3e544f48fef5f6f27c32b5f\n" + \
                "Referer: https://servicewechat.com/wxff8cad2e9bf18719/7/page-frame.html\n" + \
                "Accept-Encoding: gzip, deflate, br\n" + "\n"
cookie = ""
regionCode = ''

def config():
    res = payload(RequestHeader.format(cookie=cookie))
    print(res.req)

def check(a_func):
    def wrapTheFunction():
        if cookie == "":
            print("cookie 为空")
        else:
            a_func()

    return wrapTheFunction
