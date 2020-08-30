import sys
import logging
from slackbot.bot import Bot

# システムパスの設定
sys.path.insert(0, ".")

# logging設定
logging.getLogger().setLevel(logging.INFO)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print('start RankingSlackBot')
    main()
