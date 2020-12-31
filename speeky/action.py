import re
import importlib


class Action(object):

    def __init__(self, name, pattern, trigger):
        self.name = name
        self.pattern = _parsePattern(pattern)
        self.trigger = trigger

    def __str__(self):
      return '{} | Pattern: {}'.format(self.name, self.pattern)


def fromConfig(config):
    trigger = getattr(importlib.import_module(
        config["module"]), config["function"]
    )
    return Action(config["name"], config["pattern"], trigger)


def _parsePattern(pattern):
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


def resolveText(actions, text):
  for action in actions:
    match = re.search(action.pattern, text, flags=re.IGNORECASE)

    if match:
      return action.trigger(match, *match.groupdict().values())

  print("-- Unknown command")