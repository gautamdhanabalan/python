# Script to generate testlist

import argparse
import re

def permute_dict(line):
    print(line)
    if re.findall("TbName tb", line):
        print(re.findall("[^a-z]^: [a-z]+", line))
    				


if __name__ == '__main__':
    
	# Read perm file and output file 
    parser = argparse.ArgumentParser(prog='Test List Generation') 
    parser.add_argument('-p', '--perm', nargs='?', help='permutation file')
    parser.add_argument('-l', '--list', nargs='?', help='output testlist file')
    args = parser.parse_args()
   
    # Open perm file
    permfile = open(args.perm, "r")
    for line in permfile.readlines():
        permute_dict(line)    	
