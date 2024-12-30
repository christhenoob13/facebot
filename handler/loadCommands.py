import os
import importlib

commands = {}

# ━━━━━━━━━━━━━━━ ⦿
def loadCommands():
  if commands:
    return commands
  files = list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./commands')))
  print("\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Commands\033[97m ⦿━━━━━━━━━━━━━━━⦿")
  for file in files:
    filepath = f"commands.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      function = config.get('def')
      if not name:
        print(f"\033[31mCOMMAND NOT LOADED\033[0m ({file})")
      elif not function:
        print(f"\033[31mCOMMAND NOT LOADED\033[0m ({file})")
      else:
        for char in list(name):
          if char.lower() not in list('abcdefghijklmnopqrstuvwxyz0123456789'):
            print(f"\033[31mERROR: \033[97m({file}) Invalid character in command name")
            break
        else:
          commands[name.lower()] = config
          print(f"\033[1;97mCOMMAND LOADED: \033[0;93m{name} \033[0m- \033[35m({file})\033[0m")
  print("\033[92m[LIVE] \033[0mBot is now online")
  return commands