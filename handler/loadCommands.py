import os
import importlib

def loadCommands():
  commands = {}
  if commands:
    return commands:
  files = list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./commands')))
  for file in files:
    filepath = f"commands.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      function = config.get('def')
      # DO-TO