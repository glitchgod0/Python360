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

	File.seek(4)
	CONPublicKeyCertSize = (repr(binascii.hexlify(File.read(2)))[2:][:4])
	File.seek(6)
	CONCertOwnerConsoleID = (repr(binascii.hexlify(File.read(5)))[2:][:10])
	File.seek(11)
	CONCertOwnerConsolePart = (repr({File.read(11)})[3:14])
	File.seek(32)
	CONCertGenerationDate = (repr({File.read(8)})[3:11])
	File.seek(40)
	CONPublicExpo = (repr(binascii.hexlify(File.read(4)))[2:][:8])
	File.seek(44)
	CONPublicModu = (repr(binascii.hexlify(File.read(80)))[2:][:160])
	File.seek(172)
	CONCertSig = (repr(binascii.hexlify(File.read(100)))[2:][:200])
	File.seek(428)
	CONSignature = (repr(binascii.hexlify(File.read(80)))[2:][:160])

	print("\nCON Info:")
	File.seek(31)
	if File.read(1) == b'\x02':
		print("Retail")
	elif File.read(1) == b'\x01':
		print("Devkit")
	else:
		print("Unknown signing")

	print(f"Public Key Certificate Size: {CONPublicKeyCertSize}")
	print(f"Certificate Owner Console ID: {CONCertOwnerConsoleID}")
	print(f"Certificate Owner Console Part: {CONCertOwnerConsolePart}")
	print(f"Certificate Owner Console Date: {CONCertGenerationDate}")
	print(f"Public Exponent: {CONPublicExpo}")
	print(f"Public Modulus: {CONPublicModu}")
	print(f"Certificate Signature: {CONCertSig}")
	print(f"Signature: {CONSignature}")

	STFSHandler()
	#answer = input("\nPrint Large info? [Y/N]: ")
	#if answer == "Y" or "y":


def STFSUTFHandler(seek, readbytes, Name, NameOut, PrintName):
	File.seek(seek)
	Name = File.read(readbytes)
	NameOut = Name.decode('utf-8')
	print(PrintName, NameOut)

def STFSHandler():
	print("\nSTFS Info:")

	File.seek(4)
	PackageSignature = (repr(binascii.hexlify(File.read(100)))[2:202])

	File.seek(843)
	MetadataVer = (repr(binascii.hexlify(File.read(1)))[2:4])

	STFSUTFHandler(5777, 80, "TitleName", "TitleNameOut", "Title Name:")

	STFSUTFHandler(1041, 80, "DisplayName", "DisplayNameOut", "Display Name:")

	STFSUTFHandler(3345, 300, "DescName", "DescNameOut", "Display Description:")

	STFSUTFHandler(5649, 80, "PublishName", "PublishNameOut", "Publisher Name:")

	ContentTypeHandler()
	File.seek(864)
	TitleID = (repr(binascii.hexlify(File.read(4)))[2:10])

	File.seek(852)
	MediaID = (repr(binascii.hexlify(File.read(4)))[2:10])

	File.seek(5905)
	TransferFlags = (repr(binascii.hexlify(File.read(1)))[2:4])

	print(f"Metadata Version: {MetadataVer}")
	print(f"Media ID: {MediaID}")
	print(f"Transfer Flag: {TransferFlags}")
	print(f"Package Signature: {PackageSignature}")

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
	File.seek(836)
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
			print("CON File")
			ConHandler()
		elif FileType == b'LIVE':
			print("LIVE File")
			STFSHandler()
		elif FileType == b'PIRS':
			print("PIRS File")
			STFSHandler()
		elif FileType == b'XEX2 File':
			XEXHandler()
		else:
			print("Not Recognized")

		File.close()	
	else:
		print("Invalid file path given")
else:
	print("No file path argument given.")
