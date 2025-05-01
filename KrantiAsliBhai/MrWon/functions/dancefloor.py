from highrise import BaseBot, Position
import asyncio
import random
import time






class DanceFloor:

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.emote_duration_mapping = {
                'emote-float': 8.995302,
                'emote-frog': 14.55257,
                'emote-hot': 4.353037,
                'emote-maniac': 4.906886,
                'emote-gravity': 8.955966,
                'dance-russian': 10.252905,
                'emote-zombierun': 12.922772,
                'emote-punkguitar': 9.365807,
                'idle-guitar': 13.229398,
                'emote-teleporting': 11.7676,
                'dance-tiktok10': 8.225648,
                'dance-tiktok2': 10.392353,
                'idle-dance-tiktok4': 15.500708,
                'dance-tiktok8': 10.938702,
                'dance-tiktok9': 11.892918,
                'dance-shoppingcart': 4.316035,
                'dance-blackpink': 7.150958,
                'dance-anime': 8.46671,
                'emote-telekinesis': 10.492032,
                'emote-energyball': 7.575354,
                'dance-icecream': 14.769573,
                'emote-snowangel': 6.218627,
                'idle_singing': 10.260182,
                'emote-snake': 5.262578,
                'dance-weird': 21.556237,
                'dance-wrong': 12.422389,
                'emote-headblowup': 11.667537,
                'emote-boxer': 5.555702,
                'dance-employee': 8,
                'emote-celebrationstep': 3.353703,
                'emote-iceskating': 7.299156,
                'dance-kawai': 10.290789,
                'dance-pinguin': 11.58291,
                'emote-timejump': 4.007305,
                'emote-swordfight': 5.914365,
                'emote-astronaut': 13.791175,
                'dance-jinglebell': 10.958832,
                'emote-hyped': 7.492423,
                'emote-looping': 9.0,
                'dance-creepypuppet': 6.416121,
                'emote-sleigh': 11.333165,
                'emote-launch': 9.4,
                'dance-tiktok11': 10.8,  
            }
        self.position_bounds = {
            'x': (3, 11),
            'y': (0, 5.75),
            'z': (6, 9.5),
        }
        self.position_bounds2 = {
            'x': (4, 11),
            'y': (0, 5.75),
            'z': (1, 5),
        }
        self.last_emote_times = {}
        self.last_emote_durations = {}

    async def send_continuous_random_emotes_in_dance_floor(self):
        while True:
            try:
                room_users = await self.bot.highrise.get_room_users()
                current_time = time.time()

            
                emoting_users = {
                    user_id: self.last_emote_times[user_id]
                    for user_id in self.last_emote_times
                    if current_time - self.last_emote_times[user_id] < self.last_emote_durations[user_id]
                }

                
                if not emoting_users:
                    emote_name = random.choice(list(self.emote_duration_mapping.keys()))

               
                emote_tasks = []

                for user, position in room_users.content:
                    if isinstance(position, Position):
                        x, y, z = position.x, position.y, position.z

                      
                        if (
                            self.position_bounds['x'][0] <= x <= self.position_bounds['x'][1] and
                            self.position_bounds['y'][0] <= y <= self.position_bounds['y'][1] and
                            self.position_bounds['z'][0] <= z <= self.position_bounds['z'][1] or
                            self.position_bounds2['x'][0] <= x <= self.position_bounds2['x'][1] and
                            self.position_bounds2['y'][0] <= y <= self.position_bounds2['y'][1] and
                            self.position_bounds2['z'][0] <= z <= self.position_bounds2['z'][1]
                        ):
                            last_emote_time = self.last_emote_times.get(user.id, 0)
                            time_difference = current_time - last_emote_time

                            
                            if not emoting_users and time_difference >= self.last_emote_durations.get(user.id, 0):
                                emote_duration = self.emote_duration_mapping[emote_name]
                                emote_tasks.append(self.bot.highrise.send_emote(emote_name, user.id))

                                
                                self.last_emote_times[user.id] = current_time
                                self.last_emote_durations[user.id] = emote_duration

                
                if emote_tasks:
                    await asyncio.gather(*emote_tasks)

            except Exception as e:
                print(f"An error occurred: {e}")