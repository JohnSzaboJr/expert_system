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
import re

class Fact(object):
    def __init__(self, name):
        self.name = name
        self.implies = []
        self.isImpliedBy = []

    def addChild(self, fact):
        self.implies.append(fact)

    def addParent(self, fact):
        self.isImpliedBy.append(fact)

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

def charCheck(str, search = re.compile(r'[^A-Z()!+|^<=> \t\v\n]').search):
    if search(str):
        errorQuit('error: invalid characters')

def isSpace(char):
    return char == ' ' or char == '\t' or char == '\v' or char == '\n'

def skipSpace(str, i, l):
    while i < l and isSpace(str[i]):
        i += 1
    return i

def isOperator(char):
    return char == '+' or char == '|' or char == '^'

    

def checkSyntax(str, i, l):
    i = skipSpace(str, i, l)
    if i == l or str[i] == ')':
        return i
    j = i
    if str[i] == '(':
        i += 1
        i = skipSpace(str, i, l)
    if str[i] == ')':
        errorQuit('error: syntax error in rules')
    i = j
    if str[i] == '!':
        i += 1
    i = skipSpace(str, i, l)
    if i == l:
        errorQuit('error: syntax error in rules')
    if str[i] == '(':
        return i
    if str[i] >= 'A' and str[i] <= 'Z':
        i += 1
    else:
        errorQuit('error: syntax error in rules')
    i = skipSpace(str, i, l)
    if i == l or str[i] == ')':
        return i
    if isOperator(str[i]):
        i += 1
    else:
        errorQuit('error: syntax error in rules')
    i = skipSpace(str, i, l)
    if i == l or isOperator(str[i]) or str[i] == ')':
        errorQuit('error: syntax error in rules')
    else:
        i -= 1
    return i

def errorCheck(str):
    i = 0
    j = 0
    l = len(str)
    while i < l:
        i = checkSyntax(str, i, l)
        if i == l:
            break
        if str[i] == '(':
            j+=1
        if str[i] == ')':
            j-=1
            i += 1
            i = skipSpace(str, i, l)
            if i == l:
                break
            if str[i] == ')':
                i -= 1
            else:
                if isOperator(str[i]) == False:
                    errorQuit('error: syntax error in rules')
        if j < 0:
            errorQuit('error: syntax error in rules')
        i += 1
    if j != 0:
        errorQuit('error: syntax error in rules')

def checkRules(line):
    strict = False
    #recognize empty lines and just pass
    line = line.split('#', 1)[0]
    if len(line) == 0:
        return
    charCheck(line)
    condition = line.split('=>')[0]
    if condition == line:
        errorQuit('error: syntax error in rules')
    if len(line.split('=>')) > 2:
        errorQuit('error: syntax error in rules')
    if condition[len(condition) - 1] == '<':
        strict = True
        condition = condition[:-1]
    fact = line.split('=>')[1]
    errorCheck(condition)
    errorCheck(fact)


    print 'condition:' + condition
    print 'fact:' + fact
    print strict

#check for contradictions

def parseFile(file):
    section = 0
    facts = []
    for line in file:
        if section == 0:
            checkRules(line)


    # facts.append(Fact("C"))
    return facts

checkArgs(len(sys.argv))
file = openFile(sys.argv[1])
facts = parseFile(file)


#handling comments and empty files
