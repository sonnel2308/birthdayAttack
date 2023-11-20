# birthdayAttack

Week 9 exercise for COMP6841.

Takes the confession_real.txt file, generates its sha256 hash, and brute forces combinations of spaces at the end of each
line of the confession_fake.txt file until the last two bits of the hashes match.

The script reads from confession_fake_copy.txt (which remains the original document) and writes the appended spaces to confession_fake.txt.

# Method
The script's method of brute forcing is as follows.

First, the script generates a binary string with the length of the number of lines in the fake confession document. Each line corresponds to whether or not that line in the document has a space appended to it.

The maximum number of combinations possible is 2^n where n is the number of lines in the document, and 2 since the line can either have an appended space or not have one.

The script runs for each binary string from 0 to 2^n, and at each iteration it updates the fake confession file with the corresponding appended spaces and generates the new hash until it matches that of the real confession file.
