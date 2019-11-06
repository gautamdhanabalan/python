# Script to generate testlist

import argparse

if __name__ == '__main__':
    
	# Read perm file and output file 
    parser = argparse.ArgumentParser(prog='PROG') 
    parser.add_argument('-p', '--perm', nargs='?', help='perm file')
    parser.add_argument('-l', '--list', nargs='?', help='list file')
    args = parser.parse_args()
   
    # Open perm file
    permfile = open(args.perm, "r")
    line = permfile.readlines() 
    for lines in line:
        print(lines) 
    	
