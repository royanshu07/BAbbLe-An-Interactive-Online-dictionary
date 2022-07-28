import json, time
import os
from difflib import SequenceMatcher as SM
import sys
import search
import google_python,a2




FILE='D.json'



D={}
D_List=[]


    
def __get_words(word, D_List):
    if word.upper() in D_List:
        return word.upper()
    else:
        Word_List=[i for i in D_List if i[0].upper()==word[0].upper()]
        Matches={}

        for test_word in Word_List:
            ratio=SM(None,test_word.upper(), word.upper()).ratio()
            if ratio>0.72:
                temp={test_word:round(ratio*100,2)}
                Matches.update(temp)

        val=list(Matches.values())
        val.sort(reverse=1)
        val=val[:5]
        temp={}

        for j in val:
            for i in Matches:
                if Matches[i]==j:
                    temp.update({i: j})
        Matches=temp

        if len(Matches)==0:
        
            print(f'\nWord your entered: {word}')
            print(f"{'-'*60}")
            print('No close matches were found, you might have entered a wrong word...')
            return None

        else:
            print(f'{word.upper()} was not found. We found {len(Matches)} close matches:')
            print('+-----------------------------+')
            print('|    Word  -  Percent Match   |')
            print('+-----------------------------+')
            j=0
            for i in Matches:
                j=j+1
                print('| %-16s - %-9s|' % ( i, f'{Matches[i]} %'))
            print('+-----------------------------+')
            best_match=list(Matches.keys())[0]
            print(f'\n**{best_match} ({Matches[best_match]} %) is the best match for the word - {word.upper()}')
        return best_match.upper()

def print_meanings(word,data):
    print('WORD: ',word)
    MEANINGS=data['MEANINGS']
    ANTONYMS=data['ANTONYMS']
    SYNONYMS=data['SYNONYMS']

    if SYNONYMS!=[]:
        SYNONYMS=', '.join(SYNONYMS)
        print('SYNONYMS: ',SYNONYMS)
    if ANTONYMS!=[]:
        ANTONYMS=', '.join(ANTONYMS)
        print('ANTONYMS: ',ANTONYMS)
    print('\n')

    L=[]
    j=0
    print(' -- MEANINGS --\n')
    to_print='\n  NO MEANINGS AVAILABLE FOR THIS WORD'
    for sense_num in MEANINGS:
        template=f'  * %s (%s) - %s\n%s%s'   # word, t, m, c, e
        temp=MEANINGS[sense_num]
        t=temp[0]
        m=temp[1]
        c=temp[2]
        if c!=[]:
            c='\tIN CONTEXT WITH: '+'/ '.join(c)
        else:
            c=''


        e=temp[3]
        e=[f'{str(i)}. {e[i]}' for i in range(len(e))]
        if e!=[]:
            e='\n\tEXAMPLES :-\n\t\t'+'\n\t\t'.join(e)
        else:
            e=''
        L+=[template % (word, t, m, c, e)]
        to_print=f'\n\n'.join(L)
        j+=1
        if j%2==0:
            print(to_print)
            to_print=''
            L=[]
            
    print(to_print)



def search_word(word):
    global D_List, D

    letter=word[0].upper()

    
    f=open(f"D:\IT\data\\D{letter}.json")
    data=f.read()
    D=json.loads(data)
    f.close()
    D_List=D.keys()
    


    word=__get_words(word, D_List)
    if word!=None:
        data=D[word]
        print_meanings(word, data)
        a2.speak("Want to google search? IF yes press 'g'")
        choose=input("Want to google search? IF yes press 'g'")
        if choose=='g':
            google_python.google(word)


    return word
