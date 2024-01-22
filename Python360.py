import sys
import os 
import binascii

print("Python360 Test by Glitchgod\n")

DEBUG = True


def ConHandler():

	#TODO: look into the signature
	#"the signature is PKCS1 in big-endian format if you want to verify that
	# you verify the console certificate against microsoft's master key and then
	# verify the content signature against the console certificate's public key" - Emma

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
	File.seek(40)
	print(f"Public Exponent: {binascii.hexlify(File.read(4))}")

	answer = input("\nPrint Large info? [Y/N]: ")
	if answer == "Y" or "y":
		File.seek(44)
		print(f"Public Modulus: {binascii.hexlify(File.read(80))}")
		File.seek(172)
		print(f"Certificate Signature: {binascii.hexlify(File.read(100))}")
		File.seek(428)
		print(f"Signature: {binascii.hexlify(File.read(80))}")



def LiveHandler():
	File.seek(4)
	print(f"Package Signature: {binascii.hexlify(File.read(100))}")
	File.seek(843)
	print(f"Metadata Version: {binascii.hexlify(File.read(1))}")
	File.seek(836)
	ContentTypeHandler()

	File.seek(556)
	
	if DEBUG == True:
		print(f"[DEBUG]Licensing Data: {binascii.hexlify(File.read(100))}")

def ContentTypeHandler():
	ContentTypeMatch = binascii.hexlify(File.read(4))
	match ContentTypeMatch:
		case (b'00000001'):
			print("Saved Game")
		case (b'00000002'):
			print("Marketplace Content")
		case (b'00000003'):
			print("Publisher")
		case (b'00001000'):
			print("Xbox 360 Title")
		case (b'00002000'):
			print("IPTV Pause Buffer")
		case (b'00004000'):
			print("Installed Game")
		case (b'00005000'):
			print("Xbox Original Game")
		case (b'00007000'):
			print("Game on Demand")
		case (b'00009000'):
			print("Avatar Item")
		case (b'00010000'):
			print("Profile")
		case (b'00020000'):
			print("Gamer Picture")
		case (b'00030000'):
			print("Theme")
		case (b'00040000'):
			print("Cache File")
		case (b'00050000'):
			print("Storage Download")
		case (b'00060000'):
			print("Xbox Saved Game")
		case (b'00070000'):
			print("Xbox Download")
		case (b'00080000'):
			print("Game Demo")
		case (b'00090000'):
			print("Video")
		case (b'000A0000'):
			print("Game Title")
		case (b'000B0000'):
			print("Installer")
		case (b'000C0000'):
			print("Game Trailer")
		case (b'000D0000'):
			print("Arcade Title")
		case (b'000E0000'):
			print("XNA")
		case (b'000F0000'):
			print("License Store")
		case (b'01000000'):
			print("Movie")
		case (b'02000000'):
			print("TV")
		case (b'03000000'):
			print("Music Video")
		case (b'04000000'):
			print("Game Video")
		case (b'05000000'):
			print("Podcast Video")
		case (b'06000000'):
			print("Viral Video")
		case (b'20000000'):
			print("Community Game")
	return

def XEXHandler():
	# First 4 bytes get ate. idk why
	File.seek(7)
	Flags = binascii.hexlify(File.read(1), b' ')  # Flags
	
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

	if DEBUG == True:
			File.seek(8)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} PE Data Offset") # PE Data Offset
			File.seek(12)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} Reserved") # Reserved
			File.seek(16)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')} Security Info Offset") # Security Info Offset
			File.seek(23)
			OptionalHeaderCount = binascii.hexlify(File.read(1), b' ')
			print(f"[DEBUG] Header Count: {OptionalHeaderCount}")
			File.seek(24)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")
			File.seek(28)
			print(f"[DEBUG] {binascii.hexlify(File.read(8), b' ')}")
			File.seek(36)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")
			File.seek(40)
			print(f"[DEBUG] {binascii.hexlify(File.read(8), b' ')}")
			File.seek(48)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")
			File.seek(52)
			print(f"[DEBUG] {binascii.hexlify(File.read(8), b' ')}")
			File.seek(60)
			print(f"[DEBUG] {binascii.hexlify(File.read(4), b' ')}")
			File.seek(64)
			print(f"[DEBUG] {binascii.hexlify(File.read(8), b' ')}")




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
			print("LIVE File:")
			LIVE = True
			LiveHandler()
		elif FileType == b'XEX2':
			print("XEX File:")
			XEX2 = True
			XEXHandler()
		else:
			print("Not Recognized")

		File.close()	
else:
	print("No file path argument given.")
