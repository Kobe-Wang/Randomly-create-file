#!/usr/bin/python
import sys, getopt

def usage():
	#print 'Help information: -h <help> -i <inputfile> -o <outputfile>'
	print("Usage:%s [-B|-E|-D|-O|-N] [-h|--help] args....")
	print("For example: python pyURandom.py -B 1 -E 10 -D /home/delta/test/ -O 5 -N 3" )

def main(argv, arguList):
	try:
		opts, args = getopt.getopt(argv,"hB:E:D:O:N:",["help","BeginSize=","EndSize=", "FileDIR", "FileDirNum" ,"FileNum"])
	except getopt.GetoptError:
		print("Failed...")
		usage()
		sys.exit(2)
	if argv == [] or opts == []:
		print 'Use Default Argument...'
		#----------Default Parameters value---------
		rangeBegin = 1
		rangeEnd = 10
		fileUpDIR = '/home/delta/testggggg/'
		fileDirNum = 5
		fileNum = 3
		print 'Usage: -B %d -E %d -D %s -O %d -N %d' % (rangeBegin, rangeEnd, fileUpDIR, fileDirNum, fileNum)
		#-------------------------------------------
	else:
		rangeBegin = 0 
		rangeEnd = 0
		fileUpDIR = ''
		fileDirNum = 0
		fileNum = 0
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				usage()
				sys.exit()
			elif opt in ("-B", "--BeginSize"):
				rangeBegin = arg
			elif opt in ("-E", "--EndSize"):
				rangeEnd = arg
			elif opt in ("-D", "--FileDIR"):
				fileUpDIR = arg
			elif opt in ("-O", "--FileDirNum"):
				fileDirNum = arg
			elif opt in ("-N", "--FileNum"):
				fileNum = arg
	arguList.append(rangeBegin)
	arguList.append(rangeEnd)
	arguList.append(fileUpDIR)
	arguList.append(fileDirNum)
	arguList.append(fileNum)

'''
#if __name__ == '__main__':
def mainName():
	arguList = []
	rangeBegin = 1
	rangeEnd = 10
	fileUpDIR = '/home/delta/testggggg'
	fileNum = 3
	main(sys.argv[1:], rangeBegin, rangeEnd, fileUpDIR, fileNum, arguList)
	print arguList
'''
