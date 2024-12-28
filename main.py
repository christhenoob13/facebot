import asyncio
import aiofbchat
import json

from aiofbchat import Client
from aiofbchat._events import Connect, Disconnect
from aiofbchat._events._delta_class import MessageEvent

def get_cookie():
  appstate = json.load(open('greeg.json', 'r'))
  cookies = {x['key']:x['value'] for x in appstate}
  return cookies

#====== <======>
async def ping(bot, event):
  await bot.send_message('Pong!', reply_to_id=event.message.id)

config = {
  "name": 'ping',
  "def": ping
}
#====== <======>

class Bogart:
  def __init__(self, x,v):
    self.sender = x
    self.message = v

async def listen(listener, session: aiofbchat.Session):
  async for event in listener.listen():
    if isinstance(event, Connect):
      print("Bot is connected")
    if isinstance(event, MessageEvent):
      # If you're not the author, echo
      if event.author.id != session.user.id:
        haha = Bogart(event.author, event.message)
        if config['name'] == event.message.text.lower():
          await config['def'](event.thread, haha)
        #data = Bogart(event.author, event.message)
        #print(event.thread)
        #await event.thread.send_message("Hello!", reply_to_id=event.message.id)

# Muhammad MuQit's code
async def main():
  session = await aiofbchat.Session.from_cookies(get_cookie())
  client = aiofbchat.Client(session=session)
  listener = aiofbchat.Listener(session=session, chat_on=True, foreground=True)
  listen_task = asyncio.create_task(listen(listener, session))
  client.sequence_id_callback = listener.set_sequence_id
  await client.fetch_threads(limit=1).__anext__()
  try:
    await listen_task
  except KeyboardInterrupt:
    await session._session.close()
  finally:
    await session._session.close()

asyncio.run(main())