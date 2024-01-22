import sys
import os 
import binascii

print("Python360 Test by Glitchgod\n")

DEBUG = False


def ConHandler():
	File.seek(31)
	if File.read(1) == b'\x02':
		print("Retail")
	elif File.read(1) == b'\x01':
		print("Devkit")
	else:
		print("Unknown signing")

	print("\nCertificate Info:\n")
	File.seek(4)
	print(f"Public Key Certificate Size: {binascii.hexlify(File.read(2))}") 
	File.seek(6)
	print(f"Certificate Owner Console ID: {binascii.hexlify(File.read(5))}")
	File.seek(11)
	print(f"Certificate Owner Console Part Number: {File.read(11)}")
	File.seek(32)
	print(f"Certificate Date of Generation: {File.read(8)}")


	if DEBUG == True:
		print("\n[DEBUG CON OUT]")
		File.seek(4)
		print(f"[DEBUG] {binascii.hexlify(File.read(2), b' ')} Public Key Certificate Size") 
		File.seek(6)
		print(f"[DEBUG] {binascii.hexlify(File.read(5), b' ')} Certificate Owner Console ID")
		File.seek(11)
		print(f"[DEBUG] {binascii.hexlify(File.read(14), b' ')} Certificate Owner Console Part Number")
		File.seek(31)
		print(f"[DEBUG] {binascii.hexlify(File.read(1), b' ')} Console Type")
		File.seek(32)
		print(f"[DEBUG] {binascii.hexlify(File.read(8), b' ')} Certificate Date of Generation")
		File.seek(40)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} Public Exponent")
		File.seek(44)
		print(f"[DEBUG] {binascii.hexlify(File.read(80), b' ')} Public Modulus")
		File.seek(172)
		print(f"[DEBUG] {binascii.hexlify(File.read(100), b' ')} Certificate Signature")
		File.seek(428)
		print(f"[DEBUG] {binascii.hexlify(File.read(80), b' ')} Signature")

def LiveHandler():
	print("LIVE handling not ready!")

def XEXHandler():
	print("XEX Header:")

	
	# First 4 bytes get ate. idk why
	File.seek(7)
	Flags = binascii.hexlify(File.read(1), b' ')  # Flags
	if DEBUG == True:
		File.seek(8)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} PE Data Offset") # PE Data Offset
		File.seek(12)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} Reserved") # Reserved
		File.seek(16)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} Security Info Offset") # Security Info Offset
		File.seek(23)
		OptionalHeaderCount = binascii.hexlify(File.read(1), b' ')
		print(f"[DEBUG] {OptionalHeaderCount}")
		File.seek(24)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")
		File.seek(28)
		print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")

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





if len(sys.argv) != 1: #Check if theres arguments
	FilePath = sys.argv[1] #set FilePath to Argument
	if os.path.exists(FilePath): #Check if FilePath is actually a valid path
		if DEBUG == True:
			print(f"\n[DEBUG] File Path = {FilePath}") #print FilePath

		File = open(FilePath, "rb+") #Open File
		FileType = File.read(4) #Read the first 4 bytes

		if DEBUG == True:
			print(f"[DEBUG] File Type: {FileType}\n") #print file type

		if FileType == b'CON ':
			print("CON File:")
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
