import sys
import os 
import binascii

print("Python360 Test by Glitchgod\n")

DEBUG = False


def ConHandler():

	#TODO: look into the signature
	#"the signature is PKCS1 in big-endian format if you want to verify that
	# you verify the console certificate against microsoft's master key and then
	# verify the content signature against the console certificate's public key" - Emma

	LiveHandler()

	File.seek(31)
	if File.read(1) == b'\x02':
		print("Retail")
	elif File.read(1) == b'\x01':
		print("Devkit")
	else:
		print("Unknown signing")

	print("\nCertificate Info:")
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
	#answer = input("\nPrint Large info? [Y/N]: ")
	#if answer == "Y" or "y":
	File.seek(44)
	print(f"Public Modulus: {binascii.hexlify(File.read(80))}")
	File.seek(172)
	print(f"Certificate Signature: {binascii.hexlify(File.read(100))}")
	File.seek(428)
	print(f"Signature: {binascii.hexlify(File.read(80))}")


	#answer = input("\nPrint Large info? [Y/N]: ")
	#if answer == "Y" or "y":


def LiveHandler():
	File.seek(4)
	print(f"Package Signature: {binascii.hexlify(File.read(100))}")
	File.seek(843)
	print(f"Metadata Version: {binascii.hexlify(File.read(1))}")
	File.seek(836)
	ContentTypeHandler()

	File.seek(5777)
	TitleName = File.read(80)
	TitleNameOut = TitleName.decode('utf-8')
	print(f"Title Name: {TitleNameOut}")
	File.seek(1041)
	TitleName = File.read(80)
	TitleNameOut = TitleName.decode('utf-8')
	print(f"Display Name: {TitleNameOut}")
	#TODO: Option to read all locales

	File.seek(3345)
	TitleName = File.read(300)
	TitleNameOut = TitleName.decode('utf-8')
	print(f"Display Description: {TitleNameOut}")
	#TODO: Option to read all locales

	File.seek(864)
	print(f"Title ID: {binascii.hexlify(File.read(4))}")

	File.seek(5649)
	TitleName = File.read(80)
	TitleNameOut = TitleName.decode('utf-8')
	print(f"Publisher Name: {TitleNameOut}")

	File.seek(852)
	print(f"Media ID: {binascii.hexlify(File.read(4))}")

	File.seek(5905)
	print(f"Transfer Flag: {binascii.hexlify(File.read(1))}")

	if DEBUG == True:
		File.seek(556)
		print(f"\n[DEBUG] Licensing Data: {binascii.hexlify(File.read(8))}")
		File.seek(564)
		print(f"[DEBUG] Licensing Data: {binascii.hexlify(File.read(4))}")
		File.seek(568)
		print(f"[DEBUG] Licensing Data: {binascii.hexlify(File.read(4))}")
		File.seek(844)
		print(f"[DEBUG] Content Size: {binascii.hexlify(File.read(8))}")
	return


def ContentTypeHandler():
	ContentTypeMatch = binascii.hexlify(File.read(4))
	match ContentTypeMatch:
		case (b'00000001'):
			print("Content Type: Saved Game")
		case (b'00000002'):
			print("Content Type: Marketplace Content")
		case (b'00000003'):
			print("Content Type: Publisher")
		case (b'00001000'):
			print("Content Type: Xbox 360 Title")
		case (b'00002000'):
			print("Content Type: IPTV Pause Buffer")
		case (b'00004000'):
			print("Content Type: Installed Game")
		case (b'00005000'):
			print("Content Type: Xbox Original Game")
		case (b'00007000'):
			print("Content Type: Game on Demand")
		case (b'00009000'):
			print("Content Type: Avatar Item")
		case (b'00010000'):
			print("Content Type: Profile")
		case (b'00020000'):
			print("Content Type: Gamer Picture")
		case (b'00030000'):
			print("Content Type: Theme")
		case (b'00040000'):
			print("Content Type: Cache File")
		case (b'00050000'):
			print("Content Type: Storage Download")
		case (b'00060000'):
			print("Content Type: Xbox Saved Game")
		case (b'00070000'):
			print("Content Type: Xbox Download")
		case (b'00080000'):
			print("Content Type: Game Demo")
		case (b'00090000'):
			print("Content Type: Video")
		case (b'000A0000'):
			print("Content Type: Game Title")
		case (b'000B0000'):
			print("Content Type: Installer")
		case (b'000C0000'):
			print("Content Type: Game Trailer")
		case (b'000D0000'):
			print("Content Type: Arcade Title")
		case (b'000E0000'):
			print("Content Type: XNA")
		case (b'000F0000'):
			print("Content Type: License Store")
		case (b'01000000'):
			print("Content Type: Movie")
		case (b'02000000'):
			print("Content Type: TV")
		case (b'03000000'):
			print("Content Type: Music Video")
		case (b'04000000'):
			print("Content Type: Game Video")
		case (b'05000000'):
			print("Content Type: Podcast Video")
		case (b'06000000'):
			print("Content Type: Viral Video")
		case (b'20000000'):
			print("Content Type: Community Game")
	return

def XEXHandler():

	if DEBUG == False:
		print("XEX2 file support is very basic and not ready. Set DEBUG to True in the script to show the basic info.\n")

	if DEBUG == True:
		print("XEX File:")
		# First 4 bytes get ate. idk why
		File.seek(7)
		Flags = binascii.hexlify(File.read(1), b' ')  # Flags
		
		print("Parsed Data:")
		#make into a match case
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
			print(f"[DEBUG] File Path = {FilePath}") #print FilePath

		File = open(FilePath, "rb+") #Open File
		FileType = File.read(4) #Read the first 4 bytes

		if DEBUG == True:
			print(f"[DEBUG] File Type: {FileType}\n") #print file type

		if FileType == b'CON ':
			print("CON File:")
			ConHandler()
		elif FileType == b'LIVE':
			print("LIVE File:")
			LiveHandler()
		elif FileType == b'XEX2':
			XEXHandler()
		else:
			print("Not Recognized")

		File.close()	
	else:
		print("Invalid file path given")
else:
	print("No file path argument given.")
