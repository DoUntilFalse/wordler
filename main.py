import random
from tqdm import tqdm


def guess(guessWord, targetWord):
    remainLetters = set()
    gPos = []
    yPos = []
    for i, (x, y) in enumerate(zip(guessWord, targetWord)):
        if x == y:
            gPos.append(i)
        else:
            remainLetters.add(y)
    for i, x in enumerate(guessWord):
        if i not in gPos and x in remainLetters:
            yPos.append(i)
    return " ".join(map(str, gPos)) + " | " + " ".join(map(str, yPos))


def genStates(word, words):
    states = {}
    for x in words:
        state = guess(word, x)
        if state not in states:
            states[state] = [x]
        else:
            states[state].append(x)
    return states


def lenStates(states):
    return max(map(len, states.values()))


def genGuess(words):
    word = ""
    ansstates = {}
    maxx = 1000000
    for ans in tqdm(words):
        states = genStates(ans, words)
        l = lenStates(states)
        if maxx > l:
            maxx = l
            ansstates = states
            word = ans
    return word, ansstates


def main():
    with open("words.txt") as f:
        words = f.read().splitlines()
    # targetWord = random.choice(words)
    # print("target:", targetWord)
    for i in range(6):
        print(f"round {i}")
        if i == 0:
            word = "arise"
            states = genStates(word, words)
        else:
            word, states = genGuess(words)
        print("word: ", word)
        # res = guess(word, targetWord)
        # print("res: ", res)
        res = input()
        if res == "0 1 2 3 4 | ":
            print("Found: ", word)
            break
        words = states[res]
    else:
        print("Bad!")


if __name__ == "__main__":
    main()
