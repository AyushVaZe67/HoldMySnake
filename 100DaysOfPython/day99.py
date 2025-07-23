import time
from plyer import notification
import winsound
import os

sound_path = "C:\\Windows\\Media\\Windows Notify System Generic.wav"

while True:
    time.sleep(5)

    # Show Notification
    notification.notify(
        title='Ayush',
        message='Drink Water',
        timeout=2
    )

    # Play Sound
    if os.path.exists(sound_path):
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)
    else:
        print("Sound file not found!")
