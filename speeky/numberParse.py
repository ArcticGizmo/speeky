units = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]

tens = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]

NUM_WORDS = {}

NUM_WORDS["and"] = (1, 0)
for idx, word in enumerate(units):
    NUM_WORDS[word] = (1, idx)
for idx, word in enumerate(tens):
    NUM_WORDS[word] = (1, idx * 10)
for idx, word in enumerate(scales):
    NUM_WORDS[word] = (10 ** (idx * 3 or 2), 0)


def text2Int(text):
    current = result = 0
    for word in text.split():
        if word not in NUM_WORDS:
            return None

        scale, increment = NUM_WORDS[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current