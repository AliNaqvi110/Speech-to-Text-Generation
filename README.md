# Speech-to-Text Generation

## Overview
<p>
  The Speech-to-Text Generation project is a versatile and powerful tool for converting spoken language into written text. It harnesses the capabilities of various Python libraries, including the popular SpeechRecognition library and the Google Cloud Speech-to-Text API, to provide accurate and efficient speech recognition across multiple languages.
</p>

## Key Features
1. <b>Real-time Speech Recognition:</b> Capture audio input from a microphone in real-time and convert it into text.
2. <b>Language Support:</b> The project offers multilingual support, allowing users to transcribe speech in languages such as English, Urdu, French, and more
3. <b>Export Options:</b> Save transcriptions as text files, audio files, or CSV files, providing flexibility in how you store and use the transcribed data.
4. <b>Google Cloud Integration:</b> Utilize the power of Google Cloud's Speech-to-Text API for high-quality and accurate speech recognition.
5. <b>Easy-to-Use Interface:</b> A user-friendly interface ensures that even beginners can quickly get started with the project.

## How It Works
1. <b>Capture Audio:</b> The project captures audio input from a connected microphone.
2. <b>Speech Recognition:</b> It utilizes the SpeechRecognition library to perform initial speech recognition.
3. <b>Google Cloud Integration:</b> For enhanced accuracy and multilingual support, the project seamlessly integrates with Google Cloud's Speech-to-Text API.
4. <b>Language Support:</b> Users can choose from a variety of supported languages for transcription.
5. <b>Export Options:</b> Transcriptions can be exported in various formats, making it convenient to work with the transcribed data.

## Getting Started
<p>To get started with the Speech-to-Text Generation project, follow the installation </p>
 1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```
3. Obtain an API key from GCP and add it to the `key.json` file in the project directory. If you want to use speech_to_text_google_cloud.py

    ```shell
    Key.json =your_secret_GCP_api_key
    ```
4. Run

    ```
    python run speech_text.py
    ```  

## Use Cases
1. <b>Transcription Services:</b> Ideal for businesses or individuals who need to transcribe audio recordings or interviews quickly and accurately.
2. <b>Multilingual Support:</b> Great for projects involving multiple languages, such as language learning apps or global communication platforms.
3. <b>Data Analysis:</b> Transcribed text can be further processed and analyzed for insights and trends.
4. <b>Accessibility:</b> Improve accessibility for individuals with hearing impairments by converting spoken content into readable text.

## Contributions
<p>Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or additional features, please submit a pull request.</p>

## License
<p>This project is licensed under the MIT License.</p>

