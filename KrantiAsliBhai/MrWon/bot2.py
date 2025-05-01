
from highrise.__main__ import *
import time
from bot import Mybot

room_id = input("67dcc8ab619f9b7b91cb2228")
api_token = input("274659e847fae9bba79e14cabb0ea8623341aebd35b575c5123358eec9c1a132")

my_bot = BotDefinition(Mybot(), room_id, api_token)

PURPLE_COLOR = "\033[95m"
RESET_COLOR = "\033[0m"

while True:
    try:
        definitions = [my_bot]
        try:
            arun(main(definitions))
        except KeyboardInterrupt:
            print(f"{PURPLE_COLOR}Bot is offline{RESET_COLOR}")
            break
    except Exception as e:
        print(f"An exception occurred: {e}")
        time.sleep(5)
