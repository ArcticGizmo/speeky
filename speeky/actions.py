from speeky import audio, numberParse
import re


def whatIs(match, target):
    message = "{} -- Is something that I need to look up".format(target)
    print(message)
    # audio.say(message)


def say(match, target):
    audio.say(target)


class Replaceable(object):

    def __init__(self, string):
        self._string = string

    def replace(self, pattern, replacement, count=0, flags=0):
        self._string = re.sub(pattern, replacement, self._string, count, flags)
        return self

    def toString(self):
        return self._string


def calculate(match, target):
    # replace human words for actions (plus, minus, negative, multiply|times, divide)
    # maybe eventually "open bracket" "close bracket" "to the power of"

    parsedTarget = Replaceable(target)\
        .replace('plus|add', '+')\
        .replace('take|subtract|negative', '-')\
        .replace("divice", "/")\
        .replace('times|multiplied by', '*')\
        .replace("to the power of", "**")\
        .replace("open bracket", "(")\
        .replace("close(d*) bracket", ")")\
        .toString()

    # split against all operators so that words can be parsed
    parts = re.split('([+\-*/])', parsedTarget)
    parts = [str(numberParse.text2Int(part) or part) for part in parts]

    print(parts)


def text2Number(match, target):
  textAsInt = numberParse.text2Int(target)
  print(textAsInt)
  # audio.say(textAsInt)