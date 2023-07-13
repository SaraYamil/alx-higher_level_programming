#!/usr/bin/python3
# Owned By MoOka
import hidden_4
if __name__ == "__main__":
    folder = dir(hidden_4)
    for name in folder:
        if name[:2] != "__":
            print("{}".format(name))
