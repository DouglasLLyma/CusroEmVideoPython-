#Faça um programa em Python que abra e reproduza
#o áudio de um asrquivo mp3.
import pygame 
pygame.mixer.init()
pygame.mixer.music.load('Matanza.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()