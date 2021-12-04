import itertools
import string

def check_file_diffs(filename1, filename2):
    collisions = {}
    with open(filename1, "r") as f1, open(filename2, "r") as f2:
        for line1, line2 in itertools.zip_longest(f1, f2, fillvalue="missing elt"):
            l1 = line1.strip()
            l2 = line2.strip()
            if l1 != l2:
                if ((l1 + " != " + l2) not in collisions.keys()):
                    collisions[(l1 + " != " + l2)] = int(1)
                else:
                    collisions[(l1 + " != " + l2)] = collisions[(l1 + " != " + l2)] + 1
    f1.close()
    f2.close()
    while (collisions):
        max = 0
        max_k = ""
        for k in collisions.keys():
            if collisions[k] > max:
                max = collisions[k]
                max_k = k
        print("Found " + str(max) + " instances of " + max_k)
        del collisions[max_k]

check_file_diffs("test1.txt", "test2.txt")