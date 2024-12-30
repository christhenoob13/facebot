async def echo(bot, event):
  await bot.sendMessage(f":bold[ECHO: ] {event.args}", event.message.id)

config = {
  "name": 'echo',
  "def": echo,
  "allow_prefix": True
}