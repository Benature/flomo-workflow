import flomo
import re
from config import cookies

client = flomo.Flomo(cookies=cookies)


old_tag, new_tag = ['#我喜欢', '#生命中的盐']  # [::-1]


response = client.get(tag=old_tag)
memos = response['memos']


for memo in memos:
    content = memo['content']
    out = re.sub(f'({old_tag})[ <]', lambda m: m.group().replace(old_tag, new_tag),
                 content)
    response = client.update(memo['slug'], out)
    print(response, out)
