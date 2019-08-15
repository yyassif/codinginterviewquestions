#Myungho Sim
#regex problem from hackerrank
#matching specific string in a text and count how many matches there are
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
