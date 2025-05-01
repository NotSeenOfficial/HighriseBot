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

#"modd"

LEVEL_UP_MESSAGE_THRESHOLD = 10 
LEVEL_UP_STEP = 50 

#"all" "tip" "vip" "tele"

EMOTES_LIST = [
    "jetpack 0", "fairyfloat 1", "fairytwirl 2", "smooch 3", "launch 4", "float 5", "lust 6", "creepypuppet 7", "repose 8",
    "enthused 9", "anime 10", "gravity 11", "toilet 12", "astro 13", "flex 14", "timejump 15", "penguin 16", "kawaii 17",
    "jinglebell 18", "skating 19", "teleporting 20", "energyball 21", "pushit 22", "boxer 23", "creepycute 24",
    "headblow 25", "wrong 26", "weirdd 27", "uwu 28", "snake 29", "singing 30", "model 31", "maniac 32", "snow 33",
    "ride 34", "icecream 35", "surprise 36", "touch 37", "swordfight 38", "airguitar 39", "zombie 40", "fashion 41",
    "curtsy 42", "cutee 43", "telek 44", "russian 45", "blackpink 46", "shopping 47", "tiktok6 48", "tiktok5 49",
    "tiktok4 50", "tiktok3 51", "tiktok2 52", "tiktok1 53", "hott 54", "charge 55", "greedy 56", "confused 57",
    "punkguitar 58", "shy 59", "wildd 60", "nervous 61", "hyped 62", "fishing 63", "frog 64",
    "siu 65", "snowballfight 66", "bow 67", "thewave 68", "tiredd 69", "pennywise 70", "superpose 71",  
    "pose8 72", "laugh 73", "kiss 74", "hellos 75", "gift 76", "pose10 77", "thumbsup 78", "cursing 79",
    "celebrate 80", "macarena 81", "sitt 82", "gag 83", "superpose 84", "pose7 85", "deny 86", "casual 87",   
    "pose1 88", "pose3 89", "pose5 90", "cutey 91", "thatsright 92", "pose9 93", "angryy 94", "miningmine 95",   
    "miningsuccess 96", "fishingpull 97", "fishingpullsmall 98", "fishingcast 99" ###
]

emote_commands = [
    (0, 'jetpack', 'hcc-jetpack'),
    (1, 'fairyfloat', 'idle-floating'),
    (2, 'fairytwirl', 'emote-looping'),
    (3, 'smooch', 'emote-kissing-bound'),
    (4, 'launch', 'emote-launch'),
    (5, 'float', 'emote-float'),
    (6, 'lust', 'emote-lust'),
    (7, 'creepypuppet', 'dance-creepypuppet'),
    (8, 'repose', 'sit-relaxed'),
    (9, 'enthused', 'idle-enthusiastic'),
    (10, 'anime', 'dance-anime'),
    (11, 'gravity', 'emote-gravity'),
    (12, 'toilet', 'idle-toilet'),
    (13, 'astro', 'emote-astronaut'),
    (14, 'flex', 'emoji-flex'),
    (15, 'timejump', 'emote-timejump'),
    (16, 'penguin', 'dance-pinguin'),
    (17, 'kawaii', 'dance-kawai'),
    (18, 'jinglebell', 'dance-jinglebell'),
    (19, 'skating', 'emote-iceskating'),
    (20, 'teleporting', 'emote-teleporting'),
    (21, 'energyball', 'emote-energyball'),
    (22, 'pushit', 'dance-employee'),
    (23, 'boxer', 'emote-boxer'),
    (24, 'creepycute', 'emote-creepycute'),
    (25, 'headblow', 'emote-headblowup'),
    (26, 'wrong', 'dance-wrong'),
    (27, 'weirdd', 'dance-weird'),
    (28, 'uwu', 'idle-uwu'),
    (29, 'snake', 'emote-snake'),
    (30, 'singing', 'idle_singing'),
    (31, 'model', 'emote-model'),
    (32, 'maniac', 'emote-maniac'),
    (33, 'snow', 'emote-snowangel'),
    (34, 'ride', 'emote-sleigh'),
    (35, 'icecream', 'dance-icecream'),
    (36, 'surprise', 'emote-pose6'),
    (37, 'touch', 'dance-touch'),
    (38, 'swordfight', 'emote-swordfight'),
    (39, 'airguitar', 'idle-guitar'),
    (40, 'zombie', 'emote-zombierun'),
    (41, 'fashion', 'emote-fashionista'),
    (42, 'curtsy', 'emote-curtsy'),
    (43, 'cutee', 'emote-cute'),
    (44, 'telek', 'emote-telekinesis'),
    (45, 'russian', 'dance-russian'),
    (46, 'blackpink', 'dance-blackpink'),
    (47, 'shopping', 'dance-shoppingcart'),
    (48, 'tiktok6', 'dance-tiktok11'),
    (49, 'tiktok5', 'dance-tiktok9'),
    (50, 'tiktok4', 'dance-tiktok8'),
    (51, 'tiktok3', 'idle-dance-tiktok4'),
    (52, 'tiktok2', 'dance-tiktok2'),
    (53, 'tiktok1', 'dance-tiktok10'),
    (54, 'hott', 'emote-hot'),
    (55, 'charge', 'emote-charging'),
    (56, 'greedy', 'emote-greedy'),
    (57, 'confused', 'emote-confused'),
    (58, 'punkguitar', 'emote-punkguitar'),
    (59, 'shy', 'emote-shy2'),
    (60, 'wildd', 'idle-wild'),
    (61, 'nervous', 'idle-nervous'),
    (62, 'hyped', 'emote-hyped'),
    (63, 'fishing', 'fishing-idle'),
    (64, 'frog', 'emote-frog'),
    (65, 'siu', 'emote-celebrationstep'),
    (66, 'snowballfight', 'emote-snowball'),
    (67, 'bow', 'emote-bow'),
    (68, 'thewave', 'emote-wave'),
    (69, 'tiredd', 'emote-tired'),
    (70, 'pennywise', 'dance-pennywise'),
    (71, 'superpose', 'emote-superpose'),  
    (72, 'pose8', 'emote-pose8'),
    (73, 'laugh', 'emote-laughing'),
    (74, 'kiss', 'emote-kiss'),
    (75, 'hellos', 'emote-hello'),
    (76, 'gift', 'emote-gift'),
    (77, 'pose10', 'emote-pose10'),
    (78, 'thumbsup', 'emoji-thumbsup'),
    (79, 'cursing', 'emoji-cursing'),
    (80, 'celebrate', 'emoji-celebrate'),
    (81, 'macarena', 'dance-macarena'),
    (82, 'sitt', 'idle-loop-sitfloor'),
    (83, 'gag', 'emoji-gagging'),          
    (84, 'superpose', 'emote-superpose'),
    (85, 'pose7', 'emote-pose7'),
    (86, 'deny', 'emote-no'),
    (87, 'casual', 'idle-dance-casual'),   
    (88, 'pose1', 'emote-pose1'),
    (89, 'pose3', 'emote-pose3'),
    (90, 'pose5', 'emote-pose5'),
    (91, 'cutey', 'emote-cutey'),
    (92, 'thatsright', 'emote-yes'),
    (93, 'pose9', 'emote-pose9'),
    (94, 'angryy', 'emoji-angry'),   
    (95, 'miningmine', 'mining-mine'),
    (96, 'miningsuccess', 'mining-success'),
    (97, 'fishingpull', 'fishing-pull'),
    (98, 'fishingpullsmall', 'fishing-pull-small'),
    (99, 'fishingcast', 'fishing-cast'),
    (160, 'laidback', 'sit-open'),

]


