array = "A man, a plan, a canal: Panama"

l=len(array)-1
flag=True

for a in range(len(array)//2):
    if a<l:
        while not array[l].isalnum():
            l=l-1
        if array[a].isalpha():
                c = array[a].lower()
                if c == array[l].lower():
                    l=l-1
                else:
                    flag = False
                    print(a)
                    print(l)
if flag ==False:
    print("the string is not a palindrome" )
else:
    print("palindrome")

