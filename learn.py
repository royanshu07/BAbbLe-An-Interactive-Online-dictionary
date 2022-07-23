import a1,a2
import json
import random 
import string



FILE='D.json'



D={}
D_List=[]

def learn_new():
    global D_List, D
    alphabet=random.choice(string.ascii_letters)
    letter=alphabet.upper()

    f=open(f"D:\IT\data\\D{letter}.json")
    data=f.read()
    D=json.loads(data)
    f.close()
    D_List=list(D.keys())
    word = random.choice(D_List)
    a1.search_word(word);
    a2.speak("Learn to pronounce? if yes,press Y")
    print("\n Learn to pronounce? if yes,press Y")
    choice=input()
    if choice=='Y'or choice=='y':
        a2.speak(word)
    input("\n\nPress the enter key to continue")
                    
        

    

    
