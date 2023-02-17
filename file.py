import itertools as its


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    words = "1234567890abcdefghijklmnopqrstuvwxyz"  # a set of password characters
    r = its.product(words, repeat=8)  # random combination of 8 characters
    dic = open("pwd.txt", "a")  # store wifi combinations in file
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()
    print('end..')  # Press ⌘F8 to toggle the breakpoint.
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
