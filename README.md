# birthdayAttack

Week 9 exercise for COMP6841.

Takes the confession_real.txt file, generates its sha256 hash, and brute forces combinations of spaces at the end of each
line of the confession_fake.txt file until the last two bits of the hashes match.

The script reads from confession_fake_copy.txt (which remains the original document) and writes the appended spaces to confession_fake.txt.
