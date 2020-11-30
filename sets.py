string_A = (input("Enter first string: ").lower())
string_B = (input("Enter second string: ").lower())
print(string_A, string_B)
set_A = set()
set_B = set()
for i in string_A:
    set_A.add(i)
for j in string_B:
    set_B.add(j)
union = set_A.union(set_B)
intersection = set_A.intersection(set_B)
unique_A = set_A - intersection
unique_B = set_B - intersection
difference = union - intersection
ele_in_A_not_B = set_A.difference(set_B)
ele_in_B_not_A = set_B.difference(set_A)
print("The identical characters in both: "+str(intersection))
print("The different characters in both: "+str(difference))
print("Unique Characters in A: "+str(unique_A))
print("Unique Characters in B: "+str(unique_B))
print("The characters in A but not in B: "+str(ele_in_A_not_B))
print("The characters in B but not in A: "+str(ele_in_B_not_A))
