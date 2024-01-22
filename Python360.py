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
	print("LIVE handling not ready!")

def XEXHandler():
	print("XEX Header:")

	# First 4 bytes get ate. idk why
	File.seek(7)
	Flags = binascii.hexlify(File.read(1), b' ')  # Flags
	File.seek(8)
	print(f"{binascii.hexlify(File.read(4), b' ')} PE Data Offset") # PE Data Offset
	File.seek(12)
	print(f"{binascii.hexlify(File.read(4), b' ')} Reserved") # Reserved
	File.seek(16)
	print(f"{binascii.hexlify(File.read(4), b' ')} Security Info Offset") # Security Info Offset
	File.seek(23)
	OptionalHeaderCount = binascii.hexlify(File.read(1), b' ')
	File.seek(24)
	print(f"{binascii.hexlify(File.read(4), b' ')}")
	File.seek(28)
	print(f"{binascii.hexlify(File.read(4), b' ')}")

	print("Properly Parsed Data:")

	if Flags == b'00':
		print("Title Module")
	elif Flags == b'01':
		print("Exports To Title")
	elif Flags == b'02':
		print("System Debugger")
	elif Flags == b'03':
		print("DLL Module")
	elif Flags == b'04':
		print("Module Patch")
	elif Flags == b'05':
		print("Patch Full")
	elif Flags == b'06':
		print("Patch Delta")
	elif Flags == b'07':
		print("User Mode")
	else:
		print("Unknown Flag")

	print(f"Optional Header Count: {OptionalHeaderCount}")





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
