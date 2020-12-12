from bs4 import BeautifulSoup as bs
import requests
import sys
import flomo
import json
from config import cookies, notify_config


def notify(t, m):
    flomo.notify(t, m, **notify_config)


def get_jike(post_url):
    '''spider for jike'''
    post_url = post_url.split('?')[0]

    response = requests.get(post_url)
    soup = bs(response.text, 'lxml')

    content = ''
    for child in soup.select('.text')[0].contents[0].contents:
        if child.string is None:
            continue
        content += child + '\n'
    content

    circle = soup.select('.content')
    if circle:
        circle = circle[0].select('h3')[0].string
    else:
        circle = ''

    username = soup.select('.title')[1].text.replace(' ', '')

    memo_content = f'#即刻/剪藏/{circle} {post_url}\n#社区/即刻/{username}\n'+content
    # print(memo_content)
    return memo_content, content


def get_xyz(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    title = soup.select('.title')[1].text
    title = title.lstrip('# ').strip(' .')
    podcaster = soup.select('.name')[0].text.strip().replace(' ', '')

    url_clip = url.split('?')[0]
    content = f'''[<strong><u>{title}</u></strong>]({url_clip} ) #podcaster/{podcaster}
    #
    '''
    return content, title


if __name__ == '__main__':
    cmd = sys.argv[1].split(' ')
    url = cmd[0]

    if 'xiaoyuzhoufm.com' in url:
        content, title = get_xyz(url)
    elif 'okjike.com' in url:
        content, jike_content = get_jike(url)

    content_html = ''.join([f'<p>{c}</p>' for c in content.split('\n')])

    if len(cmd) > 1:
        import richxerox
        richxerox.copy(html=content_html)
        # notify("小宇宙👉剪贴板", title)
    else:
        client = flomo.Flomo(cookies=cookies)
        response = client.new(content_html)
        response_json = json.loads(response.text)
        print(response_json['message'])
        # if response.status_code == 200:
        #     if response_json['code'] == 0:
        #         notify("小宇宙👉flomo", title)
        #     else:
        #         print(response_json)
        #         notify("🚨 flomo Error", response_json['message'])
        # else:
        #     print(response_json)
        #     notify("🚨 flomo Failed", response_json['message'])
