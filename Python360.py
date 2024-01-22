import sys
import os 
import binascii

print("Python360 Test by Glitchgod")

DEBUG = True


def ConHandler():
	File.seek(31)
	if File.read(1) == b'\x02':
		print("02 Retail")
	elif File.read(1) == b'\x01':
		print("01 Devkit")
	else:
		print("Unknown signing")

def LiveHandler():
	print("LIVE/PIRS handling not ready!")

def XEXHandler():
	print("XEX Header")
	File.seek(4)
	print(File.read(4))
	File.seek(8)
	print(File.read(4))
	File.seek(12)
	print(File.read(4))
	File.seek(16)
	print(File.read(4))
	File.seek(20)
	print(File.read(4))
	File.seek(24)
	print(File.read(4))



if len(sys.argv) != 1: #Check if theres arguments
	FilePath = sys.argv[1] #set FilePath to Argument
	if os.path.exists(FilePath): #Check if FilePath is actually a valid path
		if DEBUG == True:
			print(f"[DEBUG] File Path = {FilePath}") #print FilePath

		File = open(FilePath, "rb+") #Open File
		FileType = File.read(4) #Read the first 4 bytes

		if DEBUG == True:
			print(f"[DEBUG] File Type: {FileType}") #print file type

			if FileType == b'CON ':
				print("CON File")
				ConHandler()
			elif FileType == b'LIVE':
				print("LIVE File")
				LIVE = True
				LiveHandler()
			elif FileType == b'XEX2':
				print("XEX File")
				XEX2 = True
				XEXHandler()
			else:
				print("Not Recognized")



		File.close()	
else:
	print("No file path argument given.")
