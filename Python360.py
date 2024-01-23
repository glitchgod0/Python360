import sys
import os 
import binascii

print("Python360 Test by Glitchgod\n")

DEBUG = False


def ByteGrabber(ByteNum, ReadNum, PrintName): # this function is here because i dont wanna do basic math manually
	File.seek(ByteNum)
	EndCrop = ReadNum + ReadNum + 2
	Name = (repr(binascii.hexlify(File.read(ReadNum)))[2:EndCrop])
	print(PrintName, Name)


def STFSUTFHandler(seek, readbytes, Name, NameOut, PrintName):
	File.seek(seek)
	Name = File.read(readbytes)
	NameOut = Name.decode('utf-8')
	print(PrintName, NameOut)

def ConHandler():

	#TODO: look into the signature
	#"the signature is PKCS1 in big-endian format if you want to verify that
	# you verify the console certificate against microsoft's master key and then
	# verify the content signature against the console certificate's public key" - Emma

	print("\nCON Info:")
	File.seek(31)
	if File.read(1) == b'\x02':
		print("Retail")
	elif File.read(1) == b'\x01':
		print("Devkit")
	else:
		print("Unknown signing")

	ByteGrabber(4, 2, "Public Key Certificate Size:")
	ByteGrabber(6, 5, "Certificate Owner Console ID:")

	File.seek(11)
	CONCertOwnerConsolePart = (repr({File.read(11)})[3:14])
	print(f"Certificate Console Part: {CONCertOwnerConsolePart}")

	File.seek(32)
	CONCertGenerationDate = (repr({File.read(8)})[3:11])
	print(f"Certificate Generation Date: {CONCertGenerationDate}")


	ByteGrabber(40, 4, "Public Exponent:")
	ByteGrabber(44, 80, "Public Modulus")
	ByteGrabber(172, 100, "Certificate Signature")
	ByteGrabber(428, 80, "Signature:")

	STFSHandler()
	#answer = input("\nPrint Large info? [Y/N]: ")
	#if answer == "Y" or "y":



def STFSHandler():
	print("\nSTFS Info:")
	
	if DEBUG == True: #TODO: Replace with Arg
		ByteGrabber(556, 100, "Licensing Data:")
		ByteGrabber(812, 14, "Content ID/Header SHA1 Hash:")
		ByteGrabber(832, 14, "Entry ID")
		ContentTypeHandler() #Content Type
		ByteGrabber(840, 4, "Metadata Version:")
		ByteGrabber(844, 8, "Content Size")
		ByteGrabber(852, 4, "Media ID")
		ByteGrabber(856, 4, "Version:")
		ByteGrabber(860, 4, "Base Version:")
		ByteGrabber(864, 4, "Title ID:")
		ByteGrabber(868, 1, "Platfrom:")
		ByteGrabber(869, 1, "Executable Type:")
		ByteGrabber(870, 1, "Disc Number")
		ByteGrabber(871, 1, "Disc In Set:")
		ByteGrabber(872, 4, "Save Game ID:")
		ByteGrabber(876, 5, "Console ID:")
		ByteGrabber(881, 8, "Profile ID:")
		ByteGrabber(889, 1, "Volume Descriptor Size:")
		ByteGrabber(890, 24, "FIle System Volume Descriptor:")
		ByteGrabber(925, 4, "Data File Count:")
		ByteGrabber(929, 8, "Data File Combined Size:")
		ByteGrabber(937, 8, "Reserved:")
		ByteGrabber(945, 4, "Padding:")
		ByteGrabber(1021, 8, "Device ID:")
		STFSUTFHandler(1041, 80, "DisplayName", "DisplayNameOut", "Display Name:")
		STFSUTFHandler(3345, 300, "DescName", "DescNameOut", "Display Description:")
		STFSUTFHandler(5649, 80, "PublishName", "PublishNameOut", "Publisher Name:")
		STFSUTFHandler(5777, 80, "TitleName", "TitleNameOut", "Title Name:")
		ByteGrabber(5905, 4, "Transfer Flags:")
		ByteGrabber(5906, 8, "Thumbnail Image Size:")
		ByteGrabber(5910, 8, "Title Thumbnail Image Size:")
		ByteGrabber(5914, 0, "Thumbnail Image, 16384. Printing Not Ready")
		ByteGrabber(22298, 0, "Title Thumbnail 16384. Printing Not Ready")
	else:
		STFSUTFHandler(1041, 80, "DisplayName", "DisplayNameOut", "Display Name:")
		STFSUTFHandler(3345, 300, "DescName", "DescNameOut", "Display Description:")
		STFSUTFHandler(5777, 80, "TitleName", "TitleNameOut", "Title Name:")
		ByteGrabber(864, 4, "Title ID:")
		ContentTypeHandler()
		ByteGrabber(5905, 4, "Transfer Flags:")

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
			CheckLIVEOnly = False
			ConHandler()
		elif FileType == b'LIVE':
			print("LIVE File")
			CheckLIVEOnly = True
			STFSHandler()
		elif FileType == b'PIRS':
			print("PIRS File")
			CheckLIVEOnly = True
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
