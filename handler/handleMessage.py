from .loadCommands import loadCommands
from sibuyas import (
  text_formatter
)
import json
import asyncio
import requests
import os

COMMANDS = loadCommands()

class Bogart:
  def __init__(self, x, v, **kiff):
    self.sender = x
    self.message = v
    self.prefix = kiff.get('prefix')
    self.args = kiff.get('args')
    self.cmd = kiff.get('cmd')
    self.commands = kiff.get('commands')

class Bot:
  def __init__(self, thread, message=None):
    self.api = thread
    #self.message = message
  async def __getUrl(self, url):
    try:
      res = await requests.get(url)
      return res.content
    except Exception as e:
      print(f"ERROR: (handleMessage.py:22) - {e}")
      return None
  async def sendMessage(self, obj, reply_to=None, files=None, mentions=None, **kwargs):
    if isinstance(obj, str):
      send = await self.api.send_message(text_formatter(obj), files=files, reply_to_id=reply_to, mentions=mentions)
      return send
    elif isinstance(obj, dict):
      TXT = obj.get('text')
      ATTACH = obj.get('attachment')
      FILES = []
      TEXT = text_formatter(TXT) if TXT else ''
      # === Attacgment ===
      async def TITE(attachment):
        if len(attachment) == 3:
          RAINIER = list(attachment)
          if attachment[1].startswith('https://'):
            j = await self.__getUrl(attachment[1])
            if not j:
              RAINIER = None
          if RAINIER:
            FILES.append(RAINIER)
      if isinstance(ATTACH, tuple):
        await TITE(ATTACH)
      elif isinstance(ATTACH, list):
        for deck in ATTACH:
          await TITE(deck)
      # === Attacgment ===
      send = await self.api.send_message(
        TEXT,
        reply_to_id = reply_to,
        mentions = mentions,
        files = FILES
      )
      return send

async def run_command(event, CONFIG, PREFIX, args, cnp):
  THREAD = event.thread
  SENDER = event.author
  MESSAGE = event.message
  BOT = Bot(THREAD)
  EVENT = Bogart(SENDER, MESSAGE,
    prefix = PREFIX,
    args = args,
    cmd = cnp,
    commands = COMMANDS
  )
  function = CONFIG["def"]
  
  send = await function(BOT, EVENT)
  return send


async def messageHandler(event):
  CONFIG = json.load(open('config.json', 'r'))
  PREFIX = CONFIG.get('prefix', '') or ''
  MESSAGE = event.message.text
  
  _x_ = MESSAGE.split(' ', 1) if MESSAGE else ['']
  cmd,args = _x_ if len(_x_)>1 else [_x_[0],''];cmd = cmd.lower()
  cnp = cmd if not cmd.startswith(PREFIX) else cmd[1:]

  def is_use_prefix(command):
    tae = COMMANDS[cnp].get('allow_prefix')
    return tae if tae == True else False
  
  if COMMANDS:
    if cmd.startswith(PREFIX):
      # check if command not in command list
      if cnp not in COMMANDS:
        await event.thread.send_message(f"⚠️ Command '{cnp}' not found",
          reply_to_id=event.message.id
        )
      
      # check if command dont need a prefix to use
      if not is_use_prefix(cmd):
        await event.thread.send_message("⚠️ This command don't need a prefix",
          reply_to_id=event.message.id
        )
      else:
        send = await run_command(event, COMMANDS[cnp], PREFIX, args, cnp)
        return send
    else:
      if cnp in COMMANDS:
        if not is_use_prefix(cmd):
          send = await run_command(event, COMMANDS[cnp], PREFIX, args, cnp)
          return send
        else:
          await event.thread.send_message("⚠️ This command required to use prefix")