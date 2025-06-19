#1/usr/bin/python3
import sys #ต้องrunในbashผลถึงจะออกตามโจทย์
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    strig_to_search =sys.argv[2]
    occurrences = re.findall(re.escape(keyword), strig_to_search)
    print(len(occurrences))
else:
    print("none")