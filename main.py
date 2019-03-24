
import readline # arrow keys
import os # This imports your OS.
from loginmail import login_mailfunc
from mail import un_mailfunc
import pyrebase

i=0
config = {
    "apiKey": "AIzaSyCk-zz4Tm9YYxyhX2C4NGTpbNO-zFDplkk",
    "authDomain": "pythonlock-e5319.firebaseapp.com",
    "databaseURL": "https://pythonlock-e5319.firebaseio.com",
    "projectId": "pythonlock-e5319",
    "storageBucket": "pythonlock-e5319.appspot.com",
    "messagingSenderId": "97710168175"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()


color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'PURPLE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
    'TWITTER_BLUE'            : '\033[38;5;33m',
}
alias = {
	'idiot' : ["password", "12345", "synthx", "qwerty"],
	'help'  : ["help", "?", "/help"],
	'exit'  : ["exit", "quit", "stop"],
	'info'  : ["info", "credits"],
	'cancel': ["cancel", "return", "back"]
}
incorrect = 'Wrong password! ' # You can change this to say whatever you like!
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] +'Folder Locker\n'
exit = False
idiot = 'You must be a idiot, you really think I would set that as my password? -_-\n' + exitSentence # You can change this to say whatever you like!
noRun = 'You are not allowed to enter that command here!'
credits = '©2019 Vivank\n' + ' Mansi'
os.system("clear") # This will clear the screen for a nice and clean interface!
 # make sure this file is in same directory that you are running this script from.
 # make sure this file is in same directory that you are running this script from.
secretPassword = "vivank"

user = ['vivank','mansi']
pwd = ['','']
header = color['RED'] + '''
          _____     _     _             _               _
         |  ___|__ | | __| | ___ _ __  | |    ___   ___| | _____ _ __
         | |_ / _ \| |/ _` |/ _ \ '__| | |   / _ \ / __| |/ / _ \ '__|
         |  _| (_) | | (_| |  __/ |    | |__| (_) | (__|   <  __/ |
         |_|  \___/|_|\__,_|\___|_|    |_____\___/ \___|_|\_\___|_|

''' + color['DEFAULT'] + '''                        +-----------------------+\n                        |  Created by ''' + color['TWITTER_BLUE'] + '''AccessDenied''' + color['DEFAULT'] + '''  |\n                        +-----------------------+
''' + color['DEFAULT']
print(header + 'Type "help" to begin!\n')
def Main():
    global exit
    user = input("Enter User Id : ")
    password = input("Enter you password : ")
    
    a = db.child("user").child(user).get()
    
    if(password == a.val()):
        login_mailfunc(user)
        maininput = input(color['TWITTER_BLUE'] + 'Folder Locker> ' + color['DEFAULT']).lower() # You can change this to whatever you like! Dont forget the space after it.
    while not maininput:
        maininput = input(color['TWITTER_BLUE'] + 'Folder Locker> ' + color['DEFAULT']).lower() # You can change this to whatever you like! Dont forget the space after it.
    if maininput in alias['help']:
        helpme()
    elif maininput == 'unlock':
        unlockst()
    elif maininput == 'lock':
        lockFolder()
    elif maininput in alias['exit']:
        os.system('clear')
        print(exitSentence)
        exit = True
    elif maininput == 'clear':
        os.system('clear')
        print(header)
        Main()
    elif maininput in alias['info']:
        os.system('clear')
        print(credits)
        Main()
    elif maininput in alias['cancel']:
        os.system('clear')
        print(header + '\n' + color['RED'] + noRun + color['DEFAULT'] + '\nThis command is only valid when trying to unlock a folder!')
        Main()
    else:
        print(color['RED'] + '[ERROR] COMMAND "' + maininput + '" NOT FOUND\n' + color['DEFAULT'] + 'PLEASE USE A PROPER COMMAND!\n')
    
	
def helpme():
	global exit
	os.system('clear')
	print(color['YELLOW'] + '''
+--------+-------------------------------------+
| help   |  shows this dialog                  |
+--------+-------------------------------------+
| unlock |  lets you unlock a specified folder |
+--------+-------------------------------------+
| lock   |  lets you lock a specified folder   |
+--------+-------------------------------------+
| exit   |  exits folder locker :/             |
+--------+-------------------------------------+
| clear  |  clears the screen                  |
+--------+-------------------------------------+
| info   |  shows credits for folder locker    |
+--------+-------------------------------------+
	''')
	Main()
def unlockst():
	os.system('clear')
	print(header + 'What folder would you like to unlock? Please type a Directory!')
	folderSelect = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	if "help" in folderSelect.lower() or "unlock" in folderSelect.lower() or "lock" in folderSelect.lower() or "exit" in folderSelect.lower() or "clear" in folderSelect.lower() or "info" in folderSelect.lower():
		unlockst()
	else:
		unlockMain(folderSelect)



def unlockMain(folder_select):
	global exit
	
	os.system('clear')
	print(header + 'Please enter in password to unlock the folder!')
	typedPassword = input(color['TWITTER_BLUE'] + "Folder Locker> " + color['DEFAULT']) # You can change this to whatever you like! Dont forget the space after it.
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
		un_mailfunc()
		
		
			
def lockFolder():
	os.system('clear')
	print(header + 'What folder would you like to lock? Please type a Directory!')
	lockInput = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	os.system('clear;' + 'chflags hidden ' + lockInput + ';clear')
	print('Folder Locked!')
	theExit()
def theExit():
	global exit
	print(header + 'Would you like to exit Folder Locker? Yes/no or Y/n')
	exitInput = input(color['TWITTER_BLUE'] + "Folder Locker> " + color['DEFAULT'])
	if "yes" in exitInput.lower() or "y" in exitInput.lower():
		os.system('clear')
		print(exitSentence)
		exit = True
	elif "no" in exitInput.lower() or "n" in exitInput.lower():
		os.system('clear')
		print(header + 'Please type "help" to begin!')
		Main()
	elif exitInput.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	else:
		os.system('clear')
		print('You may only say yes or no!')
		theExit()
while exit == False:
    Main()