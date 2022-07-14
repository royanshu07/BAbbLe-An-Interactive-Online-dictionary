import sys, a1,os,a2







main_menu='''
 * WELCOME TO **** BAbbLe:An Interactive Online dictionary ***
 MAIN MENU-
 1) Search a word
 2) Quit.
'''




msg='Enter your choice from 1-2: '
while True:
    a2.speak("welcome to babble")
    print(main_menu)
    a2.speak("press 1 to search and 2 to exit the dictionary")


    choice = input(msg)
    if choice =='1':
        a2.speak('Press t for text search and v for voice search')
        print('Press t for text search and v for voice search')
        
        search_option=input()
        if search_option=='t':
            word=input('\nEnter a word: ')
            a1.search_word(word)
        elif search_option=='v':
            word=a2.get_audio()
            a1.search_word(word)
        else:
            msg=("enter t or v for search")
            a2.speak("enter t or v for search")
            
           
        print("\n Learn to pronounce? if yes,press Y")
        a2.speak("Learn to pronounce? if yes,press Y")
        check=input()
        if check=='Y':
            a2.speak(word)
        input('Enter to continue...')

    

    if choice =='2':
        print('\n\n peace out  ')
        a2.speak("peace out")
        break

    if choice not in ['1', '2','3','4','5']:
        msg='Enter only numbers from 1 to 4: '
    else:
        msg='Enter your choice: '







