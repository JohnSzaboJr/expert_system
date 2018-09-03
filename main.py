import sys

def errorQuit(msg):
    print msg
    sys.exit()

def checkArgs(num):
    if (num != 2):
        errorQuit('error: incorrect number of arguments')

def openFile(fname):
    try:
        file = open(sys.argv[1])
        return (file)
    except IOError:
        errorQuit('error: could not read file')

checkArgs(len(sys.argv))
file = openFile(sys.argv[1])
for line in file:
    print len(line)

#handling comments and empty files
