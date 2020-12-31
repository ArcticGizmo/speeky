from speeky import audio

def whatIs(match, target):
  message = "{} -- Is something that I need to look up".format(target)
  audio.say(message)
  print(message)

def say(match, target):
  audio.say(target)