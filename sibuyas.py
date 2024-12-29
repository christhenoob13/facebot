import re

def font(type, text):
  real = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  def tae(fon, lis):
    output = ""
    for char in lis:
      if char not in list(real):
        output += char
      else:
        vh = real.index(char)
        output += fon[vh]
    return output
  match type:
    case 'bold':
      BOLD = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
      return tae(BOLD, list(text))
    case 'mono':
      MONO = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
      return tae(MONO, list(text))
    case _:
      return text

def text_formatter(text):
  match = re.findall(r":(\w+)\[([^\]]+)\]", text)
  if len(match) < 1:
    return text
  else:
    output = text
    for TYPE, TEXT in match:
      prince_text = font(TYPE, TEXT)
      output = output.replac(f":{TYPE}[{TEXT}]", prince_text)
    return output