from google.cloud import speech

client = speech.SpeechClient.from_service_account_file('key.json')

audio_file= speech.RecognitionAudio(content=file_one)

config = speech.RecognitionConfig(
    sample_rate_hertz = 44100,
    enable_automatic_punctuation = True,
    language_code = 'en-US' 
)
# recognize file
response = client.recognize(
    config=config,
    audio=audio_file,
)
# print text
print(response)

# we can also print only text
for result in response.results:
    print(result.alternatives[0]. transcript)