s = " aasjsjdnskdsdddcasa"

print(s.count('a',0,20))
# Output :- 4

print(s.count('a',0))
# Output :- 4

print(s.count('a',20))
# Output :- 0


print(s.count('a',-1,-20))
# Output :- 0



print(s.count('a',0,0))
# Output :- 0



print(s.count('a',15,0))
# Output :- 0



print(s.count('a',-2,-20))
# Output :- 0