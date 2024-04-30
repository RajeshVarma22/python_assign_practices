names = input("Enter some names with spaces: ").split()
shortestName = min(names, key=len) 
longestName = max(names, key=len)

print("shortestName :-", shortestName)
print("longestName :-", longestName)
