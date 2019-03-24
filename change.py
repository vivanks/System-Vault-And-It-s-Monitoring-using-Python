import os

cd = os.getcwd()

path = cd

early_version = []


files = []

def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))



while 1:
	for root, dirs, filenames in os.walk(path):
		for f in filenames:

			files.append(os.path.relpath(os.path.join(root, f), path))

			print(Diff(early_version,files))


			early_version.append(os.path.relpath(os.path.join(root, f), path))

	print(files)
	


