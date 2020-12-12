import sys
import requests
import json
import re
import os

from datetime import datetime

from config import cookies, notify_config, template as tc
import flomo

folder_path = os.path.dirname(os.path.abspath(__file__))


client = flomo.Flomo(cookies=cookies)


def notify(t, m):
    flomo.notify(t, m, **notify_config)


if sys.argv[1] == 'new':
    content = sys.argv[2]
    if content == 't':
        # template
        from datetime import datetime
        today = datetime.now().strftime(tc['time_format'])

        with open(os.path.join(folder_path, tc['path']), 'r') as f:
            content = f.read()
        response = client.new(content.format(today))
        if response.status_code == 200:
            notify("flomo: memo template", today)
        else:
            notify("🚨 flomo Error", response)
    else:
        response = client.new(
            ''.join([f'<p>{c}</p>' for c in content.split('\n')]))
        if response.status_code == 200:
            notify("flomo: new memo", content)
        else:
            notify("🚨 flomo Error", response)
