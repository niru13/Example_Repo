s1 = " Niraj is the Best. Niraj is a Billionaire."

print(s1.find("a"))
# Output :- 4

print(s1.find("a",5,8))
# output :- -1

print(s1.find("a",13,25))
# Output :- 23


print(s1.find("a",-1,-20))
# output :- -1 


# print(s1.find("a","t"))
# output :- Error    TypeError: slice indices must be integers or None or have an __index__ method