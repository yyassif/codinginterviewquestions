#Myungho Sim
#match string with this pattern "abc.def.abc.def"
#matching everything but a new line from hackerrank
#reference https://www.oreilly.com/library/view/oracle-regular-expressions/0596006012/re13.html
#regex anchors http://www.rexegg.com/regex-anchors.html
#{3} matches "." three times.
#"." is all the characters except newline
#^ checks for location of certain patterns

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
