# Faça um programa em python que abre e reproduza
# o áudio de um arquivo MP3. 
import pygame 
pygame.mixer.init()
pygame.mixer.music.load('Matanza.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()