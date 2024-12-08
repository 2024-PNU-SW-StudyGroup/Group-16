count = 0

def recursion(s, l, r):
    global count
    count+=1
    if l>=r :
        return 1
    elif s[l]!=s[r]:
        return 0
    else :
        return recursion(s, l+1, r-1)
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n_test = int(input())

test_case = [input() for i in range(n_test)]

for i in range(n_test):
    count = 0
    print(isPalindrome(test_case[i]),count)