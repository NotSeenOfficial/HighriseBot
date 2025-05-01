from highrise.__main__ import *
import time

bot_file_name = "bot"
bot_class_name = "Mybot"
room_id = "6800ad6f8f5b81d963124c31"
bot_token = "3f060e31d63726e31c0a49d8800031eae0a262d35cdd6e13b200a7422b12551e"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

# ANSI escape code for purple text (magenta)
PURPLE_COLOR = "\033[95m"
RESET_COLOR = "\033[0m"

while True:
    try:
        definitions = [my_bot]
        # Wrap this in a try-except block for KeyboardInterrupt
        try:
            arun(main(definitions))
        except KeyboardInterrupt:
            print(f"{PURPLE_COLOR}Bot is offline{RESET_COLOR}")  # Message in purple when Ctrl + C is pressed
            break  # Exit the while loop
    except Exception as e:
        print(f"An exception occurred: {e}")
        time.sleep(5)
