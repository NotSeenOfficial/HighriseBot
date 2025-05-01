import aiohttp
from highrise import BaseBot, User
from typing import Optional

class IPLScore:
    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.match_details = None

    async def fetch_live_score(self) -> Optional[dict]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.cricapi.com/v1/currentMatches', 
                                    params={'apikey': '8a55576c-641e-4f03-b1f8-066e763fc8d0', 'offset': '0'}) as response:
                    print("API Response:", await response.text())  # Debug print
                    if response.status == 200:
                        data = await response.json()
                        for match in data.get('data', []):
                            if 'Indian Premier League' in match.get('series', ''):
                                self.match_details = match
                                return match
                    return None
        except Exception as e:
            print(f"Error fetching score: {str(e)}")
            return None

    def format_score(self, match: dict) -> str:
        try:
            if not match:
                return "No live IPL matches found. Please try again later when a match is in progress."

            team1 = match['teamInfo'][0]['shortname']
            team2 = match['teamInfo'][1]['shortname']

            score_str = f"🏏 IPL Live Match: {team1} vs {team2}\n\n"

            if 'score' in match:
                for score in match['score']:
                    team_name = score.get('inning', '').split(' ')[0]
                    runs = score.get('r', 0)
                    wickets = score.get('w', 0)
                    overs = score.get('o', 0)
                    score_str += f"{team_name}: {runs}/{wickets} ({overs} overs)\n"

            if match.get('status'):
                score_str += f"\nStatus: {match['status']}"

            return score_str
        except Exception as e:
            return f"Error formatting score: {str(e)}"

    async def handle_command(self, user: User, message: str) -> None:
        if message.lower().startswith("!iplscore") or message.lower() == "!ipl":
            try:
                match = await self.fetch_live_score()
                score = self.format_score(match)
                await self.bot.highrise.chat(score)
            except Exception as e:
                await self.bot.highrise.chat(f"Error fetching IPL score: {str(e)}")

        elif message.lower() == "!iplinfo":
            if not self.match_details:
                await self.bot.highrise.chat("No match data available. Try !iplscore first.")
                return
                
            info = (
                f"📊 Match Information:\n"
                f"Venue: {self.match_details.get('venue', 'N/A')}\n"
                f"Match Type: {self.match_details.get('matchType', 'N/A')}\n"
                f"Time: {self.match_details.get('date', 'N/A')}"
            )
            await self.bot.highrise.chat(info)
            
        elif message.lower() == "!iplhelp":
            help_text = (
                "🏏 IPL Bot Commands:\n"
                "!iplscore - Get live match score\n"
                "!iplinfo - Get match details\n"
                "!iplhelp - Show this help message"
            )
            await self.bot.highrise.chat(help_text)