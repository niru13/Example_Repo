s1 = " Niraj "


#  s1[a:b:c]
#  s1[a:b:c] when a<= b and c is +ve
print(s1[2:7:1])
# Output :- iraj


#  s1[a:b:c] when a>b and c is +ve
print(s1[7:2:1])
# Output :- No output


# s1[a:b:c] when a>b and c is -ve
print(s1[7:2:-1])
# Output :- jar


#s1[a:b:c] when a is -ve and b is -ve and c is +1
print(s1[-1:-7:])
# Output :- No Output

#s1[a:b:c] when a is -ve and b is -ve and c is also -1
print(s1[-1:-9:-1])
# Output :- jariN