import flask
import json
from flask import request

from shortcuts import get_jike, get_xyz
import flomo
from config import cookies


server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False


@server.route('/memo', methods=['get', 'post'])
def memo():
    #url = request.values.get('url')
    #token = request.values.get('token')

    data = json.loads(request.data.decode('utf-8'))
    url = data['content']
    token = data['token']

    if token != 'shaonannblightnb': 
        return json.dumps({'code':500, 'message':'who are u'})

    if 'xiaoyuzhoufm.com' in url:
        content, response_message = get_xyz(url)
    elif 'okjike.com' in url:
        content, response_message = get_jike(url)
    else:
        content = url
        response_message = url

    content_html = ''.join([f'<p>{c}</p>' for c in content.split('\n')])

    client = flomo.Flomo(cookies)
    response = client.new(content_html)
    response_json = json.loads(response.text)
    # print(response_json['message'])

    if response.status_code == 200:
        if response_json['code'] == 0:
            res = {'code': 200, 'message': response_message}
        else:
            res = {'code': 0, 'message': response_json['message']}
    else:
        res = response_json

    # if username and pwd:
    #     if username == 'xiaoming' and pwd == '111':
    #         resu = {'code': 200, 'message': '登录成功'}
    #         # 将字典转换为json串, json是字符串
    #         return json.dumps(resu, ensure_ascii=False)
    #     else:
    #         resu = {'code': -1, 'message': '账号密码错误'}
    #         return json.dumps(resu, ensure_ascii=False)
    # else:
    #     resu = {'code': 10001, 'message': '参数不能为空！'}
    return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
    server.run(debug=False, port=8888, host='0.0.0.0')
