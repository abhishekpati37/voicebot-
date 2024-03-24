import speech_recognition as sr
from gtts import gTTS
import os

# Sample college information data structure (can be replaced with database)
college_info = {
    "computer science": "Computer Science program offers...",
    "biology": "Biology program provides...",
    "history": "History program covers...",
    "library": "Our library is equipped with...",
    "labs": "We have state-of-the-art labs...",
    "sports": "Sports facilities include..."
}

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")

# Function to listen to user's speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your query.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        return ""

# Function to process user's query and provide response
def process_query(query):
    response = college_info.get(query, "Sorry, I couldn't find information about that.")
    return response

# Main function
def main():
    print("Welcome to College Enquiry System VoiceBot!")
    speak("Welcome to College Enquiry System VoiceBot!")
    while True:
        speak("How can I assist you?")
        query = listen()
        if query == "exit":
            print("Exiting the system.")
            speak("Exiting the system.")
            break
        response = process_query(query)
        speak(response)

if __name__ == "__main__":
    main()
