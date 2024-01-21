import sys
import os 

print("Python360 Test by Glitchgod")

if len(sys.argv) != 1: #Check if theres arguments
	FilePath = sys.argv[1] #set FilePath to Argument
	if os.path.exists(FilePath): #Check if FilePath is actually a valid path
		print(f"File Path = {FilePath}") #print FilePath
		file = open(FilePath, "rb+") #Open File
		filetype = file.read(4) #Read the first 4 bytes
		filetype=str(filetype, 'utf-8') #removes the b from the start of the string
		print(f"File Type: {filetype}") #print file type
		file.close()	
else:
	print("No file path argument given.")
