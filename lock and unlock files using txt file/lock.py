#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:12:21 2019

@author: vivanksharma
"""
import os
def lockFolder():
    os.system('clear')
    print('What folder would you like to lock? Please type a Directory!')
    lockInput = "~/Desktop/ftl/"
    text_file = open("lock.txt","r")
    lines = text_file.read().split('\n')
    text_file.close()
    for i in lines:
        os.system('clear;'+'chflags hidden ' + lockInput+i + ';clear')
    print('Folder Locked!')

secretPassword = 'vivank'


def unlockMain(folder_select,typedPassword):
    global exit
	
    os.system('clear')
    typedPasswordLow = typedPassword.lower()
    if typedPassword == secretPassword:
        os.system('clear;' + 'chflags nohidden ' + folder_select + ';clear')
        print('Folder Unlocked!')
        theExit()
    elif typedPasswordLow in alias['idiot'] and not secretPassword in alias['idiot']:
        os.system('clear')
        print(idiot)
        exit = True
    elif typedPasswordLow in alias['exit']:
        os.system('clear')
        print(exitSentence)
        exit = True
    elif typedPasswordLow == 'lock':
        os.system('clear')
        print(color['RED'] + 'You cannot use this command as the folder is already locked :/' + color['DEFAULT'])
    elif typedPasswordLow == 'clear':
        os.system('clear')
    elif typedPasswordLow in alias['info']:
        os.system('clear')
        print(noRun + '\nIf you would like to see credits, please type "cancel"!\nOtherwise, Please enter in password to unlock the folder!')
        unlockMain()
    elif typedPasswordLow in alias['cancel']:
        os.system('clear')
        print(header)
        Main()
    else:
        os.system("clear")
        print(incorrect + exitSentence)
        
        
        
        
def unlock():
    print('Please enter in password to unlock the folder!')
    typedPassword = input("Enter you password : ")
    lockInput = "~/Desktop/ftl/"
    text_file = open("lock.txt","r")
    lines = text_file.read().split('\n')
    text_file.close()
    for i in lines:
        os.system('clear;' + 'chflags nohidden ' + lockInput+i + ';clear')
        print('Folder Unlocked!')
    print("Unlock all files")
 # You can change this to whatever you like! Dont forget the space after it.

