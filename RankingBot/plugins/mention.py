from slackbot.bot import listen_to
from plugins import rank


# 1週間のうち、貢献した人のランキングを返す
@listen_to('rank 1w cont')
def contributeRank(message):
    rank.get_rank_contribute_one_week()
    message.send_webapi(rank.get_rank_contribute_one_week())
