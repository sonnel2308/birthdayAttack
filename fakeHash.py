#!/usr/bin/env python3

import subprocess

# Number of lines in the fake confession document
NUM_LINES = 30
# Number of possible combinations of spaces in the document
NUM_COMBINATIONS = pow(2, NUM_LINES)
# Format binary string
FORMAT = "0" + str(NUM_LINES) + "b"

# Initialise binary string of spaces of length NUM_LINES to 0 padded with leading zeroes
currCombination = 0
spaceString = format(currCombination, FORMAT)

############################################################################################

# Generate next binary string that tracks which lines have spaces
def nextSpaceString(currCombination):
    if currCombination != NUM_COMBINATIONS:
        currCombination += 1
    return format(currCombination, FORMAT), currCombination

# Update the fake confession file with the spaces in the lines corresponding to the
# binary space string
def updateFile(spaceString):
    lines = dict()
    with open("confession_fake_copy.txt") as file:
        i = 0
        for line in file:
            if spaceString[-i - 1] == "1":
                lines[i] = line.strip() + " " + "\n"
            else:
                lines[i] = line.strip() + "\n"
            i += 1
    # Write to the file
    with open("confession_fake.txt", "w") as file:
        for line in lines.values():
            file.write(line)

############################################################################################

commandReal = "cat confession_real.txt | openssl dgst -sha256"
commandFake = "cat confession_fake.txt | openssl dgst -sha256"

# While the real hash is not equal to the fake hash, rewrite the textfile with the new
# spaceString combination of spaces at the end of each line

resultReal = subprocess.run(commandReal, shell=True, text=True, capture_output=True)
resultFake = subprocess.run(commandFake, shell=True, text=True, capture_output=True)

hashReal = resultReal.stdout.split(' ')[1].strip()
hashFake = resultFake.stdout.split(' ')[1].strip()

print('REAL HASH:', hashReal)
print('FAKE HASHES:') 
print(hashFake)

# while hashReal != hashFake:
for i in range(NUM_COMBINATIONS):
    spaceString, currCombination = nextSpaceString(currCombination)
    updateFile(spaceString)
    resultFake = subprocess.run(commandFake, shell=True, text=True, capture_output=True)
    hashFake = resultFake.stdout.split(' ')[1].strip()
    print(hashFake)
    
    if hashFake[-2:] == hashReal[-2:]:
        print('HASH FOUND WITH SPACESTRING:', spaceString)
        exit(0)