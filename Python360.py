import sys
import os 

print("Python360 Test by Glitchgod")

DEBUG = True

if len(sys.argv) != 1: #Check if theres arguments
	FilePath = sys.argv[1] #set FilePath to Argument
	if os.path.exists(FilePath): #Check if FilePath is actually a valid path
		if DEBUG == True:
			print(f"[DEBUG] File Path = {FilePath}") #print FilePath

		File = open(FilePath, "rb+") #Open File
		FileType = File.read(4) #Read the first 4 bytes
		FileType=str(FileType, 'utf-8') #removes the b from the start of the string

		if DEBUG == True:
			print(f"[DEBUG] File Type: {FileType}") #print file type

			if FileType == "CON ":
				print("CON File")
				CON = True
			elif FileType == "LIVE":
				print("LIVE File")
				LIVE = True
			elif FileType == "XEX2":
				print("XEX File")
				XEX2 = True
			else:
				print("Not Recognized")

		if CON == True:
			File.seek(31)
			File.read(1)

		File.close()	
else:
	print("No file path argument given.")
