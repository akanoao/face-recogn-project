import time
from playsound import playsound

while True:
    print('proof that the while loop is running while the sound is playing')
    time.sleep(0.1)
    playsound('siren.mp3', block=False)  # Please suggest another module, "playsound" stopped working and I gave up on fixing it.
