import time
import os

Trumpets_Still_L = pygame.image.load(os.path.join(".\resources", "\images", "\special effects", "TrumpetsForFanFare - Left.png"))
Trumpets_Still_R = pygame.image.load(os.path.join(".\resources", "\images", "\special effects", "TrumpetsForFanFare - Right.png"))
Trumpets_Moved_L = pygame.image.load(os.path.join(".\resources", "\images", "\special effects", "TrumpetsForFanFare Moved - Left.png"))
Trumpets_Moved_R = pygame.image.load(os.path.join(".\resources", "\images", "\special effects", "TrumpetsForFanFare Moved - Right.png"))
Trumpet_Song = pygame.mixer.Sound(os.path.join(".\resources", "\images", "\special effects", "ClippedTrumpet.mp3"))
y = -85
jumped = True


while jumped:
     while y != 1:
         screen.blit(Trumpets_Still_L, (0,y))
         screen.blit(Trumpets_Still_R, (400,y))
         time.sleep(.02)
         pygame.display.update()
         y += 1
    
     start_time = time.time()
     duration = 5
     pygame.Sound.play(Trumpet_Song)

     while time.time() - start_time < duration:
         screen.blit(Trumpets_Moved_L, (0,y))
         screen.blit(Trumpets_Moved_R, (400,y))
         time.sleep(.1)
         pygame.display.update()
         screen.fill((0,0,0))
         screen.blit(Trumpets_Still_L, (0,y))
         screen.blit(Trumpets_Still_R, (400,y))
         time.sleep(.1)
         pygame.display.update()
        
     while y != -86:
         screen.fill((0,0,0))
         screen.blit(Trumpets_Still_L, (0,y))
         screen.blit(Trumpets_Still_R, (400,y))
         time.sleep(.02)
         pygame.display.update()
         y -= 1
     jumped = False