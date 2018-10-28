from words import greetings
import random

def greeting(name, familiar_score):
    acceptable_phrases = [] #list of phrases within familiar score
    for words in greetings:
        if int(greetings[words]) <= familiar_score:
            acceptable_phrases.append(words)
    greet = random.choice(acceptable_phrases) #randomly choose a greeting
    greeting_phrase = str(greet +' ' +name)
    return greeting_phrase

print(greeting('bob',10))