positions = {
}

AUTHORIZED_ME = ["kingkong_fou","cjvjvjh","notseeN.official","its.___a","thelyann"]


class Mybot(BaseBot):

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

    @staticmethod
    def load_conversations(file_path="conversations.json"):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_conversations(conversations, file_path="conversations.json"):
        with open(file_path, "w") as f:
            json.dump(conversations, f)
    


    def load_welcome_messages(self):
        if os.path.exists(self.welcome_messages_file):
            with open(self.welcome_messages_file, "r") as file:
                self.welcome_messages = json.load(file)
        else:
            self.welcome_messages = self.default_messages
            self.save_welcome_messages()

    def save_welcome_messages(self):
        with open(self.welcome_messages_file, "w") as file:
            json.dump(self.welcome_messages, file)

    async def send_welcome_messages(self):
        if self.welcome_messages_active:
            return
        self.welcome_messages_active = True
        try:
            while True:
                for message in self.welcome_messages:
                    await self.highrise.chat(message)
                    await asyncio.sleep(10)

                await self.display_leaderboard()

                await asyncio.sleep(60)
        except Exception as e:
            logging.error(f"An error occurred in send_welcome_messages: {e}")
        finally:
            self.welcome_messages_active = False

            




    def load_levels_data(self):
        try:
            with open(self.levels_data_file, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning("Levels data file not found or empty.")
            return {}

    def save_levels_data(self):
        with open(self.levels_data_file, 'w') as file:
            json.dump(self.levels_data, file)

        

    def load_join_data(self):
        if os.path.exists(self.join_data_file):
            with open(self.join_data_file, 'r') as f:
                return json.load(f)
        return {}

    def save_join_data(self):
        with open(self.join_data_file, 'w') as f:
            json.dump(self.join_data, f)

    def load_modd(self):
        if os.path.exists(self.modd_file):
            with open(self.modd_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_modd(self):
        with open(self.modd_file, 'w') as f:
            json.dump(self.modd, f)

    def load_vip(self):
        with open(self.vip_file, 'r') as f:
            return json.load(f)
        return []
    
    def save_vip(self):
        with open(self.vip_file, 'w') as f:
            json.dump(self.vip, f)
            self.vip_file = self.vip

    def save_position(self, position_name, position, restricted=False):
        file_path = self.positions_folder / f"{position_name}.json"
        with open(file_path, 'w') as f:
            json.dump({
                "x": position.x,
                "y": position.y,
                "z": position.z,
                "facing": position.facing,
                "restricted": restricted
            }, f)

    def load_position(self, position_name):
        file_path = self.positions_folder / f"{position_name}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                data = json.load(f)
                return Position(
                    data.get("x", 0),
                    data.get("y", 0),
                    data.get("z", 0),
                    facing=data.get("facing", 'FrontRight')
                ), data.get("restricted", False)
        return None, None

    def delete_position(self, position_name):
        file_path = self.positions_folder / f"{position_name}.json"
        if file_path.exists():
            os.remove(file_path)
            return True
        return False

    def load_dynamic_positions(self):
        positions = {}
        for file in self.positions_folder.glob("*.json"):
            position_name = file.stem  # Use the filename (without .json) as the position name
            with open(file, 'r') as f:
                data = json.load(f)
                positions[position_name] = Position(
                    data.get("x", 0),
                    data.get("y", 0),
                    data.get("z", 0),
                    facing=data.get("facing", 'FrontRight')
                )
        return positions



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

        self.join_data_file = 'joinsdata.json'
        self.join_data = self.load_join_data()

        self.levels_data_file = 'levelsdata.json'
        self.levels_data = self.load_levels_data()

        self.modd_file = 'modd.json'
        self.modd = self.load_modd()

        self.vip_file = 'vip.json'
        self.vip = self.load_vip()

        self.welcome_messages_active = False

        self.frozen_users = {}

        self.teleport_mode_users = {}

        self.welcome_messages_file = "welcome_messages.json"
        self.default_messages = [
            "✨ Ohayo! ✨\nBienvenue au bar de Tokyo",
            "Votre présence rend ce lieux vivant ! 💞",
            "💖"
        ]
        
        self.load_welcome_messages()

        self.positions_folder = Path("teleport_positions")
        self.positions_folder.mkdir(exist_ok=True)  # Ensure the folder exists



    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        try:
            print(f"{user.username} joined")
            # Save the user's ID and username
            add_user(user.id, user.username)

            # Increment the user's join count
            if user.username in self.join_data:
                self.join_data[user.username] += 1
                join_count = self.join_data[user.username]
                welcome_message =(
                    f"Ohayo ! bon retour parmis nous, {user.username} 🥰 C'est votre {join_count}e fois. "
                )
            else:
                self.join_data[user.username] = 1
                join_count = self.join_data[user.username]
                welcome_message =(
                    f"Ohayo ! Bienvenue parmis nous, {user.username} 🥰 C'est vôtre première fois ici. "
                )

            self.save_join_data()  # Save the updated join data

            await self.highrise.chat(welcome_message)
            await self.highrise.send_whisper(user.id, "Envoyez moi un message en privée pour utilisé les émotes de 0 à 309 😊")
            await self.highrise.send_emote("dance-floss")
        except Exception as e:
            logging.error(f"An error occurred in on_user_join: {e}")


    async def on_user_leave(self, user: User) -> None:
        try:
            print(f"{user.username} left the room")
            
            goodbye_message =(f"Aurevoir {user.username} 👋")
            await self.highrise.chat(goodbye_message)

        except Exception as e:
            logging.error(f"An error occurred in on_user_leave: {e}")


    async def on_chat(self, user: User, message: str) -> None:
        if message.lower() == "!r":
                print(await self.highrise.restartr(user.id))
                
        elif message.lower().startswith("/getinventory"):
            inventory = await self.highrise.get_inventory()
            print(inventory)
            
        elif message.lower().startswith("/buy "):
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.chat("Commande invalide")
                return
            item_id = parts[1]
            try:
                response = await self.highrise.buy_item(item_id)
                await self.highrise.chat(f"Item bought: {response}")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                
        elif message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)
                
        elif message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Commande invalide")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print(item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print(response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
        try:
            print(f"{user.username}: {message}")
            await self.go_and_bring.handle_command(user, message)
            await self.userinfo.handle_command(user, message)
            await self.loop_emote.handle_command(user, message)
            await self.follow_commands.handle_command(user, message)
            await self.dance_bot_commands.handle_command(user, message)
            await self.joke_rizz_poetry_flirt.handle_command(user, message)

            UserEmote_ids = self.load_UserEmote_ids()



            #Leveling Up System


            username = user.username
            if username not in self.levels_data:
                self.levels_data[username] = {'messages': 0, 'level': 0}
            self.levels_data[username]['messages'] += 1
            total_messages = self.levels_data[username]['messages']
            if total_messages == LEVEL_UP_MESSAGE_THRESHOLD or \
               (total_messages - LEVEL_UP_MESSAGE_THRESHOLD) % LEVEL_UP_STEP == 0:
                self.levels_data[username]['level'] += 1
                await self.highrise.chat(f"🎉 Félicitation {username}, vous venez de passer au niveau {self.levels_data[username]['level']}! 🎉")
            self.save_levels_data()

            if message.lower().startswith("!level"):
                await self.highrise.chat(f"Vous êtes au niveau {self.levels_data[username]['level']} 😊!")

            elif message.lower() in ['vip', 'ارجع مكانك', '!goback ']: 
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or user.username in self.vip):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                if message.lower() == "vip":
                    await self.highrise.teleport(user.id, Position(5.0, 10.5, 4.5, facing='FrontRight'))
                elif message.lower() == "lllllllll":
                    await self.highrise.teleport(user.id, Position(15.5, 12, 8.5, facing='FrontRight'))
                elif message.lower() in ["ارجع مكانك", "!goback"]:
                    await self.highrise.walk_to(Position(x=1, y=0.0, z=8, facing='FrontLeft'))

            elif message.lower().startswith("!addvip "):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                username = parts[1]
                username = username.split("@")
                username = username[1]
                print(username)
                try:
                    print(f"{username} making vip")

                    # Increment the user's join count
                    if username in self.vip:
                        self.highrise.chat(f"{username} est déjà vip.")
                        print(f"{username} is already vip")
                    else:
                        self.vip.append(username)
                        self.highrise.chat(f"{username} est désormais vip.")
                        print(f"{username} is vip")

                    self.save_vip()  # Save the updated join data
                except Exception as e:
                    logging.error(f"An error occurred in on_user_join: {e}")


            elif message.lower().startswith("!create tele "):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                position_name = parts[2]
                restricted = len(parts) > 3 and parts[3].lower() == "restricted"

                room_users = (await self.highrise.get_room_users()).content

                for room_user, pos in room_users:
                    if room_user.id == user.id:
                        current_position = pos 
                        self.save_position(position_name, current_position, restricted=restricted)
                        await self.highrise.send_whisper(user.id, f"Position '{position_name}' saved for teleport (restricted={restricted}).")
                        break
                else:
                    await self.highrise.send_whisper(user.id, "Unable to save your current position.")


            elif message.lower().startswith("!remove tele "):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                position_name = message[13:].strip()  
                if self.delete_position(position_name):
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' removed.")
                else:
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' not found.")


            elif message.lower() in [f.stem.lower() for f in self.positions_folder.glob("*.json")]:
                position_name = message.lower()

                # Check if user.id is in UserEmote_ids
                if user.id not in UserEmote_ids:
                    await self.highrise.send_whisper(user.id, "Désolé, vous devez m'envoyez un message en privée pour utiliser les émotes!")
                    return

                saved_position, restricted = self.load_position(position_name)

                if restricted:
                    privilege_response = await self.highrise.get_room_privilege(user.id)
                    if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                        await self.highrise.send_whisper(user.id, "You don't have permission to access this teleport.")
                        return

                if saved_position:
                    await self.highrise.teleport(user.id, saved_position)
                    await self.highrise.send_whisper(user.id, f"Teleported to '{position_name}'.")
                else:
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' does not exist.")
            
            elif message.lower().startswith("list"):
                emote_chunk = ""
                for emote in EMOTES_LIST:
                    if len(emote_chunk) + len(emote) + 4 > 256:
                        await self.highrise.send_whisper(user.id, emote_chunk.strip())
                        emote_chunk = ""
                    emote_chunk += emote + "   "
                if emote_chunk:
                    await self.highrise.send_whisper(user.id, emote_chunk.strip())

            elif message.lower().startswith("!outfit"):
                print(await self.highrise.get_user_outfit(user.id))

            



            elif message.lower() == "!flash":
                self.teleport_mode_users[user.id] = True  
                await self.highrise.send_whisper(user.id, f"{user.username}, vous êtes maintenant en flashmode")

            elif message.lower() == "!stopflash":
                if user.id in self.teleport_mode_users:
                    del self.teleport_mode_users[user.id]
                    await self.highrise.send_whisper(user.id, f"{user.username}, Vous n'êtes plus en flashmode.")
                else:
                    await self.highrise.send_whisper(user.id, f"{user.username}, Vous n'êtes pas en flashmode.")


            if message.lower() == "!invite":
                room_id = "6800ad6f8f5b81d963124c31"
                conversations = self.load_conversations()
                for conversation_id in conversations.keys():
                    await self.highrise.send_message(conversation_id, content="", message_type="invite", room_id=room_id)



            elif message.lower().startswith("!freeze"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Commande invalide. Faites !freeze @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "Utilisateur non trouvé ou invalide.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=3600)
                    await self.highrise.chat(f"{username} a été freeze pendant 1 heure.")
                    self.frozen_users[user_id] = pos
                except Exception as e:
                    await self.highrise.chat(f"{e}")

            elif message.lower().startswith("!unfreeze"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Commande invalide. Faites !unfreeze @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "Utilisateur non trouvé ou invalide.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=1)
                    await self.highrise.chat(f"{username} a été unfrozen.")
                    self.frozen_users.pop(user_id, None)
                except Exception as e:
                    await self.highrise.chat(f"{e}")



            elif message.lower().startswith("!welcome"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                custom_messages = message[len("!welcome"):].strip().split(',')
                custom_messages = [msg.strip() for msg in custom_messages if msg.strip()]
                if len(custom_messages) > 0:
                    self.welcome_messages = custom_messages
                    self.save_welcome_messages()
                    await self.highrise.send_whisper(user.id, f"Welcome messages updated to: {', '.join(custom_messages)}")
                else:
                    await self.highrise.send_whisper(user.id, "Please provide valid messages after the command. Example: !welcome hello, hi, welcome")

    



            elif message.lower().startswith("!ban"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 3:
                    await self.highrise.send_whisper(user.id, "Invalid ban command format. Use !ban @username <minutes>.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                try:
                    duration = int(parts[2]) * 60 
                except ValueError:
                    await self.highrise.send_whisper(user.id, "Please specify a valid number of minutes for the ban.")
                    return
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "ban", action_length=duration)
                    await self.highrise.chat(f"{username} has been banned from the room for {parts[2]} minutes.")
                except Exception as e:
                    await self.highrise.chat(f"{e}")



            elif message.lower().startswith("!mute"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) < 3:
                    await self.highrise.send_whisper(user.id, "Invalid mute command format. Use !mute @username <minutes>.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                try:
                    duration = int(parts[2]) * 60 
                except ValueError:
                    await self.highrise.send_whisper(user.id, "Please specify a valid number of minutes for the mute.")
                    return
                room_users = (await self.highrise.get_room_users()).content
                user_id = None
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return

                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=duration)
                    await self.highrise.chat(f"{username} has been muted for {parts[2]} minutes.")
                except Exception as e:
                    await self.highrise.chat(f"An error occurred while trying to mute {username}: {e}")



            elif message.lower().startswith("!unmute"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid unmute command format. Use !unmute @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=1)
                    await self.highrise.chat(f"{username} has been unmuted.")
                except Exception as e:
                    await self.highrise.chat(f"An error occurred while trying to unmute {username}: {e}")



            elif message.lower().startswith("!kick"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid kick command format. Use !kick @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "kick")
                    await self.highrise.chat(f"{username} has been kicked from the room.")
                except Exception as e:
                    await self.highrise.chat(f"{e}")




            elif message.lower().lstrip().startswith(('!tele', '!wallet', '!tipme ', '!tipall ', '!tip ', '!reactall ', '!h ', '!stopreact', '!react', '!changefit')):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]



                if message.lower().startswith("!tele"):
                    args = message.split()[1:]

                    dynamic_positions = self.load_dynamic_positions()
                    positions.update(dynamic_positions)

                    if len(args) < 2:
                        await self.highrise.send_whisper(user.id, "Usage: !tele <@username> <position>")
                        return
                    elif args[0][0] != "@":
                        await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                        return
                    
                    username = args[0][1:].lower()
                    position_name = " ".join(args[1:]).lower()


                    dest = positions.get(position_name)
                    if not dest:
                        await self.highrise.send_whisper(user.id, "Unknown location")
                        return


                    users = (await self.highrise.get_room_users()).content
                    user_id = next((room_user.id for room_user, _ in users if room_user.username.lower() == username), None)
                    if not user_id:
                        await self.highrise.send_whisper(user.id, f"{username} is not in the room.")
                        return


                    await self.highrise.teleport(user_id, dest)
                    await self.highrise.send_whisper(user.id, f"Teleported {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")



                elif message.lower().startswith("!wallet"):
                    wallet = (await self.highrise.get_wallet()).content
                    await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")



                elif message.lower().startswith("!reactall "):
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    reaction = parts[1]
                    if reaction not in ['clap', 'heart', 'thumbs', 'wave', 'wink']:
                        await self.highrise.send_whisper(user.id, "Invalid reaction")
                        return
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        active_user_ids = {room_user.id for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    bot_id = "66ffb1a3989b8812d98e2b11"
                    active_user_ids.discard(bot_id)
                    async def react_to_user(user_id):
                        try:
                            for _ in range(10):
                                await self.highrise.react(reaction, user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    tasks = [react_to_user(user_id) for user_id in active_user_ids]
                    await asyncio.gather(*tasks)



                elif message.lower().startswith("!h "):
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide. Use !heart @username")
                        return
                    username = parts[1].lstrip("@")
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        user_dict = {room_user.username: room_user.id for room_user, _ in room_users}
                        if username not in user_dict:
                            await self.highrise.send_whisper(user.id, f"User {username} not found in the room.")
                            return
                        target_user_id = user_dict[username]
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    async def react_to_user(user_id):
                        try:
                            for _ in range(20):
                                await self.highrise.react('heart', user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    await react_to_user(target_user_id)
                    confirmation_message = f"Hearts have been sent to {username}! ❤️"
                    await self.highrise.chat(confirmation_message)



                elif message.lower().lstrip().startswith("!react"):
                    interval_str = message.lstrip()[6:]
                    if not interval_str.isdigit() or len(interval_str) == 0:
                        await self.highrise.send_whisper(user.id, "Commande invalide. Use !react<number>.")
                        return
                    interval = int(interval_str)
                    if interval <= 0:
                        await self.highrise.send_whisper(user.id, "Interval must be greater than 0.")
                        return
                    reaction = "heart"
                    async def react_to_user(user_id):
                        try:
                            for _ in range(5):
                                await self.highrise.react(reaction, user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    async def periodic_reactions():
                        while True:
                            try:
                                room_users = (await self.highrise.get_room_users()).content
                                active_user_ids = {room_user.id for room_user, _ in room_users}
                                bot_id = "66ffb1a3989b8812d98e2b11"
                                active_user_ids.discard(bot_id)
                                tasks = [react_to_user(user_id) for user_id in active_user_ids]
                                await asyncio.gather(*tasks)
                                await asyncio.sleep(interval)
                            except Exception as e:
                                logging.error(f"An error occurred during periodic reactions: {e}")
                                break
                    if self.react_task is None or self.react_task.done():
                        self.react_task = asyncio.create_task(periodic_reactions())
                        await self.highrise.send_whisper(user.id, f"Started reacting with hearts every {interval} seconds!")
                    else:
                        await self.highrise.send_whisper(user.id, "Reactions are already running.")



                elif message.lower().startswith("!stopreact"):
                    if self.react_task and not self.react_task.done():
                        self.react_task.cancel()
                        await self.highrise.send_whisper(user.id, "Stopped reacting with hearts!")
                        self.react_task = None
                    else:
                        await self.highrise.send_whisper(user.id, "No active reactions to stop.")



                elif message.lower().startswith("!changefit"):
                    await self.highrise.set_outfit(outfit=[
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='body-flesh',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='eye-n_basic2018zanyeyes',
                                                            account_bound=False,
                                                            active_palette=7
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='eyebrow-n_26',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='nose-n_01',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='pants-n_room12019rippedpantsblack',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='watch-n_room32019blackwatch',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='shirt-n_room12019buttondownblack',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='shoes-n_room12019sneakersblack',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='hair_back-n_malenew05',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='hair_front-n_malenew05',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='mouth-basic2018lollipop',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='glasses-n_10',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        ])



                elif message.lower().startswith("!tipme "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    try:
                        amount = int(parts[1])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    if bot_amount <= amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    bars_dictionary = {10000: "gold_bar_10k", 
                                    5000: "gold_bar_5000",
                                    1000: "gold_bar_1k",
                                    500: "gold_bar_500",
                                    100: "gold_bar_100",
                                    50: "gold_bar_50",
                                    10: "gold_bar_10",
                                    5: "gold_bar_5",
                                    1: "gold_bar_1"}
                    fees_dictionary = {10000: 1000,
                                    5000: 500,
                                    1000: 100,
                                    500: 50,
                                    100: 10,
                                    50: 5,
                                    10: 1,
                                    5: 1,
                                    1: 1}
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount = amount % bar
                            for _ in range(bar_amount):
                                tip.append(bars_dictionary[bar])
                                total += bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    tip_string = ",".join(tip)
                    await self.highrise.tip_user(user.id, tip_string)



                elif message.lower().startswith("!tipall "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    try:
                        amount = int(parts[1])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    bars_dictionary = {
                        10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        active_user_ids = {room_user.id for room_user, _ in room_users}
                        user_names = {room_user.id: room_user.username for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    bot_id = "66ffb1a3989b8812d98e2b11"
                    active_user_ids.discard(bot_id)
                    total_cost = 0
                    for user_id in active_user_ids:
                        amount_copy = amount
                        for bar in sorted(bars_dictionary.keys(), reverse=True):
                            if amount_copy >= bar:
                                bar_amount = amount_copy // bar
                                amount_copy = amount_copy % bar
                                total_cost += bar_amount * (bar + fees_dictionary[bar])
                    if total_cost > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds to tip everyone")
                        return
                    for user_id in active_user_ids:
                        try:
                            tip = []
                            amount_copy = amount
                            for bar in sorted(bars_dictionary.keys(), reverse=True):
                                if amount_copy >= bar:
                                    bar_amount = amount_copy // bar
                                    amount_copy = amount_copy % bar
                                    for _ in range(bar_amount):
                                        tip.append(bars_dictionary[bar])
                            await self.highrise.tip_user(user_id, ",".join(tip))
                            user_name = user_names.get(user_id, "Unknown")
                            await self.highrise.chat(f"💰 tipped @{user_name} {parts[1]}g!")
                            await asyncio.sleep(1)
                        except Exception as e:
                            logging.error(f"An error occurred while tipping user {user_id}: {e}")



                elif message.lower().startswith("!tip "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ", 2)
                    if len(parts) != 3:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    username = parts[1].strip("<>@")
                    try:
                        amount = int(parts[2])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    if bot_amount <= amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    bars_dictionary = {
                        10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount = amount % bar
                            for _ in range(bar_amount):
                                tip.append(bars_dictionary[bar])
                                total += bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        user_ids = {room_user.username: room_user.id for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    user_id = user_ids.get(username)
                    if user_id:
                        try:
                            await self.highrise.tip_user(user_id, ",".join(tip))
                            await self.highrise.chat(f"💰 tipped @{username} {parts[2]}g!")
                        except Exception as e:
                            logging.error(f"An error occurred while tipping user {user_id}: {e}")
                    else:
                        await self.highrise.chat(f"User @{username} not found")



            elif message.lower().endswith("all"): ##
                if len(message) < 4:
                    return
                command = message[:-3].strip()
                if command.isdigit():
                    emote_number = int(command)
                    if emote_number in range(len(emote_commands)):
                        emote_action = emote_commands[emote_number][2]
                else:
                    emote_action = None
                    for emote in emote_commands:
                        if emote[1].lower() == command.lower():
                            emote_action = emote[2]
                            break
                if emote_action:
                    privilege_response = await self.highrise.get_room_privilege(user.id)
                    if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    try:
                        roomUsers = (await self.highrise.get_room_users()).content
                        emote_tasks = []
                        for roomUser in roomUsers:
                            user_object = roomUser[0]
                            emote_tasks.append(self.highrise.send_emote(emote_action, user_object.id))
                        if emote_tasks:
                            await asyncio.gather(*emote_tasks)
                    except Exception as e:
                        logging.error(f"An error occurred in on_chat: {e}")
                else:
                    await self.highrise.send_whisper(user.id, "Invalid emote command.")

        except Exception as e:
                logging.error(f"An error occurred in on_chat: {e}")



    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        try:
            print(f"{sender.username} a tips {receiver.username} d'un montant de {tip.amount}🪙")
        except Exception as e:
            logging.error(f"An error occurred in on_tip: {e}")



    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        try:
            print(f"New message from {user_id} in {conversation_id}! Is new conversation: {is_new_conversation}")
            UserEmote_ids = self.load_UserEmote_ids()

            if user_id not in UserEmote_ids:
                UserEmote_ids[user_id] = True 
                self.save_UserEmote_ids(UserEmote_ids) 
            
            conversations = self.load_conversations()

            if conversation_id not in conversations:
                conversations[conversation_id] = True
                self.save_conversations(conversations) 

            await self.highrise.send_message(conversation_id, "Activated!")

        except Exception as e:
            logging.error(f"An error occurred in on_message: {e}")
        


    async def on_user_move(self, user: User, pos: Position) -> None: ##
        try:
            if user.username not in ["TheoCafeBot", "TheoCafeBot2", "TheoCafeBot3"]:
                print(f"{user.username} moved to {pos}")

            if user.id in self.frozen_users:
                frozen_pos = self.frozen_users[user.id]
                await self.highrise.teleport(user.id, frozen_pos)
                print(f"{user.username} was teleported back to {frozen_pos} because they are frozen.")
                return
            if user.id in self.teleport_mode_users:
                await self.highrise.teleport(user.id, pos)
                print(f"{user.username} teleported to {pos} while in teleport mode.")
                return
            
        except Exception as e:
            logging.error(f"An error occurred in on_user_move: {e}")



    async def on_moderate(self, moderator_id: str, target_user_id: str, moderation_type: Literal["kick", "mute", "unmute", "ban", "unban"], duration: int | None) -> None:
        try:
            room_users_response = await self.highrise.get_room_users()
            room_users = room_users_response.content
            user_map = {user.id: user.username for user, _ in room_users}
            moderator_name = user_map.get(moderator_id, f"User with ID {moderator_id}")
            formatted_moderator_name = f"@{moderator_name}"
            target_user_name = get_username(target_user_id)
            formatted_target_name = f"@{target_user_name}" if "User with ID" not in target_user_name else target_user_id
            if moderation_type == "kick":
                message = f"{formatted_moderator_name} kicked {formatted_target_name} from the room."
            elif moderation_type == "mute":
                message = f"{formatted_moderator_name} muted {formatted_target_name} for {duration} seconds."
            elif moderation_type == "unmute":
                message = f"{formatted_moderator_name} unmuted {formatted_target_name}."
            elif moderation_type == "ban":
                message = f"{formatted_moderator_name} banned {formatted_target_name}."
            elif moderation_type == "unban":
                message = f"{formatted_moderator_name} unbanned {formatted_target_name}."
            else:
                message = "Unknown moderation action."
            await self.highrise.chat(message)

        except Exception as e:
            logging.error(f"An error occurred in on_moderate: {e}")



    async def display_leaderboard(self): ##
        try:
            leaderboard = sorted(self.levels_data.items(), key=lambda item: item[1]['level'], reverse=True)[:10]
            if not leaderboard:
                logging.info("Leaderboard is empty!")
                await self.highrise.chat(("\n🏆 Leaderboard is empty! 🏆"))
                return
            leaderboard_message = ("\n🏆__Chat Leaderboard__🏆\n")
            header_sent = False
            leaderboard_entries = [
                (f"{index + 1}. {username} - Level {data['level']}") 
                for index, (username, data) in enumerate(leaderboard)
            ]
            for entry in leaderboard_entries:
                if len(leaderboard_message) + len(entry) + 1 > 256:
                    await self.highrise.chat(leaderboard_message)
                    leaderboard_message = "\n"
                if not header_sent:
                    leaderboard_message = ("\n🏆__Chat Leaderboard__🏆\n")
                    header_sent = True
                leaderboard_message += entry + "\n"
            if leaderboard_message.strip():
                await self.highrise.chat(leaderboard_message)

        except Exception as e:
            logging.error(f"An error occurred in display_leaderboard: {e}")





    async def on_whisper(self, user: User, message: str) -> None:
        try:
            print(f"{user.username} whispered: {message}")
            await self.go_and_bring.handle_command(user, message)
            await self.userinfo.handle_command(user, message)
            await self.loop_emote.handle_command(user, message)
            await self.follow_commands.handle_command(user, message)
            await self.dance_bot_commands.handle_command(user, message)
            await self.joke_rizz_poetry_flirt.handle_command(user, message)

            if message.lower() in ['vip', 'ارجع مكانك', '!goback']: 
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content] 
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]
                if message.lower() == "vip":
                    await self.highrise.teleport(user.id, Position(15.5, 12, 8.5, facing='FrontRight'))
                elif message.lower() in ["ارجع مكانك", "!goback"]:
                    await self.highrise.walk_to(Position(x=19.5, y=0.0, z=3.0, facing='FrontLeft'))

            elif message.lower().startswith("!create tele "):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                position_name = message[13:].strip()
                room_users = (await self.highrise.get_room_users()).content

                for room_user, pos in room_users:
                    if room_user.id == user.id:
                        current_position = pos  
                        self.save_position(position_name, current_position)
                        await self.highrise.send_whisper(user.id, f"Position '{position_name}' saved for teleport.")
                        break
                else:
                    await self.highrise.send_whisper(user.id, "Unable to save your current position.")


            elif message.lower().startswith("!remove tele "):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER or self.has_permission(user.id)):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                position_name = message[13:].strip() 
                if self.delete_position(position_name):
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' removed.")
                else:
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' not found.")

            elif message.lower() in [f.stem.lower() for f in self.positions_folder.glob("*.json")]:
                position_name = message.lower()
                saved_position = self.load_position(position_name)
                if saved_position:
                    await self.highrise.teleport(user.id, saved_position)
                    await self.highrise.send_whisper(user.id, f"Teleported to '{position_name}'.")
                else:
                    await self.highrise.send_whisper(user.id, f"Position '{position_name}' does not exist.")

            elif message.lower().startswith("list"):
                emote_chunk = ""
                for emote in EMOTES_LIST:
                    if len(emote_chunk) + len(emote) + 4 > 256:
                        await self.highrise.send_whisper(user.id, emote_chunk.strip())
                        emote_chunk = ""
                    emote_chunk += emote + "   "
                if emote_chunk:
                    await self.highrise.send_whisper(user.id, emote_chunk.strip())

            elif message.lower() == "!flashmode":
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                self.teleport_mode_users[user.id] = True  
                await self.highrise.send_whisper(user.id, f"{user.username}, you are now in flash mode! Click on a position to teleport.")

            elif message.lower() == "!stopflash":
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, f"Sorry {user.username}, you are not authorized to use this command.")
                    return
                if user.id in self.teleport_mode_users:
                    del self.teleport_mode_users[user.id]
                    await self.highrise.send_whisper(user.id, f"{user.username}, you have exited flash mode.")
                else:
                    await self.highrise.send_whisper(user.id, f"{user.username}, you are not in flash mode.")



            elif message.lower().startswith("!freeze"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid freeze command format. Use !freeze @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=3600)
                    await self.highrise.chat(f"{username} has been frozen for 1 hour.")
                    self.frozen_users[user_id] = pos
                except Exception as e:
                    await self.highrise.chat(f"{e}")

            elif message.lower().startswith("!unfreeze"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid unfreeze command format. Use !unfreeze @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=1)
                    await self.highrise.chat(f"{username} has been unfrozen.")
                    self.frozen_users.pop(user_id, None)
                except Exception as e:
                    await self.highrise.chat(f"{e}")



            elif message.lower().startswith("!welcome"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                custom_messages = message[len("!welcome"):].strip().split(',')
                custom_messages = [msg.strip() for msg in custom_messages if msg.strip()]
                if len(custom_messages) > 0:
                    self.welcome_messages = custom_messages
                    self.save_welcome_messages()
                    await self.highrise.send_whisper(user.id, f"Welcome messages updated to: {', '.join(custom_messages)}")
                else:
                    await self.highrise.send_whisper(user.id, "Please provide valid messages after the command. Example: !welcome hello, hi, welcome")

            elif message.lower().startswith("!ban"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 3:
                    await self.highrise.send_whisper(user.id, "Invalid ban command format. Use !ban @username <minutes>.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                try:
                    duration = int(parts[2]) * 60 
                except ValueError:
                    await self.highrise.send_whisper(user.id, "Please specify a valid number of minutes for the ban.")
                    return
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "ban", action_length=duration)
                    await self.highrise.chat(f"{username} has been banned from the room for {parts[2]} minutes.")
                except Exception as e:
                    await self.highrise.chat(f"{e}")



            elif message.lower().startswith("!mute"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) < 3:
                    await self.highrise.send_whisper(user.id, "Invalid mute command format. Use !mute @username <minutes>.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                try:
                    duration = int(parts[2]) * 60 
                except ValueError:
                    await self.highrise.send_whisper(user.id, "Please specify a valid number of minutes for the mute.")
                    return
                room_users = (await self.highrise.get_room_users()).content
                user_id = None
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return

                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=duration)
                    await self.highrise.chat(f"{username} has been muted for {parts[2]} minutes.")
                except Exception as e:
                    await self.highrise.chat(f"An error occurred while trying to mute {username}: {e}")



            elif message.lower().startswith("!unmute"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid unmute command format. Use !unmute @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "mute", action_length=1)
                    await self.highrise.chat(f"{username} has been unmuted.")
                except Exception as e:
                    await self.highrise.chat(f"An error occurred while trying to unmute {username}: {e}")



            elif message.lower().startswith("!kick"):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                parts = message.split()
                if len(parts) != 2:
                    await self.highrise.send_whisper(user.id, "Invalid kick command format. Use !kick @username.")
                    return
                username = parts[1][1:] if parts[1].startswith('@') else parts[1]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, pos in room_users:
                    if room_user.username.lower() == username.lower():
                        user_id = room_user.id
                        break
                else:
                    await self.highrise.send_whisper(user.id, "User not found, please specify a valid user.")
                    return
                try:
                    await self.highrise.moderate_room(user_id, "kick")
                    await self.highrise.chat(f"{username} has been kicked from the room.")
                except Exception as e:
                    await self.highrise.chat(f"{e}")




            elif message.lower().lstrip().startswith(('!tele', '!wallet', '!tipme ', '!tipall ', '!tip ', '!reactall ', '!h ', '!stopreact', '!react', '!changefit')):
                privilege_response = await self.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]



                if message.lower().startswith("!tele"):
                    args = message.split()[1:]

                    dynamic_positions = self.load_dynamic_positions()
                    positions.update(dynamic_positions)

                    if len(args) < 2:
                        await self.highrise.send_whisper(user.id, "Usage: !tele <@username> <position>")
                        return
                    elif args[0][0] != "@":
                        await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                        return
                    
                    username = args[0][1:].lower()
                    position_name = " ".join(args[1:]).lower()


                    dest = positions.get(position_name)
                    if not dest:
                        await self.highrise.send_whisper(user.id, "Unknown location")
                        return


                    users = (await self.highrise.get_room_users()).content
                    user_id = next((room_user.id for room_user, _ in users if room_user.username.lower() == username), None)
                    if not user_id:
                        await self.highrise.send_whisper(user.id, f"{username} is not in the room.")
                        return


                    await self.highrise.teleport(user_id, dest)
                    await self.highrise.send_whisper(user.id, f"Teleported {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")



                elif message.lower().startswith("!wallet"):
                    wallet = (await self.highrise.get_wallet()).content
                    await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")



                elif message.lower().startswith("!reactall "):
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    reaction = parts[1]
                    if reaction not in ['clap', 'heart', 'thumbs', 'wave', 'wink']:
                        await self.highrise.send_whisper(user.id, "Invalid reaction")
                        return
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        active_user_ids = {room_user.id for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    bot_id = "66ffb1a3989b8812d98e2b11"
                    active_user_ids.discard(bot_id)
                    async def react_to_user(user_id):
                        try:
                            for _ in range(10):
                                await self.highrise.react(reaction, user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    tasks = [react_to_user(user_id) for user_id in active_user_ids]
                    await asyncio.gather(*tasks)



                elif message.lower().startswith("!h "):
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide. Use !heart @username")
                        return
                    username = parts[1].lstrip("@")
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        user_dict = {room_user.username: room_user.id for room_user, _ in room_users}
                        if username not in user_dict:
                            await self.highrise.send_whisper(user.id, f"User {username} not found in the room.")
                            return
                        target_user_id = user_dict[username]
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    async def react_to_user(user_id):
                        try:
                            for _ in range(20):
                                await self.highrise.react('heart', user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    await react_to_user(target_user_id)
                    confirmation_message = f"Hearts have been sent to {username}! ❤️"
                    await self.highrise.chat(confirmation_message)



                elif message.lower().lstrip().startswith("!react"):
                    interval_str = message.lstrip()[6:]
                    if not interval_str.isdigit() or len(interval_str) == 0:
                        await self.highrise.send_whisper(user.id, "Commande invalide. Use !react<number>.")
                        return
                    interval = int(interval_str)
                    if interval <= 0:
                        await self.highrise.send_whisper(user.id, "Interval must be greater than 0.")
                        return
                    reaction = "heart"
                    async def react_to_user(user_id):
                        try:
                            for _ in range(5):
                                await self.highrise.react(reaction, user_id)
                        except Exception as e:
                            logging.error(f"An error occurred while reacting to user {user_id}: {e}")
                    async def periodic_reactions():
                        while True:
                            try:
                                room_users = (await self.highrise.get_room_users()).content
                                active_user_ids = {room_user.id for room_user, _ in room_users}
                                bot_id = "66ffb1a3989b8812d98e2b11"
                                active_user_ids.discard(bot_id)
                                tasks = [react_to_user(user_id) for user_id in active_user_ids]
                                await asyncio.gather(*tasks)
                                await asyncio.sleep(interval)
                            except Exception as e:
                                logging.error(f"An error occurred during periodic reactions: {e}")
                                break
                    if self.react_task is None or self.react_task.done():
                        self.react_task = asyncio.create_task(periodic_reactions())
                        await self.highrise.send_whisper(user.id, f"Started reacting with hearts every {interval} seconds!")
                    else:
                        await self.highrise.send_whisper(user.id, "Reactions are already running.")



                elif message.lower().startswith("!stopreact"):
                    if self.react_task and not self.react_task.done():
                        self.react_task.cancel()
                        await self.highrise.send_whisper(user.id, "Stopped reacting with hearts!")
                        self.react_task = None
                    else:
                        await self.highrise.send_whisper(user.id, "No active reactions to stop.")



                elif message.lower().startswith("!changefit"):
                    await self.highrise.set_outfit(outfit=[
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='body-flesh',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='eye-n_basic2018zanyeyes',
                                                            account_bound=False,
                                                            active_palette=7
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='eyebrow-n_26',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='nose-n_01',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='pants-n_room12019rippedpantsblack',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='watch-n_room32019blackwatch',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='shirt-n_room12019buttondownblack',
                                                            account_bound=False,
                                                            active_palette=0
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='shoes-n_room12019sneakersblack',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='hair_back-n_malenew05',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='hair_front-n_malenew05',
                                                            account_bound=False,
                                                            active_palette=1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='mouth-basic2018lollipop',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        Item(
                                                            type='clothing',
                                                            amount=1,
                                                            id='glasses-n_10',
                                                            account_bound=False,
                                                            active_palette=-1
                                                        ),
                                                        ])



                elif message.lower().startswith("!tipme "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    try:
                        amount = int(parts[1])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    if bot_amount <= amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    bars_dictionary = {10000: "gold_bar_10k", 
                                    5000: "gold_bar_5000",
                                    1000: "gold_bar_1k",
                                    500: "gold_bar_500",
                                    100: "gold_bar_100",
                                    50: "gold_bar_50",
                                    10: "gold_bar_10",
                                    5: "gold_bar_5",
                                    1: "gold_bar_1"}
                    fees_dictionary = {10000: 1000,
                                    5000: 500,
                                    1000: 100,
                                    500: 50,
                                    100: 10,
                                    50: 5,
                                    10: 1,
                                    5: 1,
                                    1: 1}
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount = amount % bar
                            for _ in range(bar_amount):
                                tip.append(bars_dictionary[bar])
                                total += bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    tip_string = ",".join(tip)
                    await self.highrise.tip_user(user.id, tip_string)



                elif message.lower().startswith("!tipall "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ")
                    if len(parts) != 2:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    try:
                        amount = int(parts[1])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    bars_dictionary = {
                        10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        active_user_ids = {room_user.id for room_user, _ in room_users}
                        user_names = {room_user.id: room_user.username for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    bot_id = "66ffb1a3989b8812d98e2b11"
                    active_user_ids.discard(bot_id)
                    total_cost = 0
                    for user_id in active_user_ids:
                        amount_copy = amount
                        for bar in sorted(bars_dictionary.keys(), reverse=True):
                            if amount_copy >= bar:
                                bar_amount = amount_copy // bar
                                amount_copy = amount_copy % bar
                                total_cost += bar_amount * (bar + fees_dictionary[bar])
                    if total_cost > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds to tip everyone")
                        return
                    for user_id in active_user_ids:
                        try:
                            tip = []
                            amount_copy = amount
                            for bar in sorted(bars_dictionary.keys(), reverse=True):
                                if amount_copy >= bar:
                                    bar_amount = amount_copy // bar
                                    amount_copy = amount_copy % bar
                                    for _ in range(bar_amount):
                                        tip.append(bars_dictionary[bar])
                            await self.highrise.tip_user(user_id, ",".join(tip))
                            user_name = user_names.get(user_id, "Unknown")
                            await self.highrise.chat(f"💰 tipped @{user_name} {parts[1]}g!")
                            await asyncio.sleep(1)
                        except Exception as e:
                            logging.error(f"An error occurred while tipping user {user_id}: {e}")



                elif message.lower().startswith("!tip "):
                    if user.username.lower() not in OWNER_USER:
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    parts = message.split(" ", 2)
                    if len(parts) != 3:
                        await self.highrise.send_whisper(user.id, "Commande invalide")
                        return
                    username = parts[1].strip("<>@")
                    try:
                        amount = int(parts[2])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    if bot_amount <= amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    bars_dictionary = {
                        10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount = amount % bar
                            for _ in range(bar_amount):
                                tip.append(bars_dictionary[bar])
                                total += bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        user_ids = {room_user.username: room_user.id for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Failed to retrieve room users")
                        logging.error(f"An error occurred while retrieving room users: {e}")
                        return
                    user_id = user_ids.get(username)
                    if user_id:
                        try:
                            await self.highrise.tip_user(user_id, ",".join(tip))
                            await self.highrise.chat(f"💰 tipped @{username} {parts[2]}g!")
                        except Exception as e:
                            logging.error(f"An error occurred while tipping user {user_id}: {e}")
                    else:
                        await self.highrise.chat(f"User @{username} not found")



            elif message.lower().endswith("all"):
                if len(message) < 4:
                    return
                command = message[:-3].strip()
                if command.isdigit():
                    emote_number = int(command)
                    if emote_number in range(len(emote_commands)):
                        emote_action = emote_commands[emote_number][2]
                else:
                    emote_action = None
                    for emote in emote_commands:
                        if emote[1].lower() == command.lower():
                            emote_action = emote[2]
                            break
                if emote_action:
                    privilege_response = await self.highrise.get_room_privilege(user.id)
                    if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                        await self.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                        return
                    try:
                        roomUsers = (await self.highrise.get_room_users()).content
                        emote_tasks = []
                        for roomUser in roomUsers:
                            user_object = roomUser[0]
                            emote_tasks.append(self.highrise.send_emote(emote_action, user_object.id))
                        if emote_tasks:
                            await asyncio.gather(*emote_tasks)
                    except Exception as e:
                        logging.error(f"An error occurred in on_chat: {e}")
                else:
                    await self.highrise.send_whisper(user.id, "Invalid emote command.")

        except Exception as e:
                logging.error(f"An error occurred in on_chat: {e}")