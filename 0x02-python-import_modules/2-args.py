#!/usr/bin/python3
import sys
if __name__ == "__main__":
    list_argv = sys.argv
    list_argv.pop(0)

    liat_len = len(list_argv)
    arg = ""

    if liat_len == 0:
        arg = "argument" + "."
    elif liat_len == 1:
        arg = "argument" + ":"
    else:
        arg = "arguments" + ":"
    print(f"{liat_len} {arg}")

    length = liat_len - 1

    for num in range(liat_len):
        print(f"{num + 1}: {list_argv[num]}")
