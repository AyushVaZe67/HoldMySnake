import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# List to speak
l1 = ['Ayush', 'Mia', 'Angela', 'Ava']

# Join the list into a single string
text = ', '.join(l1)

# Speak the text
engine.say("The names are: " + text)

# Play the speech
engine.runAndWait()
