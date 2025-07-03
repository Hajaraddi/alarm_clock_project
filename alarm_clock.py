from datetime import datetime,timedelta
import time
import pygame
 
#Initialize pygame
pygame.mixer.init()

# Set the alarm time(daily)
alarm_time = input("Set the alarm time (HH:MM): ")
snooze_minutes = 5

print(f"Alarm set for {alarm_time}, waiting...")

# print("Current folder:", os.getcwd())
# print("Files in current directory:", os.listdir())

# print(f"Alarm is set for ")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Wake up!")
        pygame.mixer.music.load("alarm-301729.mp3")
        pygame.mixer.music.play()
        
        # wait while for playing
        
        while pygame.mixer.music.get_busy():
            time.sleep(1)
 
        # Ask for snooze

        choice = input("Do you want to snooze? (s = snooze, any other key to skip): ").strip().lower()
        if choice == 's':
            # Wait for 5 minutes
            snooze_until = (datetime.now() + timedelta(minutes=snooze_minutes)).strftime("%H:%M")
            print(f"Soozed until {snooze_until}")
            while True:
                now = datetime.now().strftime("%H:%M")
                if now == snooze_until:
                    print("Snooze Alarm!")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)
                    break
                    time.sleep(1)

        print("Alarm done. Waiting for next day...")       

        # Wait until next day to repeat alarm
        while datetime.now().strftime("%H:%M") == alarm_time:
            time.sleep(10)
    time.sleep(5)       
