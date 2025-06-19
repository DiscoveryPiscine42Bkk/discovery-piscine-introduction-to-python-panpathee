#1/usr/bin/python3
import sys #ต้องrunในbashผลถึงจะออกตามโจทย์


if len(sys.argv) == 2:
    parameter =sys.argv[1]
    user_input = input("what was the parameter? ")

    if user_input == parameter:
        print("good job")
    else:
        print("nope, sorry...")
else:
    print("none")