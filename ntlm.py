import hashlib, binascii, sys
print '''
	NTLM Hash Cracker 
		and 
	Generator\n'''
def argument_list():
	print("Arguments: -crack and -gen\n")
	exit()
args = sys.argv[1:]
if args:
	for arg in args:
		if arg == "-crack":
			passlist = raw_input("Insert dictionary: ")
			lines = [line.rstrip('\n') for line in open(passlist)]
			list_count = len(lines) -1
			password = raw_input("Insert hash to crack: ")
			count = 0
			while count <= list_count:
				hash = hashlib.new('md4',lines[count].encode('utf-16le')).digest()
				hash1 = binascii.hexlify(hash)
				print hash1
				if hash1 == password:
					print lines[count]
					exit()
				else:
					count = count + 1
		elif arg == "-gen":
			hash_gen = raw_input("Insert string: ")
			hash1_gen = hashlib.new('md4',hash_gen.encode('utf-16le')).digest()
			print(binascii.hexlify(hash1_gen) + ":%s" % hash_gen)

		else:
			argument_list()
else:
	argument_list()
