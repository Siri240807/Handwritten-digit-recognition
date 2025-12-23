import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

WINDOWSZEx = 640
WINDOWSIZEy = 480

BOUNDARYINC = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False
MODEL = load_model("Model.h5")

LABELS = {0: "Zero",
          1: "One",
          2: "Two",
          3: "Three",
          4: "Four",
          5: "Five",
          6: "Six",
          7: "Seven",
          8: "Eight",
          9: "Nine"}

pygame.init()

FONT = pygame.font.SysFont("freesansbold.ttf", 18)

DISPLAYSURF = pygame.display.set_mode((WINDOWSZEx, WINDOWSIZEy))

pygame.display.set_caption("Digit Board")

iswriting = False
numberxcord = []
numberycord = []

img_cnt = 0

PREDICT = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 10, 0)
            
            numberxcord.append(xcord)
            numberycord.append(ycord)
            
        if event.type == MOUSEBUTTONDOWN:
            iswriting = True
            
        if event.type == MOUSEBUTTONUP:
            iswriting = False
            if not numberxcord:
                continue
            numberxcord = sorted(numberxcord)
            numberycord = sorted(numberycord)
            
            rect_min_x, rect_max_x = max(numberxcord[0] - BOUNDARYINC, 0), min(WINDOWSZEx, numberxcord[-1]+BOUNDARYINC)
            
            rect_min_y, rect_max_y = max(numberycord[0] - BOUNDARYINC, 0), min(numberycord[-1]+BOUNDARYINC, WINDOWSIZEy)
            
            numberxcord = []
            numberycord = []
            
            # Extract image data properly from surface
            img_arr = pygame.surfarray.array3d(DISPLAYSURF)[rect_min_x:rect_max_x, rect_min_y:rect_max_y]
            img_arr = np.transpose(img_arr, (1, 0, 2))
            img_arr = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
            
            pygame.draw.rect(DISPLAYSURF, RED, (rect_min_x, rect_min_y, rect_max_x - rect_min_x, rect_max_y - rect_min_y), 2)
            
            if IMAGESAVE:
                cv2.imwrite("image.png", img_arr)
                img_cnt += 1
                
            if PREDICT:
                # Resize preserving aspect ratio (fit to 20x20 box)
                image = img_arr
                rows, cols = image.shape
                if rows > cols:
                    factor = 20.0 / rows
                    rows = 20
                    cols = int(round(cols * factor))
                else:
                    factor = 20.0 / cols
                    cols = 20
                    rows = int(round(rows * factor))
                image = cv2.resize(image, (cols, rows), interpolation=cv2.INTER_AREA)
                
                # Pad to 28x28 (centering the image)
                colsPadding = (int(np.ceil((28 - cols) / 2.0)), int(np.floor((28 - cols) / 2.0)))
                rowsPadding = (int(np.ceil((28 - rows) / 2.0)), int(np.floor((28 - rows) / 2.0)))
                image = np.pad(image, (rowsPadding, colsPadding), 'constant')
                
                # Normalize to 0-1 range
                image = image.astype('float32') / 255.0
                
                label = str(LABELS[np.argmax(MODEL.predict(image.reshape(1, 28, 28, 1)))])
                
                textSurface = FONT.render(label, True, RED, WHITE)
                textRecObj = textSurface.get_rect()
                textRecObj.left, textRecObj.bottom = rect_min_x, rect_max_y
                
                DISPLAYSURF.blit(textSurface, textRecObj)
                
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURF.fill(BLACK)
      
    pygame.display.update()             
    
                
                

                
                        
            
            