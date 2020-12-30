import re

# It will probably be better to have the input regex as a list (or regex string)
# In the list form it will be easier to define an action, and the part where the data must be collected
#   this also makes it easier to eventually nest list queries together so that not everything need to be run at once

class Action(object):

  def __init__(self, pattern, callback):
    self.pattern = pattern
    self.callback = callback

  def __str__(self):
    return 'Pattern: {}'.format(self.pattern)

class ResolvedAction(object):

  def __init__(self, action, match):
    self.action = action
    self.match = match


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
  actions = [
    Action(r'(What is a) (.*)', lambda match, action: print('What is a "{}"'.format(match.groups()))),
    Action(r'(Define the word) (.*)', lambda match, action: print('Define the word "{}"'.format(match.groups()))),
    Action(r'(\d) times (\d)', lambda match, action: print('Times table: {}'.format(match.groups())))
  ]

  resolveFirstAction(actions, 'What is a cat man')

def analyizeText(text, pattern):
  match = re.match(pattern, text)
  if match:
    print('{} -- {}'.format(text, match.groups()))
  else:
    print('No match on text: "{}"'.format(text))