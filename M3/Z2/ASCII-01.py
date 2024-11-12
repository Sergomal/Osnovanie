for i in range(256):
    if i == 9:
        print(f"| {i:>3}:\t ", end="\t")
    elif i == 10:
        print(f"| {i:>3}:\t ", end="\t")
    elif i == 13:
        print(f"| {i:>3}:\t ", end="\t")
        # break
    elif i == 142:
        print(f"| {i:>3}:\t ", end="\t")
    else:
        print(f"| {i:>3}:\t {chr(i)}", end="\t")
    if i % 10 == 0:
        print()
