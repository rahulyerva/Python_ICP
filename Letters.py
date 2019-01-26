s = str(input("Enter a Sentence: "))
l = s.split()
i = len(l)
n = 0
W = 0
N = 0
while (i > 0):

    if l[i-1].isalpha() ==  True:
        w = len(l[i-1])
        W = W + w
    else:
        n = len(l[i-1])
        N = N + n
    i = i - 1
print("From the given sentence there are", W, "Words and there are", N, "Numbers")




