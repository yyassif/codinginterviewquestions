#Myungho Sim
#match string with this pattern "abc.def.abc.def"
#matching everything but a new line from hackerrank

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
