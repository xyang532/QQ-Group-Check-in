#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, execjs, os, time
from requests import Session

'只需填入QQ号，QQ密码，签到群号即可'

user = 'xxxxxxxx' # QQ号
pwd = 'xxxxxxxx' # QQ密码
g_list = [1234,] # 签到的QQ群号  可多填，用英文符号','隔开

def main():
    global pwd
    s = Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 QQ/6.5.5.0 TIM/2.2.0.401 V1_IPH_SQ_6.5.5_1_TIM_D Pixel/1080 Core/UIWebView Device/Apple(iPhone 6Plus) NetType/WIFI'})
    
    # 获取参数
    url = 'https://ssl.ptlogin2.qq.com/check'
    params = {
        'regmaster': '',
        'pt_tea': '2',
        'pt_vcode': '1',
        'uin': user,
        'appid': '715030901',
        'js_ver': '10270',
        'js_type': '1',
        'login_sig': 'XrNFVuBrDawRb7wlxYUGMdFFqHc6D2zIBNueAG1BTNsft-rKvtiJVQq7OCqbcVvU',
        'u1': 'https://qun.qq.com/',
        'pt_uistyle': '40',
        'pt_jstoken': '1114830175'
    }
    web = s.get(url, params=params).text
    web = re.findall(r'ptui_checkVC(.*?),\'(.*?)\',\'(.*?)\',\'(.*?)\'', web)[0]
    verifycode = web[1] # 验证码
    pt_verifysession_v1 = web[3] # 验证任务值
    
    # 登陆
    url = 'https://ssl.ptlogin2.qq.com/login'
    salt = eval(repr(web[2]).replace('\\\\', '\\'))
    
    #通过js来计算密码的密文
    jspath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qqlogin.js')
    with open(jspath, 'r') as f:
        content = f.read()
    ctx = execjs.compile(content)
    try:
       pwd = ctx.call('my_getEncPass',pwd , salt, web[1])
    except Exception as e:
       print(e)
    
    params = {
        'u': user,
        'verifycode': verifycode,
        'pt_vcode_v1': '0',
        'pt_verifysession_v1': pt_verifysession_v1,
        'p': pwd,
        'pt_randsalt': '2',
        'pt_jstoken': '1114830175',
        'u1': 'https://qun.qq.com/',
        'ptredirect': '1',
        'h': '1',
        't': '1',
        'g': '1',
        'from_ui': '1',
        'ptlang': '2052',
        'js_ver': '10270',
        'js_type': '1',
        'login_sig': 'XrNFVuBrDawRb7wlxYUGMdFFqHc6D2zIBNueAG1BTNsft-rKvtiJVQq7OCqbcVvU',
        'pt_uistyle': '40',
        'aid': '715030901',
        'daid': '73',
        'has_onekey': '1'
    }
    s.get(url, params=params)
    
    # 签到
    skey = s.cookies['skey']
    bkn = getBKN(skey)
    url = 'https://qun.qq.com/cgi-bin/qiandao/sign/publish'
    for i in range(len(g_list)):
        data = {
            'client': '2',
            'gallery_info': {
                'category_id': '21',
                'page': '0',
                'pic_id': '173'
            },
            'gc': str(g_list[i]),
            'lgt': '0',
            'poi': '',
            'pic_id': '',
            'template_id': '4',
            'bkn': bkn,
            'text': '云签到', #### 签到内容 ####
            'lat': '0',
            'template_data': ''
        }
        web = s.post(url, data=data).text
        print(web)
        time.sleep(5) #### 签到的间隔，单位秒 ####
        
def getBKN(skey):
    length = len(skey)
    hash = 5381
    for i in range(length):
        hash += (hash << 5) + ord(skey[i])
    return hash & 2147483647 # 计算bkn

if __name__ == '__main__':
    main()
