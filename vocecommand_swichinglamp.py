import pygame
import speech_recognition as sr

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Voice Command Test")

recognizer = sr.Recognizer()

def control_device(command):
    if "light on" in command:
        screen.fill((255, 255, 0)) 
        pygame.display.update()
        print("Light turned ON")
    elif "light off" in command:
        screen.fill((0, 0, 128))  
        pygame.display.update()
        print("Light turned OFF")
    else:
        print("Command not recognized.")

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print(f"User said: {command}")
    control_device(command)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand.")
except sr.RequestError:
    print("Failed to connect to the recognition service.")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()