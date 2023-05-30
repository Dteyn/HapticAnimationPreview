# Simple Python script to preview the Haptic Animations from OpenVRChatHapticFeedback
# See https://github.com/alextrof94/OpenVRChatHapticFeedback/ for more details

import os
import json

# HapticAnimations file path
file_path = 'HapticAnimations.json'

# Load the JSON data
if os.path.isfile(file_path):
    with open(file_path) as file:
        haptic_data = json.load(file)
else:
    print(f"ERROR: {file_path} not found. Please move {file_path} to the script folder.")
    exit()
      
# Create a list of haptic animations
animations = haptic_data

import pygame

# Initialize pygame
pygame.mixer.init()

# Load sound effect
sound_effect = pygame.mixer.Sound('vibration.wav')

# Play the haptic animation
def play_haptic_animation(animation):
    for frame in animation['hapticFrames']:
        sound_effect.play()
        pygame.time.wait(frame['duration'])
        sound_effect.stop()
        pygame.time.wait(frame['delayAfterPlay'])

# Print the menu
def print_menu():
    print("Haptic Animations:")
    for index, animation in enumerate(animations):
        print(f"{index + 1}. {animation['name']}")
    print("q. Quit")

# Main program loop
while True:
    print_menu()
    choice = input("Select an animation (1-{}), or 'q' to quit: ".format(len(animations)))
    
    if choice == 'q':
        break

    try:
        index = int(choice) - 1
        animation = animations[index]
        play_haptic_animation(animation)
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
