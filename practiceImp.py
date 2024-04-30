# anagram in python

# input1=input("enter the first string:")
# input2=input("enter the second string:")

# found=0
# not_found=0
# one=len(input1)
# two=len(input2)
# if one==two:
#     for i in range(one):
#         found=0
#         for j in range(one):
#             if input1[i]==input2[j]:
#                 found=+1
#                 break
#         if found==0:
#             not_found=1
#             break
#     if not_found==1:
#         print("given string is not a anagram")
#     else:
#         print("given string is a anagram")
# else:
#     print("given string lengths are not equal")


# -----------------------------------------------------------------------------

# def string(stri):
#     if len(stri)==1:
#         return [stri]
#     anagrams=[]
#     for i in range(len(stri)):
#         c=stri[i]
#         sub_anagram=string(stri[:i]+stri[i+1:])
#         for sub in sub_anagram:
#             anagrams.append(c+sub)
#     return anagrams

    
# stri='abcd'
# anagrams=string(stri)
# print(anagrams)



# -------------------------------------------------------------
# palindrome


# def pali(str):
#     length = len(str)
#     ans = ""
#     for i in range(length):
#         ans += str[-(i+1)]
#     return ans

# ip = "absa"
# op  = pali(ip)

# if(op == ip):
#     print("Pali")
# else:
#     print("not pali")


# --------------------------------------------------------------

#  remove vowels in python

# def string(stri):
#     vowels=['a','e','i','o','u']
#     output=[i for i in stri.lower() if i not in vowels]
#     sp = [j for j in output if j not in " "]
#     print(output)
#     print(sp)
#     print("".join(output))
# stri=input("enter the string:")
# string(stri)

# ------------------------------------------------------------------

# Example using two inputs i and j
# output = [(i, j) for i in range(3) for j in range(3)]
# print(output)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# ------------------------------------------------------------

def string(stri):
    non_repitative={}
    for i in stri:
        if i in non_repitative:
            non_repitative[i]+=1
        else:
             non_repitative[i]=1
    for i in stri:
        if non_repitative[i]==1:
            print(non_repitative[i])
            return i
    return None
print(string("this is naveenkumar"))