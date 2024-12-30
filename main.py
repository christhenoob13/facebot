import asyncio
import aiofbchat
import json
import os

from aiofbchat import Client, FacebookError, NotLoggedIn, UnknownEvent
from aiofbchat._events import Connect, Disconnect
from aiofbchat._events._delta_class import MessageEvent
from handler.handleMessage import messageHandler
from handler.loadCommands import loadCommands

def get_cookie():
  appstate = json.load(open('greeg.json', 'r'))
  cookies = {x['key']:x['value'] for x in appstate}
  return cookies

done = False
async def load():
  #os.system('cls' if os.name == 'nt' else 'clear')
  return loadCommands()

async def listen(listener, session: aiofbchat.Session):
  try:
    async for event in listener.listen():
      # if pag run mo may nag display na napakahabang json data
      # hindi ko rin alam kung bakit lumalabas yun. :)
      if isinstance(event, UnknownEvent):
        print("[EVENT] UNKNOWN EVENT")
      if isinstance(event, Connect):
        print("\033[92m[CONNECTED] \033[0mBot is now online")
      if isinstance(event, MessageEvent):
        if event.author.id != session.user.id:
          await messageHandler(event)
  except FacebookError:
    print("Fcabeook ERROR")

# Muhammad MuQit's code
async def main():
  try:
    session = await aiofbchat.Session.from_cookies(get_cookie())
    client = aiofbchat.Client(session=session)
    listener = aiofbchat.Listener(session=session, chat_on=True, foreground=True)
    listen_task = asyncio.create_task(listen(listener, session))
    client.sequence_id_callback = listener.set_sequence_id
    await client.fetch_threads(limit=1).__anext__()
  except Exception as d:
    print("ERROR --> ", d)
  try:
    await load()
    await listen_task
  except NotLoggedIn:
    print("\033[91m[ERROR] \033[0mUnable to login account")
  except KeyboardInterrupt:
    await session._session.close()
  finally:
    await session._session.close()

if __name__ == '__main__':
  asyncio.run(main())