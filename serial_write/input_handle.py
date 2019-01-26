import serial
import pygame
import time

for i in range(4):
    message = serial.Serial('/dev/tty.usbmodem336837523037')
    sentMessage = message.read(1)
    if str(sentMessage) == "b'A'":
        print("play sound 1")
        pygame.init()
        pygame.mixer.music.load("cry.mp3")
        pygame.mixer.music.play()
        time.sleep(3)
    elif str(sentMessage) == "b'B'":
        print("play sound 2")
        pygame.mixer.music.load("water.mp3")
        pygame.mixer.music.play()
        time.sleep(3)
    elif str(sentMessage) == "b'C'":
        print("play sound 3")
        pygame.mixer.music.load("bubble.mp3")
        pygame.mixer.music.play()
        time.sleep(3)
    elif str(sentMessage) == "b'D'":
        print("play sound 4")
        pygame.mixer.music.load("bell.mp3")
        pygame.mixer.music.play()
        time.sleep(3)
    else:
        print("Message: " + str(sentMessage))