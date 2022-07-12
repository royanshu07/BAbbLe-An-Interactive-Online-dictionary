import sys, a1,os

logo=''' * WELCOME TO BAbbLe:An Interactive Online dictionary *\n'''

main_menu=rf'''
{logo}
 MAIN MENU-
 1) Search a word
 2) Quit
'''


def main():
    while True:
        msg='Enter your choice from 1-3: '
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
    

ALL_ARGS=['--ADD', '-A', '--SEARCH', '-S','-D','--DOC', '-H','--HELP']
args=sys.argv[1:]
args=[i.upper() for i in args]

if args==[]:
    arg='MAIN'

elif args[-1] in ALL_ARGS:
    arg=args[-1]
else:
    arg='-S'



    
if arg in ['--ADD','-A']:
    dictionary.add_new_word()


elif arg=='MAIN':
    main()
    sys.exit()

elif arg in ['-D','--DOC','-H','--HELP']:
    os.system('cls')
    print(__doc__)

elif arg in ['-S','--SEARCH'] :
    try:word=''.join(args.remove(arg))
    except:word=''.join(args)
    dictionary.search_word(word)


