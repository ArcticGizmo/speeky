from speeky import audio, numberParse
import re
from simpleeval import simple_eval


def whatIs(match, target):
    message = '{} -- Is something that I need to look up'.format(target)
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
    parsedTarget = Replaceable(target)\
        .replace('plus|add', '+')\
        .replace('take|subtract|negative', '-')\
        .replace('divide', '/')\
        .replace('times|multiplied by', '*')\
        .replace('to the power of', '**')\
        .replace('open bracket', '(')\
        .replace('close(d*) bracket', ')')\
        .replace('mod(ulus)*', '%')\
        .replace('equals', '==')\
        .replace('less than', '<')\
        .replace('less than or equal to', '<')\
        .replace('greater than', '>')\
        .replace("squared", "**2")\
        .replace("pi", "3.1415")\
        .replace('greater than or equal to', '>=')\
        .toString()

    # split against all operators so that number words can be parsed
    parts = re.split('([+\-*/=<>])', parsedTarget)
    expression = ''.join(
        [str(numberParse.text2Int(part) or part) for part in parts])

    print(expression)

    try:
        answer = simple_eval(expression)
        print(answer)
    except:
        print('!Unable to perform calculation!')


def text2Number(match, target):
    textAsInt = numberParse.text2Int(target)
    print(textAsInt)
    # audio.say(textAsInt)
