import sys
from random import choice

ngrams = dict()
beginnings = list()

word_limit = 500
n = 3
source = sys.stdin


def feed(text):
    # Take text word-by-word
    word_list = text.split(" ")

    # Skip text if less than order
    if len(word_list) < n:
        return

    # Add first gram in text to beginnings
    beginning = tuple(word_list[:n])
    beginnings.append(beginning)

    for i in range(len(word_list) - n):
        # Gram at i
        gram = tuple(word_list[i:i+n])

        # Word following i. gram
        next_word = word_list[i+n]

        # Build dict of grams and what words follow each
        if gram in ngrams:
            ngrams[gram].append(next_word)
        else:
            ngrams[gram] = [next_word]


def generate():
    # Start with a random word
    current = choice(beginnings)
    output = list(current)

    # Stop when max is reached...
    for i in range(word_limit):
        # ...or if nothing follows this gram
        if current in ngrams:
            # Well, does something follow it?
            possible_next = ngrams[current]

            # Pick a random following word, consider it a gram
            nextGram = choice(possible_next)

            # Add it to the output
            output.append(nextGram)

            # Repeat with gram at end of output
            current = tuple(output[-n:])
        else:
            break

    # Return as normal string
    return ' '.join(output)


if __name__ == "__main__":
    # Build beginnings list and ngrams dict from text
    for line in source:
        line = line.strip()
        feed(line)

    # Print blather to stdout
    blather = ""
    while not blather:
        blather = generate()

    print(blather)
