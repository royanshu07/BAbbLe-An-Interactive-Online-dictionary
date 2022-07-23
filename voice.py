import time
import speech_recognition as sr

def get_audio():
   
    r=sr.Recognizer()
    with sr.Microphone()as source:
        r.adjust_for_ambient_noise(source) 
        audio=r.listen(source)
        said=""
        

        try:
            said=r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return said



            
