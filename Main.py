import os
import highrise
from highrise import BaseBot, User, ChannelMessage

class Bot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("✅ Bot conectado correctamente")
        await self.chat("¡Hola! Soy un bot configurado con Render 🤖")

    async def on_channel_message(self, user: User, message: ChannelMessage) -> None:
        if message.content.lower() == "!hola":
            await self.chat(f"¡Hola, {user.username}! 👋")

if __name__ == "__main__":
    bot_token = os.environ["BOT_TOKEN"]    # Leerá el token desde Render
    bot_name = os.environ["BOT_NAME"]      # Leerá el nombre desde Render
    room_id = os.environ["ROOM_ID"]        # Leerá el ID de sala desde Render
    highrise.main(bot_token, bot_name, Bot, room_id)
