########## Promt to check for more words ##########
def checkmore():

    more=input('Search for more words? [y/n]: ')

    if str.lower(more)=='y':
        recur()
    elif str.lower(more)=='n':
        print('Goodbye!')
    else:
        print('Please enter Y or N')
        checkmore()

########## Function to suggest sililar words ##########
def suggest(lc,word):

    yn=input ("Did you mean '" + get_close_matches(lc,data.keys(),cutoff=0.8)[0] + "' instead? [y/n]: ")
    if str.lower(yn)=='y':
        return(search(get_close_matches(lc,data.keys(),cutoff=0.8)[0]))
    elif str.lower(yn)=='n':
        return 'Please check the word'
    else:
        print('Please enter Y or N')
        suggest(word)

########## Function to search for word ##########
def search(word):

    if word in data:
        return data[word]
    if word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif get_close_matches(word.lower(),data.keys(),cutoff=0.8)==[]:
        return ('"' + word + '" not found.')
    else:
        print ('"' + word + '" not found.')
        return(suggest(word.lower(),word))

########## Keep searching for words until user wants to exit the program ##########
def recur():

    word=input("Enter a word: ")
    output=search(word)

    if type(output)==list:
        for item in output:
            print (item)
    else:
        print(output)

    checkmore()

########## Main ##########
import json
import difflib
from difflib import get_close_matches
data=json.load(open('data.json'))

recur()

########## Exit ##########
