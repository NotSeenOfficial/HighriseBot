
import random
import json
from pathlib import Path
from highrise import BaseBot, User

class JokeRizzPoetryFlirt:
    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.lines = {
            "jokes": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",
                "Why don't eggs tell jokes? They'd crack up!",
                "What do you call a bear with no teeth? A gummy bear!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ],
            "rizz": [
                "Are you a magician? Because whenever I look at you, everyone else disappears.",
                "Are you made of copper and tellurium? Because you're Cu-Te!",
                "Are you a camera? Because every time I look at you, I smile!",
                "Do you have a map? I keep getting lost in your eyes.",
                "Is your name Google? Because you've got everything I've been searching for!"
            ],
            "poetry": [
                "Roses are red, violets are blue, sugar is sweet, and so are you!",
                "The night is young, the stars are bright, your presence here makes everything right.",
                "Through sunshine and rain, through joy and pain, our friendship remains, again and again.",
                "Life is a journey we travel each day, with friends like you lighting the way.",
                "In moments of silence, in times of noise, your friendship brings me endless joys."
            ],
            "flirt": [
                "You must be a ninja, because you snuck right into my heart!",
                "Is it hot in here or is it just you?",
                "If you were a vegetable, you'd be a cute-cumber!",
                "Are you French? Because Eiffel for you!",
                "Do you like science? Because we've got great chemistry!"
            ]
        }

    async def handle_command(self, user: User, message: str) -> None:
        if message.lower().startswith("!joke"):
            await self.bot.highrise.chat(f"🎭 {random.choice(self.lines['jokes'])}")
        
        elif message.lower().startswith("!rizz"):
            await self.bot.highrise.chat(f"💘 {random.choice(self.lines['rizz'])}")
        
        elif message.lower().startswith("!poetry"):
            await self.bot.highrise.chat(f"📝 {random.choice(self.lines['poetry'])}")
        
        elif message.lower().startswith("!flirt"):
            await self.bot.highrise.chat(f"💝 {random.choice(self.lines['flirt'])}")
