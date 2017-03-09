# coding:utf-8

from AssociationRulesMining.common.crossplatform import ossep
import sys

def readAD():
    data_dict = {}
    try:
        with open('.' + ossep + 'testInput.dat', 'r') as file:
            line = file.readline()
            while line:
                data_list = (line.strip()).split(' ')
                data_dict.setdefault(data_list[0], data_list[1:])
                line = file.readline()
    except IOError:
        print('cann\'t  open testInput.dat.\n')
        sys.exit(0)
    print(data_dict)
