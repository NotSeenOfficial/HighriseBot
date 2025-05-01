import asyncio
from pathlib import Path
from typing import Literal
from highrise import BaseBot, Position, User, AnchorPosition, SessionMetadata, CurrencyItem, Item, GetMessagesRequest
from functions.dancefloor import DanceFloor
from functions.goandbring import GoAndBringCommands
from functions.userinfo import UserInfo
from functions.loop_emote import LoopEmote
from functions.follow import FollowCommands
from functions.emotebot import DanceBotCommands
from functions.joke_rizz_poetry_flirt import JokeRizzPoetryFlirt
from functions.ipl import IPLScore
import logging
import json
import os
from datausers import *
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from owner import OWNER_USER

class Mybot2(BaseBot):

    @staticmethod
    def load_UserEmote_ids(file_path="UserEmotes.json"):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_UserEmote_ids(UserEmote_ids, file_path="UserEmotes.json"):
        with open(file_path, "w") as f:
            json.dump(UserEmote_ids, f)

    
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            bot_id = "66ffb1a3989b8812d98e2b11"
            await self.highrise.teleport(bot_id, Position(x=1, y=0.0, z=8, facing='FrontLeft'))
            GREEN_COLOR = "\033[32m"
            RESET_COLOR = "\033[0m"
            print(f"{GREEN_COLOR}Bot is online{RESET_COLOR}")

            asyncio.create_task(self.send_welcome_messages())
            await self.DanceFloor.send_continuous_random_emotes_in_dance_floor()

        except Exception as e:
            logging.error(f"An error occurred in on_start: {e}")
        await self.DanceFloor.send_continuous_random_emotes_in_dance_floor()


    def __init__(self):
        super().__init__()
        self.DanceFloor = DanceFloor(self)
        self.go_and_bring = GoAndBringCommands(self)
        self.userinfo = UserInfo(self)
        self.loop_emote = LoopEmote(self)
        self.follow_commands = FollowCommands(self)
        self.dance_bot_commands = DanceBotCommands(self)
        self.joke_rizz_poetry_flirt = JokeRizzPoetryFlirt(self)
        self.react_task = None
        self.position_bounds = self.DanceFloor.position_bounds
        self.emote_duration_mapping = self.DanceFloor.emote_duration_mapping

# z -> 6 - 9.5 
# x -> 3 - 11
# y = 1.1