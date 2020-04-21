import pygame, time
pygame.init()
sound = pygame.mixer.Sound("F:\\MAJOR 2\\Drowsiness_detection\\wrong_move.wav")
sound.play()
pygame.time.wait(10000) # You won't need this line if your programme does not end here!

pygame.quit()
