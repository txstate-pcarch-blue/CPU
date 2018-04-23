#!/usr/bin/python3

from Build_Functions import normalize_hex, get_parser


def clean_input(inlines):
    lines = []
    for line in inlines:
        # Remove Comments
        line = line.split('#')[0].split(';')[0]
        # Remove Commas
        line = line.replace(',', ' ')
        # Normalize spaces
        line = ' '.join(line.split())
        # Remove empty lines
        if len(line) != 0:
            lines.append(line)
    return lines


# Parses and stores the labels
#   Creates a dictionary storing the label name and the index
def parse_labels(inlines):
    labels_dict = dict()
    lines = []
    for i, line in enumerate(inlines):
        sp = line.split(':')
        if len(sp) == 1:
            lines.append(line)
            continue
        print("Label found at %#x, line: %s" % (i, sp))
        labels_dict[sp[0].strip()] = i
        lines.append(sp[1])
    return lines, labels_dict

# Assembles the source code in the inlines to hex
#   First, the input is cleaned, removing comments, standardizing format, and removing empty lines
#   Next, each line is parsed for the mnemonic
#   Next, The mnemonic is used to determine the function used to parse the instruction
#   Next, the parser function is called to get the assembled instruction
#   Next, The assembled hex data is added to an array
#   Finally, the filled array is returned
def assemble(inlines):
    lines = clean_input(inlines)
    lines, labels = parse_labels(lines)
    hexdata = []
    for i, line in enumerate(lines):
        sp = line.split()
        try:
            parser = get_parser(sp[0])
            instr = parser(line, labels, i)
        except KeyError:
            print("Key Error", i + 1, line)
            quit(1)
        hexdata.append(hex(instr))
    return hexdata


# Runs as a program if the file is called by python
# This section is ignored if the file is imported instead of called
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MIPS Assembler for the blue team CPU")
    parser.add_argument('ifile')
    parser.add_argument('-o', '--output', default='a.hex', metavar='ofile')
    args = parser.parse_args()
    with open(args.ifile) as f:
        lines = f.readlines()
    hexdata = assemble(lines)
    normalized = normalize_hex(hexdata)
    with open(args.output, 'w') as f:
        f.writelines(normalized)
