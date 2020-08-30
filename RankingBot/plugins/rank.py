from plugins import url
from datetime import datetime, timedelta
import slackbot_settings
import requests
from plugins import user
import collections


def get_rank_contribute_one_week():
    now = datetime.today()
    one_week_ago = now - timedelta(days=7)
    payload = {
        url.CONST_TOKEN: slackbot_settings.API_TOKEN,
        url.CONST_CHANNEL: slackbot_settings.CHANNEL,
        url.CONST_LIMIT: 100,
        url.CONST_OLDEST: one_week_ago.strftime('%s'),
        url.CONST_LATEST: now.strftime('%s')
    }
    history = get_history(payload)
    contributors = user.get_contributors()
    # typeがmessageかつ、subtypeがない純粋な投稿のみ抜粋
    messages = list(filter(lambda x: x['type'] == 'message' and 'subtype' not in x, history['messages']))

    # 投稿数が多かった人
    most_post_contributors = filter_most_post_contributor(contributors, messages)
    text_result_most_post_contributors = create_rank_text(most_post_contributors)

    # スタンプ数が多かった人
    most_react_contributors = filter_most_react_contributor(contributors, messages)
    text_result_most_react_contributors = create_rank_text(most_react_contributors)

    # 返信した数が多かった人
    most_reply_contributors = filter_most_reply_contributor(contributors, messages)
    text_result_most_reply_contributors = create_rank_text(most_reply_contributors)

    text_result = ('<!channel>\n'
                   + create_term_text(one_week_ago, now) + '\n'
                   + create_all_counts_text(messages) + '\n'
                   + ':tada: 投稿数ランキング :tada:' + '\n' + text_result_most_post_contributors + '\n'
                   + ':tada: スタンプした人ランキング :tada:' + '\n' + text_result_most_react_contributors + '\n'
                   + ':tada: 返信した人ランキング :tada:' + '\n' + text_result_most_reply_contributors + '\n')
    print(text_result)
    return text_result


def get_history(params: {}):
    result = requests.get(url.URL_HISTORY, params)
    json_data = result.json()
    if not json_data.get('ok', False):
        print('取得に失敗しました: ' + url.URL_HISTORY)
        return -1
    return json_data


# 投稿数が多かった人の抽出
def filter_most_post_contributor(contributors: {}, messages: []):
    user_ids = []
    for message in messages:
        user_ids.append(message['user'])
    users_mapped_display_names = user.map_user_to_display_name(contributors, user_ids)
    return collections.Counter(users_mapped_display_names).most_common()


# スタンプした数が多かった人の抽出
def filter_most_react_contributor(contributors: {}, messages: []):
    user_ids = []
    for message in messages:
        if 'reactions' not in message:
            continue
        for reaction in message['reactions']:
            user_ids.extend(reaction['users'])
    users_mapped_display_names = user.map_user_to_display_name(contributors, user_ids)
    return collections.Counter(users_mapped_display_names).most_common()


# 返信した数が多かった人の抽出
def filter_most_reply_contributor(contributors: {}, messages: []):
    user_ids = []
    for message in messages:
        if 'reply_users' not in message:
            continue
        user_ids.extend(message['reply_users'])
    users_mapped_display_names = user.map_user_to_display_name(contributors, user_ids)
    return collections.Counter(users_mapped_display_names).most_common()


def create_rank_text(result: [tuple]):
    text = ''
    rank = 1
    for contributor, count in result:
        text += (str(rank) + '位 ' + str(contributor) + ' ' + str(count) + '回\n')
        rank += 1
    return text


def create_term_text(start: datetime, end: datetime):
    return '集計期間: ' + start.strftime('%Y/%m/%d') + ' ~ ' + end.strftime('%Y/%m/%d')


def create_all_counts_text(all_list: []):
    return '総投稿数: ' + str(len(all_list))
