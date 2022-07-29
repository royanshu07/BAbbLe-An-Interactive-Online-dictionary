INDIRA GANDHI DELHI TECHNICAL UNIVERSITY FOR WOMEN 
              IT WORKSHOP PROJECT 
              
     BAbbLe:An Interactive Online  dictionary

 
 
Team: Group No.7 (B.Tech CSE- AI 2nd Semester)
       01901172021 Shreya Mittal
       02301172021 Anshu Roy
       04201172021 Srishti Gupta
 

Introduction:
A Dictionary is the most important tool to understand the vocabulary of any language because it has all the words that are there in the vocabulary of a language listed in it. To learn English vocabulary and pronunciation as quickly as possible, you can use an online dictionary. Technology is fascinating and fast, and only a traditionalist or a person incapable of affording it (which is rare after smartphones barged in) would like to pore through a heavy, small-font printed treatise to find a word.
We have created BAbbLe: An Interactive Online dictionary, built using python and its various modules.
Following are the functions in this Dictionary-
1.Dictionary that speaks for convenient use.
2. To get the meaning of the word.
3. To get antonym and synonym of the word.
4. If the word is misspelled, it will provide word suggestions and the meaning of the closest matching word.




5. To provide the user choice between text search and voice search.
6. By supplementing audio to teach the   word’s pronunciation to the user.
7. Chrome browse the word.
8. Play Jumble word game.
9. Vocabulary Enrichment - Improving user’s vocabulary by teaching a new word.
         

Methodology:
Terminal Setup-
In order to create this application, Concepts of gTTS, playsound, speech recognition ,JSON, File Reading, selenium, chromedriver.exe, Python Data Structure and difflib, time, random, string module etc. are being used.
 
 
TEXT TO SPEECH: The text-to-speech (TTS) is the process of converting words into a vocal audio form. The program, tool, or software takes an input text from the user, and using methods of natural language processing understands the linguistics of the language being used, and performs logical inference on the text. This processed text is passed into the next block where digital signal processing is performed on the processed text. Using many algorithms and transformations this processed text is finally converted into a speech format. This entire process involves the synthesizing of speech. Below is a simple block diagram to understand the same.
 
Google Text to Speech API commonly known as the gTTS API is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.
Primary Requirement for using gTTS: An active internet connection with at least a moderate bandwidth because we will be using the Google API for the text to speech translation.

The playsound module is used to play audio files. With this module, we can play a sound file with a single line of code.

SPEECH RECOGNITION: Speech recognition is a machine's ability to listen to spoken words and identify them. Speech recognition in Python works with algorithms that perform linguistic and acoustic modelling. Acoustic modelling is used to recognize phenones/phonetics in our speech to get the more significant part of speech, as words and sentences.
 
Speech recognition starts by taking the sound energy produced by the person speaking and converting it into electrical energy with the help of a microphone. It then converts this electrical energy from analog to digital, and finally to text. 
It breaks the audio data down into sounds, and it analyses the sounds using algorithms to find the most probable word that fits that audio. 
SpeechRecognition package-Offers easy audio processing and microphone accessibility. The package has a Recognizer class which is used to recognize the speech. We have used recognize_google( ) class in our program.
pyaudio module-To use the microphones. We use the microphone class to get the input speech from the microphone instead of any other input method like an audio file.

SEARCHING WORD USING JSON FILE:  JSON stands for JavaScript Object Notation. JSON is a lightweight format for storing and transporting data. JSON is "self-describing" and easy to understand. In JSON data is stored in name/value pairs, data is separated by commas, curly braces hold objects. In our program when the word is entered or converted to text from speech→>
1.it is passed to search_word function, where the json file is opened using the first letter of the word in capital. Two global variable D_list and D are declared. All the data from the particular JSON file is loaded to variable data. From data variable it is loaded to D. All the keys from the D is stored in D_list.
2.Function _get_words is called where the word and D_list are passed as arguments. This function will check for the word in the D_list if the word is present it will return the word, if not then it will return the closest matching word using diffilib.
3. print_meaning function is called where the word and Data are passed as arguments. Here the meaning, synonym, antonym and sentences using that word are printed.
 
GOOGLE SEARCH: We can chrome browse the word using selenium (a browser automation tool). We need chromedriver.exe to launch  the chrome browser and web driver package from the Selenium framework to open it.

JUMBLED WORD GAME: This feature helps the user to learn new words by playing a simple game using random module that will select any random number corresponding to which there is a word. The word generated will then jumbled and displayed to the user If the user guesses the word correctly, then the execution of the program stops and if not guessed correctly then the user will be again asked to input the right word until the user enters the correct word.

LEARNING NEW WORD: We have created a feature where we can learn a new word for vocabulary enrichment of the user. A random letter will be selected from a string of ascii letters using string and random module. A json will be opened having all the info like the word as the key and meaning and other details as the value. A list will be created out of the dictionary keys(word). A random word starting with the pre-randomly chosen alphabet will be randomly selected from the list, the word with all its information will be given as the output. We also have the feature to learn pronunciation of the new word using gTTS.

Working of the project:
 
 Program Files and JSON file --->

main.py - File where all the other files are imported, and main program is run.
 
a1.py - Searching and printing of word using JSON.

a2.py - gtts pronounciation

voice.py - gtts speech recognition

game.py - jumbled word function

learn.py - learning new word using random

google_python.py - Google Search 

data.7z - Highly Compressed JSON file.


 
 

Flowchart of BAbbLe




 
Future Scope and Implementation:
1.	Spelling and grammar checker like grammarly.
2.	Converting handwritten notes to text.
3.	Converting text to handwritten text.
4.	Adding more functions to make it fully functionable for disabled people.
5.	Adding features like diary entry, notepad etc.
6.	Translation to Hindi and other native languages.
7.	Stating the origin of the word.    
8.	Stating the origin of the word.    


 
 
 
 


