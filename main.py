# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jszabo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/03 17:31:36 by jszabo            #+#    #+#              #
#    Updated: 2018/09/03 17:31:41 by jszabo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    line = line.split('#', 1)[0]
    while i < len(line) and line[i] != '#':
        print line[i]
        i += 1

#skip spaces
#error if there is are multiple characters besides each other
#error if there are characters that are not 1, uppercase characters
# 2, parentheses 3, operators
#error if parentheses don't match

def parseFile(file):
    section = 0
    for line in file:
        if section == 0:
            checkRules(line)
        print len(line)

checkArgs(len(sys.argv))
file = openFile(sys.argv[1])
parseFile(file)


#handling comments and empty files
