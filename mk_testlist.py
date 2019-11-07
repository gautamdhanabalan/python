# Script to generate testlist

import argparse
import re

parsed_test_ops = {} 
testlist = ""

def parse_permute(line):
    #line = re.findall(": [\s\S]+", line)
    #print(line)
    #line = re.findall("[a-z0-9+;_\s]+", line[0])
    #print(line)
    parsed_list = []
    line = re.split(":", line)
    line = re.split(";", line[1])
    for l in line:
        parsed_list.append(l.strip("\s \n"))
    print(parsed_list)
    return parsed_list 

def permute_dict(line):
    if re.findall("TbName tb", line):
        line = parse_permute(line)
        parsed_test_ops["tb"] = line 
    elif re.findall("TestName test", line):
        line = parse_permute(line)
        parsed_test_ops["test"] = line 
    elif re.findall("TestMode pe", line):
        line = parse_permute(line)
        parsed_test_ops["pe"] = line 
    elif re.findall("TestMode exe_state", line):
        line = parse_permute(line)
        parsed_test_ops["exe_state"] = line 
    elif re.findall("TestMode reg", line):
        line = parse_permute(line)
        parsed_test_ops["reg"] = line 
    elif re.findall("TestMode length", line):
        line = parse_permute(line)
        parsed_test_ops["length"] = line 
    elif re.findall("SimSeed iterations", line):
        line = parse_permute(line)
        parsed_test_ops["simseed"] = line 

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
    
    # Generate testlist
    for pe in parsed_test_ops["pe"]:
        if pe != '':
            pe += "+"
        for state in parsed_test_ops["exe_state"]:
            if state != '':
                state += "+"
            for reg in parsed_test_ops["reg"]:
                if reg != '':
                    reg += "+"
                for length in parsed_test_ops["length"]:
                    if length != '':
                        length += "+"
                    testlist += parsed_test_ops["tb"][0] + "." + parsed_test_ops["test"][0] + "." \
                            + pe + state + reg + length\
                            + ":" + parsed_test_ops["simseed"][0] + "\n"
    
    print(testlist) 
   
    
