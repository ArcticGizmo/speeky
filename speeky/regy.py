import re

# what do I want to callback to have access to
# pattern: no (kind pointless, you know how you got here)
# raw match: yes (gives full flexibility on the match results)
# group parameters: yes, but modified
#   this should only return the parts of the sentence that we care about (Ie not the action words)

# how do we filter the returned groups?

class Action(object):

  def __init__(self, pattern, callback):
    self.pattern = parsePattern(pattern)
    self.callback = callback

  def __str__(self):
    return 'Pattern: {}'.format(self.pattern)

class ResolvedAction(object):

  def __init__(self, action, match):
    self.action = action
    self.match = match

def parsePattern(pattern):
  if type(pattern) is str:
    return pattern
  namedPatterns = []
  for (index, part) in enumerate(pattern):
    match = re.match(r'^:(.*):(.*)', part)
    name = (match.group(1) or index) if match else None
    test = match.group(2) if match else part
    
    if name:
      namedPatterns.append('?P<{}>{}'.format(name, test))
    else:
      namedPatterns.append(test)

  return " ".join(namedPatterns)

def resolveActions(actions, text):
  resolutions = []
  for action in actions:
    match = re.match(action.pattern, text)
      
    if match:
      resolutions.append(ResolvedAction(action, match))

  return resolutions

def resolveFirstAction(actions, text):
  resolutions = resolveActions(actions, text)
  if len(resolutions):
    resolution = resolutions[0]
    resolution.action.callback(resolution.match, resolution.action)
  else:
    print("No action for '{}'".format(text))

def main():
  a = Action(r'(What is a) (.*)', lambda match, action: print('What is a "{}"'.format(match.groups())))
  print(a)

  b = Action(['What is a', ':apple:(.*)', '::(.*)'], lambda match, action: print('What is a "{}"'.format(match.groups())))
  print(b)



  # actions = [
  #   Action(r'(What is a) (.*)', lambda match, action: print('What is a "{}"'.format(match.groups()))),
  #   Action(r'(Define the word) (.*)', lambda match, action: print('Define the word "{}"'.format(match.groups()))),
  #   Action(r'(\d) times (\d)', lambda match, action: print('Times table: {}'.format(match.groups())))
  # ]

  # resolveFirstAction(actions, 'What is a cat man')

  # analyizeText('What is a cat', r'(What is) (?P<xpple>a) (?P<eggplant>.*)')


def analyizeText(text, pattern):
  match = re.match(pattern, text)
  if match:
    print('{} -- {} -- {}'.format(text, match.groups(), match.groupdict().values()))
  else:
    print('No match on text: "{}"'.format(text))