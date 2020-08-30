import requests
import slackbot_settings
from plugins import url


# チャンネル参加メンバーのユーザーIDとユーザー名をペアにして返す
def get_contributors():
    members = get_members()
    contributors = {}
    for user_id in members:
        user_info = get_user_info(user_id)
        if not user_info['ok']:
            print('error userId [{0}]'.format(user_id))
            continue
        if user_info['user']['is_bot']:
            # botは省く
            continue
        else:
            display_name = user_info['user']['profile']['display_name']
            if display_name != '':
                contributors[user_id] = display_name
            else:
                contributors[user_id] = user_info['user']['name']
    return contributors


# チャンネルに参加しているメンバー一覧の取得
def get_members():
    params = {
        url.CONST_TOKEN: slackbot_settings.API_TOKEN,
        url.CONST_CHANNEL: slackbot_settings.CHANNEL
    }
    result = requests.get(url.URL_MEMBERS, params)
    json_data = result.json()
    if not json_data.get('ok', False):
        print('取得に失敗しました: ' + url.URL_MEMBERS)
        return -1
    return json_data['members']


# user_idをもとに、userの詳細を取得する.
# 表示用ユーザー名のマッピングのために必要
def get_user_info(user_id):
    params = {
        url.CONST_TOKEN: slackbot_settings.API_TOKEN,
        'user': user_id
    }
    result = requests.get(url.URL_USER_INFO, params)
    json_data = result.json()
    if not json_data.get('ok', False):
        print('取得に失敗しました: ' + url.URL_USER_INFO)
        return -1
    return json_data


def map_user_to_display_name(all_contributors: {}, user_ids: []):
    display_name = []
    for user_id in user_ids:
        if user_id not in all_contributors:
            continue
        display_name.append(all_contributors[user_id])
    return display_name
