s1 = "Hi AKM ! How are you ?"

print(s1.endswith("?"))
# Output :- True

print(s1.endswith("akm"))
# Output :- False

print(s1.endswith("are you ?"))
# Output :- true

print(s1.endswith("Hi",0,2))
# Output :- True

print(s1.endswith("Hi",-1,-20))
# Output :-false 


print(s1.endswith(("Hi","?","are")))
# Output :- True
