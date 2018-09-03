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

def checkRules(line):
    i = 0
    while i < len(line) and line[i] != '#':
        print line[i]
        i = i + 1

def parseFile(file):
    section = 0
    for line in file:
        if section == 0:
            checkRules(line)
        print len(line)

checkArgs(len(sys.argv))
file = openFile(sys.argv[1])
parseFile(file)


#add 42 header!
#handling comments and empty files
