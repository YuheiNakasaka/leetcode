S = input()
a = S[0:2]
b = S[2:4]

def is_month(s):
    if 1 <= int(s) <= 12:
        return True
    else:
        return False


if is_month(a) and is_month(b):
    print("AMBIGUOUS")
elif is_month(a) and is_month(b) == False:
    print("MMYY")
elif is_month(a) == False and is_month(b):
    print("YYMM")
else:
    print("NA")