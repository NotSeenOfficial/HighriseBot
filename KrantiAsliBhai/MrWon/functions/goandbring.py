from highrise import BaseBot, User, Position
from owner import OWNER_USER
from pathlib import Path
import json
import random

class GoAndBringCommands:
    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def has_permission(self, user: User) -> bool:
        """Check if the user is a moderator."""
        privilege_response = await self.bot.highrise.get_room_privilege(user.id)
        return privilege_response.moderator or user.username.lower() in OWNER_USER

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        # Check user permission before proceeding
        if not await self.has_permission(user):
            await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
            return
        
        try:
            response = await self.bot.highrise.get_room_users()
            for target, position in response.content:
                if target.username.lower() == target_username.lower():
                    new_position = Position(position.x + 1, position.y, position.z, position.facing)
                    await self.bot.highrise.teleport(user.id, new_position)
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_to_me(self, user: User, target_username: str) -> None:
        # Check user permission before proceeding
        if not await self.has_permission(user):
            await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
            return

        try:
            response = await self.bot.highrise.get_room_users()
            my_position = next((pos for usr, pos in response.content if usr.id == user.id), None)
            if my_position is None:
                print("Unable to retrieve your position.")
                return

            for target, _ in response.content:
                if target.username.lower() == target_username.lower():
                    new_position = Position(my_position.x + 1, my_position.y, my_position.z, facing='FrontRight')
                    await self.bot.highrise.teleport(target.id, new_position)
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} to you: {e}")

    async def bring_all_to_teleport(self, user: User, teleport_name: str) -> None:
        # Check user permission and ownership
        if user.username.lower() not in OWNER_USER:
            await self.bot.highrise.send_whisper(user.id, "Only owners can use this command.")
            return

        try:
            # Load the teleport position
            position_path = Path("teleport_positions") / f"{teleport_name}.json"
            if not position_path.exists():
                await self.bot.highrise.send_whisper(user.id, f"Teleport position '{teleport_name}' not found.")
                return

            with open(position_path, 'r') as f:
                pos_data = json.load(f)
                teleport_pos = Position(
                    pos_data.get("x", 0),
                    pos_data.get("y", 0),
                    pos_data.get("z", 0),
                    facing=pos_data.get("facing", 'FrontRight')
                )

            # Get all users in room
            response = await self.bot.highrise.get_room_users()
            bot_id = "66ffb1a3989b8812d98e2b11"

            # Teleport all users except the bot
            for room_user, _ in response.content:
                if room_user.id != bot_id:
                    try:
                        # Add slight offset to prevent stacking
                        offset_pos = Position(
                            teleport_pos.x + (random.random() - 0.5),
                            teleport_pos.y,
                            teleport_pos.z + (random.random() - 0.5),
                            facing=teleport_pos.facing
                        )
                        await self.bot.highrise.teleport(room_user.id, offset_pos)
                    except Exception as e:
                        print(f"Failed to teleport {room_user.username}: {e}")

            await self.bot.highrise.chat(f"Teleported everyone to {teleport_name}!")

        except Exception as e:
            print(f"An error occurred while teleporting all users: {e}")

    async def handle_command(self, user: User, message: str) -> None:
        # This method will already handle permission checks for the commands
        if message.lower().startswith(("!goto", "اذهب")):
            target_username = message.split("@")[-1].strip()
            await self.teleport_to_user(user, target_username)

        elif message.lower().startswith("!bring all "):
            teleport_name = message[11:].strip()
            await self.bring_all_to_teleport(user, teleport_name)

        elif message.lower().startswith(("!bring", "اسحب")):
            target_username = message.split("@")[-1].strip()
            await self.teleport_user_to_me(user, target_username)