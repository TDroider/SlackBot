import sys
import os

API_TOKEN = ''
CHANNEL = ''

if (os.environ['API_TOKEN'] is None or os.environ['API_TOKEN'] == '') or \
        (os.environ['CHANNEL'] is None or os.environ['CHANNEL'] == ''):
    if len(sys.argv) > 2:
        API_TOKEN = sys.argv[1]
        CHANNEL = sys.argv[2]
    else:
        print('第１引数にトークン、第２引数にチャンネルIDを指定してください.\nまたは環境変数にAPI_TOKEN, CHANNELとしてそれぞれ登録してください.')
        exit()
else:
    API_TOKEN = os.environ['API_TOKEN']
    CHANNEL = os.environ['CHANNEL']

# デフォルトのリプライ
DEFAULT_REPLY = 'わけがわからないよ'

PLUGINS = ['plugins']
