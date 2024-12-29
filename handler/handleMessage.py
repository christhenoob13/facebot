from .loadCommands import loadCommands
from sibuyas import (
  text_formatter
)
import json
import asyncio

class Bogart:
  def __init__(self, x,v):
    self.sender = x
    self.message = v

class Bot:
  def __init__(self, thread, message):
    self.api = thread
    self.message = message
  def sendMessage(self, obj):
    if isinstance(obj, str):
      # INFO: TO-DI

def run_command(event, CONFIG, PREFIX, args, cnp):
  BOT = event.thread
  SENDER = event.author
  MESSAGE = event.message
  setattr(MESSAGE, "args", args)
  setattr(MESSAGE, "cmd", cnp)
  setattr(BOT, "prefix", PREFIX)
  setattr(BOT, "commands", COMMANDS)
  EVENT = Bogart(SENDER, MESSAGE)
  function = CONFIG["def"]

def messageHandler(event):
  CONFIG = json.load(open('config.json', 'r'))
  PREFIX = config.get('prefix', '') or ''
  COMMANDS = loadCommands()
  
  _x_ = MESSAGE.text.split(' ', 1)
  cmd,args = _x_ if len(_x_)>1 else [_x_[0],''];cmd = cmd.lower()
  cnp = cmd if not cmd.startswith(PREFIX) else cmd[1:]

  def is_use_prefix(command):
    tae = COMMANDS[cnp].get('allow_prefix')
    return tae if tae == True else False
  
  if cmd.startswith(PREFIX):
    # check if command not in command list
    if cnp not in COMMANDS:
      return event.thread.send_message(f"⚠️ Command '{cnp}' not found",
        reply_to_id=event.message.id
      )
    
    # check if command dont need a prefix to use
    if not is_use_prefix(cmd):
      return event.thread.send_message("⚠️ This command don't need a prefix",
        reply_to_id=event.message.id
      )
    else:
      return run_command(event, CONFIG, PREFIX, args, cnp)
  else:
    if cnp in COMMANDS:
      if not is_use_prefix(cmd):
        return run_command(event, CONFIG, PREFIX, args, cnp)
      else:
        return event.thread.send_message("⚠️ This command required to use prefix")
"""
  if cnp in COMMANDS:
    BOT = event.thread
    SENDER = event.author
    MESSAGE = event.message
    setattr(MESSAGE, "args", args)
    setattr(MESSAGE, "cmd", cnp)
    setattr(BOT, "prefix", PREFIX)
    setattr(BOT, "commands", COMMANDS)
    EVENT = Bogart(SENDER, MESSAGE)
    
    function = CONFIG["def"]
    
    # [USER] [COMMAND]
    if is_use_prefix(cmd) and cmd.startswith(PREFIX):
      return function(BOT, EVENT)
    
    # (USER) (COMMAND)
    elif not is_use_prefix(cmd) and cmd.startswith(PREFIX):
      return function(BOT, EVENT)
    
    elif not is_use_prefix(cmd) and cmd.startswith(PREFIX):
      pass
    else:
      BOT.send_message("⚠️ This command ")
"""