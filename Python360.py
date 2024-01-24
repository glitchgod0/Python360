import sys
import os 
import binascii

print("Python360 Test by Glitchgod\n")

DEBUG = False
PrintAll = False

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
	
	if ArgType == "-a":
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

def HeaderIDHandler(LookAt):
	print("HeaderIDHandler being redone")
#	LookUpValue = 
#	match TypeDataStruct[LookAt]:
#		case ('000002ff'):
#			print("Resource Info:")
#		case ('000003ff'):
#			print("Base File Format:")
#		case ('00000405'):
#			print("Base Reference:")
#		case ('000005ff'):
#			print("Delta Patch Descriptor:")
#		case ('000080ff'):
#			print("Bounding Path:")
#		case ('00008105'):
#			print("Device ID:")
#		case ('00010001'):
#			print("Original Base Address:")
#		case ('00010100'):
#			print("Entry Point:")
#		case ('00010201'):
#			print("Image Base Address:")
#		case ('000103ff'):
#			print("Import Libraries:")
#		case ('00018002'):
#			print("Checksum Timestamp:")
#		case ('00018102'):
#			print("Enabled For Callcap:")
#		case ('00018200'):
#			print("Enabled For Fastcap:")
#		case ('000183ff'):
#			print("Original PE Name:")
#		case ('000200ff'):
#			print("Static Libraries:")
#		case ('00020104'):
#			print("TLS Info:")
#		case ('00020200'):
#			print("Default Stack Size:")
#		case ('00020301'):
#			print("Default Filesystem Cache Size:")
#		case ('00020401'):
#			print("Default Heap Size:")
#		case ('00028002'):
#			print("Page Heap Size and Flags:")
#		case ('00030000'):
#			print("System Flags:")
#		case ('00040006'):
#			print("Execution ID:")
#		case ('000401ff'):
#			print("Service ID List:")
#		case ('00040201'):
#			print("Title Workspace Size:")
#		case ('00040310'):
#			print("Game Ratings:")
#		case ('00040404'):
#			print("LAN Key:")
#		case ('000405ff'):
#			print("Xbox 360 Logo:")
#		case ('000406ff'):
#			print("Multidisc Media IDs:")
#		case ('000407ff'):
#			print("Alternate Title IDs:")
#		case ('00040801'):
#			print("Additional Title Memory:")
#		case ('00e10402'):
#			print("Exports by Name:")
#		case ('00030100'):
#			print("Extra XEX Requirements (Kinect, NXE Packages etc): NOT READY")
#		case default:
#			print("Unknown:")
		
def XEXHandler():

	if DEBUG == False:
		print("XEX2 file support is very basic and not ready. Do -dbg to see early progress.\n")

	else:
		File.seek(7)
		Flags = binascii.hexlify(File.read(1), b' ')  # Flags
		match Flags:
			case (b'00'):
				print("Title Module")
			case (b'01'):
				print("Exports To Title")
			case (b'02'):
				print("System Debugger")
			case (b'03'):
				print("DLL Module")
			case (b'04'):
				print("Module Patch")
			case (b'05'):
				print("Patch Full")
			case (b'06'):
				print("Patch Delta")
			case (b'07'):
				print("User Mode")
			case default:
				print("Unknown Flag")

		File.seek(20)
		DecimalHeaderCount = int((repr(binascii.hexlify(File.read(4)))[2:10]), 16)
		print("\nOptional Header Info:")
		print("Optional Header Decimal =", DecimalHeaderCount)

		global TypeDataStruct
		global ValueDataStruct
		TypeDataStruct = []
		ValueDataStruct = []

		InitialTypeSeek = 24 # This gets the header ID
		for x in range(DecimalHeaderCount):
			File.seek(InitialTypeSeek)
			ReadOut = (repr(binascii.hexlify(File.read(4)))[2:10])
			InitialTypeSeek = InitialTypeSeek + 8
			TypeDataStruct.append(ReadOut)

		InitialTypeSeek = 28 # This gets the header Value
		for x in range(DecimalHeaderCount):
			File.seek(InitialTypeSeek)
			ReadOut = (repr(binascii.hexlify(File.read(4)))[2:10])
			InitialTypeSeek = InitialTypeSeek + 8
			ValueDataStruct.append(ReadOut)

		HeaderScanRange = 0 #Prints Header ID types in the XEX, change
		for x in range(DecimalHeaderCount):
			HeaderIDHandler(HeaderScanRange)
			#print(ValueDataStruct[HeaderScanRange], "\n")
			#HeaderScanRange = HeaderScanRange + 1

def TypeHandler():
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
	elif FileType == b'XEX2':
			XEXHandler()
	else:
			print("Not Recognized")
			File.close()

if len(sys.argv) != 1: #Check if theres arguments

	FilePath = sys.argv[1] #set FilePath to Argument

	if len(sys.argv) == 3:

		match sys.argv[2]:
			case "-a":
				ArgType = "-a"
			case "-dbg":
				DEBUG = True
				ArgType = "-a"
			case default:
				sys.exit("Invalid argument.")

		if os.path.exists(FilePath): #Check if FilePath is actually a valid path

			File = open(FilePath, "rb+") #Open File
			FileType = File.read(4) #Read the first 4 bytes
			TypeHandler()

		else:
			print("Invalid file path given")	

	else:

		ArgType = 0

		if os.path.exists(FilePath): #Check if FilePath is actually a valid path
			File = open(FilePath, "rb+") #Open File
			FileType = File.read(4) #Read the first 4 bytes
			TypeHandler()
		else:
			print("Invalid file path given")

else:
	print("No arguments given.\nProper Usage: Python360.py [File-Path] [Optional-Args]\n-a   - Prints full STFS info.")
	print("-dbg - Shows various debug info and enables early XEX support. this automatically does -a.")