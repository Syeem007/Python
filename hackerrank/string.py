'''
s = input()
if s.isalnum():
    print(True)
elif s.isalpha():
    print(True)
    if s.isdigit():
        print(True)
        if s.isdigit():
            print(True)
            if s.isupper():
                    print(True)
else:
    print(False)
'''


def new():
    s=input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        return "s." + test + "()"

