from words import *
import random
import time

def greeting(name, familiar_score):
    acceptable_phrases = [] #list of phrases within familiar score
    for words in greetings:
        if int(greetings[words]) <= familiar_score:
            acceptable_phrases.append(words)
    greet = random.choice(acceptable_phrases) #randomly choose a greeting
    greeting_phrase = str(greet + ' ' + name)
    return greeting_phrase

def state_of_mind(wellbeing):
    for words in how_are_you:
        if wellbeing == words:
            state = how_are_you[words]
    if state >=4:
        time.sleep(random.randint(1, 5))
        print('great to hear!')
    if state > 3 and state <4:
        time.sleep(random.randint(1, 5))
        print('cool')
    if state < 3:
        time.sleep(random.randint(1, 5))
        print('sorry to hear')

def transition():
    transition_list = ['want to talk?']
    trans = str(random.choice(transition_list))
    return trans

def main():
    #intro
    name = input('hi, what is your name')
    print(greeting(name, 10))
    time.sleep(random.randint(1, 2))
    #how are you?
    wellbeing = input('how are you?')
    state_of_mind(wellbeing)

    #transition to see if wanna talk
    transition_statement = str(transition())
    talk_q = input(transition_statement)

    if talk_q in yes_answers:
        proceed = 'Y'
    if talk_q in no_answers:
        proceed = 'N'
        print('ok, goodbye')
    while proceed =='Y':
    #get to know
        question = random.choice(get_to_know)
        time.sleep(random.randint(1,5))
        response = str(input(question))

        react = response.replace('I','You')
        print(react)
main()