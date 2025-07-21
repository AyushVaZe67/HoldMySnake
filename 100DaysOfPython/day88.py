import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set the text you want to convert to speech
text = "Hello Ayush! This is a text-to-speech example using Python."

# Speak the text
engine.say(text)

# Wait for the speech to complete
engine.runAndWait()
