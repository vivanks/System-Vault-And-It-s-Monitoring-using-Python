# System to Track/Lock Resources and Session
 
## Base Variant
System supports tracking/locking of resources like *Files, Folders, Image Files, Commands, any/all kind of files stored in folders*. 
The basic variant of the system features a folder locking system. The barebone library of python, OS was used to accompalish this:

1.  *Log in System*:  
The users can login with username and password. For each attempt to log-in, an 			 email will be sent to the administrator. 
The mailing system is made using SMTP. 
While exiting the system, the file will be made inaccessible by other means, including OS commands.

2. *Monitoring Edits*: The file-walk commands are used to keep a detailed log of all edits made and are sent to the administrator via email. All other forms of logging online/offline are being avoided for security reasons. 
After every attempt, cache is being cleared such that nobody can access the directory and find ways to log-in.

4. *Securing System with sha256*:  Unlike most other third party locking systems, our system uses the sha256 encryption algorithm, by firebase to ensure security.

## Remote Access

The use case of files being accessed using a local host server is considered. 
A Raspberry Pi 3B, loaded with Pixel-Raspbian OS was used for demonstration purpose.
Our whole system is built using python. By changing administrator settings, it is possible to open the terminal before the Raspberry Pi boots completely. 
Here is where the python script will be run. Since the script is being run at the time  of booting, the file locking and logging system turns effective and users can securely access/store their data.
 
## Monitoring Edits in files
The first base variant keeps a log of edits made in storage of files in the folder. As an additional feature, modules have also been made to log edits made in text files. file explorer is accessible using the button in left corner of the navigation

## Email Methods

 1. When user logs in :
 ![User log in](https://github.com/vivanks/S-Locker-using-Python/raw/master/readmeimg/1.jpeg)
 2. When user enters wrong password to access file :
 ![Wrong password](https://github.com/vivanks/S-Locker-using-Python/raw/master/readmeimg/4.jpeg)
 3. When user adds new file :
 ![When user add new file](https://github.com/vivanks/S-Locker-using-Python/raw/master/readmeimg/2.jpeg)
 4. When user remove an existing file :
 ![When user delete file](https://github.com/vivanks/S-Locker-using-Python/raw/master/readmeimg/3.jpeg)

