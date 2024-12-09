string = input()
list_string = list(string)
def alphabet_finder(string):
    for i in range(ord('a'), ord('z')):
        if (ord(string)) == i:
            return i - ord('a')
        i += 1
    return - 1

for i in range(0, len(list_string)):
    if alphabet_finder
    print(alphabet_finder(list_string[i]))
    i += 1