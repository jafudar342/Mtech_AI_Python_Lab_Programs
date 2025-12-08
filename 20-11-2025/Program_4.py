s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("Original set1 = ", s1)
print("Original set2 = ", s2)

s1.add(6)
s2.add(7)
print("After adding element to set1 = ", s1)
print("After adding element to set2 =", s2)

s1.remove(2)
s2.remove(3)
print("After removing element from set1 = ", s1)
print("After removing element from set2 =", s2)

print("Search 3 in set1: ", 3 in s1)

print("Union = ", s1.union(s2))

print("Intersection = ", s1.intersection(s2))
