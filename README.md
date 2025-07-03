# SPEECH-RECOGNITION-SYSTEM

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*:LISBON RAJA B

*INTERN ID*:CT04DG3488

*DOMAIN*:WEB DEVELOPMENT

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTOSH

*DESCRIPTION*:
               
This Python script is designed to provide a simple yet effective solution for converting speech contained in audio files into text using the popular SpeechRecognition library. By leveraging Google’s free Web Speech API, the script enables developers, students, or hobbyists to build a functional speech-to-text pipeline without the need for training complex machine learning models or dealing with low-level audio processing. The core function, transcribe_speech(), takes the file path of an audio file as input, opens the file using SpeechRecognition’s AudioFile class, and initializes a recognizer instance to process the audio. The script uses the listen() method with customizable timeout and phrase_time_limit parameters, ensuring that it avoids indefinite blocking in case of silent or lengthy recordings. Once the audio is captured, it attempts to transcribe the speech content using recognize_google(), which sends the audio data to Google’s Web Speech API and retrieves the recognized text. The script also includes error handling for common issues: if the speech in the audio is unintelligible or silent, it returns a user-friendly message indicating that the audio could not be understood, and if there is a network or API issue, it gracefully informs the user with a descriptive error message. The example usage block provided in the script’s main section demonstrates how to call the transcription function on a sample .wav file and print the resulting text, making it straightforward to adapt and integrate into other Python projects or automation pipelines. This script can serve as a foundational component for applications such as automated note-taking, voice-controlled interfaces, accessibility tools for transcribing recorded lectures or meetings, or even language learning software that requires accurate transcription of spoken phrases. Since it uses Google’s online service, an internet connection is required during transcription, but this approach ensures high-quality speech recognition without local compute overhead. The script also shows best practices for working with the SpeechRecognition library, including proper use of context managers to handle audio file resources, and demonstrates a clean, readable structure that is easy to extend—for example, by adding support for alternative recognition engines like Sphinx or integrating additional pre-processing steps such as noise reduction or audio segmentation for longer recordings. To set up the script, users simply need to install the SpeechRecognition library using pip, ensuring compatibility with Python 3 environments. The script assumes the input audio is in a format supported by SpeechRecognition, with .wav files being the most reliable choice for offline processing, but formats like FLAC and AIFF can also work depending on the backend and system configuration. Overall, this project highlights how to build a robust and user-friendly speech-to-text tool with minimal dependencies, empowering developers to quickly prototype voice-enabled features or transcription services in their applications, research projects, or assistive technologies. By including comprehensive error handling and clear instructions, this script makes speech transcription accessible to a broad audience, encouraging experimentation and learning in the fields of speech processing and natural language understanding.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/d7befacd-0d13-480f-a68c-40760990debd)
