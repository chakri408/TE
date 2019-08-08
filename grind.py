import sys
import argparse
import os

# Parse arguments
parser = argparse.ArgumentParser(
    description='Usage:',
    epilog="Eg: ./grind")
parser.add_argument(
    '--d',
    dest='path',
    help='List files in directory. Eg: ./grind --d <path>',
    action='store')
parser.add_argument(
    '--m',
    action='store',
    dest='match',
    help='Search file in given directory Eg: ./grind --d <path> --m foo')
parser.add_argument(
    '--r',
    action='store',
    dest='recursive',
    help='Search file recursively in a given directory. Eg: ./grind --d <directory> --r foo')
args = parser.parse_args()

def ListFiles(path):
    if os.path.dirname(path):
        file_list = []
        for t1, t2, t3 in os.walk(path):
            for file in t3:
                file_list.append(''.join(t1+"/"+file))
            for directory in t2:
                file_list.append(''.join("/" + directory))

        for list in file_list:
            print(list)


def MatchFile(path,match):
    if os.path.dirname(path):
        file_list = []
        for t1, t2, t3 in os.walk(path, topdown=True):
            if match in t3:
                file_list.append(''.join(t1+"/"+match))
                t2[:] = []
                #print(file_list)
        for list in file_list:
            print(list)

def RecursiveMatch(path,match):
    if os.path.dirname(path):
        file_list = []
        for t1,t2,t3 in os.walk(path):
            if match in t3:
                file_list.append(''.join(t1+"/"+match))
            if match in t2:
                file_list.append(''.join(t1+"/"+match))
        for list in file_list:
            print(list)
	
def main():
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.match and args.path:
        path = '%s' % args.path
        match = '%s' % args.match
        MatchFile(path,match)
    elif args.recursive and args.path:
        path = '%s' % args.path
        match = '%s' % args.recursive
        RecursiveMatch(path,match)
    elif args.path:
        path = '%s' % args.path
        ListFiles(path)
    else:
        print('No action defined, please choose one of the action. ./grind -h')

main()
