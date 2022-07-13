import sys, a1,os







main_menu='''
 * WELCOME TO **** BAbbLe:An Interactive Online dictionary ***
 MAIN MENU-
 1) Search a word
 2) Quit
'''




msg='Enter your choice from 1-2: '
while True:
    print(main_menu)

    choice = input(msg)
    if choice =='1':
        print('\n\n ** STARTING SEARCH **')
        word=input('\nEnter a word: ')
        a1.search_word(word)
        input('Enter to continue...')

    

    if choice =='2':
        print('\n\n  ** GOODBYE **')
        break

    if choice not in ['1', '2','3','4','5']:
        msg='Enter only numbers from 1 to 4: '
    else:
        msg='Enter your choice: '







