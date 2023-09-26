# import librarirs
import speech_recognition as sr

# function to recognize
def recognize_speech():
  recognizer = sr.Recognizer() # To recognize speech
  
  # creating source to get audio fule we can also use directory to open audio file
  # But at this point we will use Microphone
  with sr.Microphone() as source:
    # To remove Noise
    # We can also use duration=4 to open microphone for 4 sec, by default is 5 sec
    # We can also specify offset=3 which will start recording at 3 sec, and will ignore first 2 secs.
    recognizer.adjust_for_ambient_noise(source)
    # Print message to the user
    print('Hi dear Say something!')
    # get audio
    audio = recognizer.listen(source)

    # Using Recognizer to detect speech
    try:
      print("You have said : \n " + recognizer.recognize_google(audio))
      # Saving in a file
      with open("Recordeedaudio.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print('Recorded Successfully')
    except Exception as e:
      print("Error "+ str(e))

if __name__=="__main__":
    # calling function
    recognize_speech()