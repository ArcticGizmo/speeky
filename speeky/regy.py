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

def parsePattern(pattern):
  if type(pattern) is str:
    return pattern
  namedPatterns = []
  for (index, part) in enumerate(pattern):
    match = re.match(r'^:(.*):(.*)', part)
    name = (match.group(1) or 'p{}'.format(index)) if match else None
    test = match.group(2) if match else part
    
    if name:
      namedPatterns.append(r'(?P<{}>{})'.format(name, test))
    else:
      namedPatterns.append('({})'.format(test))

  return r" ".join(namedPatterns)

def resolveActions(actions, text):
  resolutions = []
  for action in actions:
    match = re.search(action.pattern, text, flags=re.IGNORECASE)
      
    if match:
      resolutions.append((action, match))

  return resolutions

def resolveFirstAction(actions, text):
  resolutions = resolveActions(actions, text)
  if len(resolutions):
    (action, match) = resolutions[0]
    action.callback(match, *match.groupdict().values())
  else:
    print("No action for '{}'".format(text))


def main():
  actions = [
    Action(['What is a', '::(.*)'], lambda match, target: print('What is a "{}"'.format(target))),
    Action(['Define', '::(.*)'], lambda match, target: print('Define the word "{}"'.format(target))),
    Action([r'::\d', 'times', r'::\d'], lambda match, a, b: print('{} x {} = {}'.format(a, b, int(a) * int(b))))
  ]

  resolveFirstAction(actions, 'What is a cat man')
  resolveFirstAction(actions, 'bad start What is a cat man')
  resolveFirstAction(actions, '5 times 6')

  # analyizeText('What is a cat', r'(What is) (?P<xpple>a) (?P<eggplant>.*)')


def analyizeText(text, pattern):
  match = re.match(pattern, text)
  if match:
    print('{} -- {} -- {}'.format(text, match.groups(), match.groupdict().values()))
  else:
    print('No match on text: "{}"'.format(text))