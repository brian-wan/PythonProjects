import time
import datetime
import subprocess

timeLeft = int(input('How long do you want to time for: '))
while timeLeft > 0:
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'alarm.wav'])
