import os
print("Current folder:", os.getcwd())
print("Files in current directory:", os.listdir())

from datetime import datetime
import time
import pygame

pygame.mixer.init()

alarm_time = input("Set the alarm time (HH:MM): ")
while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Wake up!")
        
        pygame.mixer.music.load("alarm-301729.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break
    time.sleep(1)    