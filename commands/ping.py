async def ping(bot, event, **dick):
  await bot.sendMessage("Ping")

config = {
  "name": 'ping',
  "def": ping
}