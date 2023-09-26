# import librarirs
import pandas as pd
import speech_recognition as sr
import os
import csv

from csv import writer
import io

# function to recognize
def recognize_speech():
  recognizer = sr.Recognizer() # To recognize speech
  
  # creating source to get audio fule we can also use directory to open audio file
  # But at this point we will use Microphone
  with sr.Microphone() as source:
    # To remove Noise
    recognizer.adjust_for_ambient_noise(source)
    # Print message to the user
    print('Hi dear Say something!')
    # get audio
    audio = recognizer.listen(source)

    # Using Recognizer to detect speech
    try:
        text_file = (recognizer.recognize_google(audio, language='ur-PK'))
        data = pd.DataFrame({'text': text_file}, index=[0])
        print("You have said : \n " + text_file)
        data.to_csv('text.csv', mode='a', index=False, header=False)



    except Exception as e:
      print("Error "+ str(e))

if __name__=="__main__":
    # calling function
    recognize_speech()