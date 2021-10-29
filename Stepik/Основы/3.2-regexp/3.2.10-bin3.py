"""
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Sample Input:

0
10010
00101
01001
Not a number
1 1
0 0
Sample Output:

0
10010
01001
"""


import sys
import re
pattern1 = r"^(0|(1(01*0)*1))*$"
pattern2 = r"((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1(0+)?)|(0(0+)?)))"

for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(pattern1, line):
        print(line)
