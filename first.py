
# append it add elements in the end of list
a = [1, 2, 3, 4]
b= [6, 7, 8, 9]
print(a)
a.append(5)
a.append(True)
a.append(b)
print(a[2])
print(a[6][1])
print(a)
print("#" * 20)

# extend
c = [1, 2, 3, 4]
d = ["A", "B", "C"]
e = ["One", "Two"]
c.extend(d)
print(c)
c.extend(e)
print(c)
print("#" * 20)

# remove
x = [1, 2, 3, 4, "ayman", True, "ayman"]
x.remove("ayman")
print(x)
print("#" * 20)

# sort 
# It rearranges the list for one kind (int or str)
y = [1, 2, -10, 17, 29]
y.sort()
print(y)
z = ["A", "B", "C"]
z.sort()
print(z)

u = [1, 2, 100, 120, -10, 17, 29]
u.sort(reverse=False) # Default for sort is false
print(u)
v = [1, 2, 100, 120, -10, 17, 29]
v.sort(reverse=True) # Change Default for sort to true
print(v)

print("#" * 20)

# reverse reflects the elements only and does matter about kind of data
h = [10, 1, 2, 80, "ayman", 100]
h.reverse()
print(h)

print("#" * 20)

# clear 
f = [1, 2, 3]
f.clear()
print(f)

print("#" * 20)

# count 
g = [1, 2, 3, 4, 5, 4]
print(g.count(4))

print("#" * 20)

#index it prints first elements find
j = ["ayman", "osama", "ameen", "ayman"]
print(j.index("ayman"))
j.index("ayman")

print("#" * 20)

# insert
m = [1, 2, 3, "A", "B", "C"]
m.append(5)
print(m)
n = [1, 2, 3, "A", "B", "C"]
n.insert(0,0) #(index, elements)
n.insert(4,4)
n.insert(-1,"Test")
n.append("Test")
print(n)

print("#" * 20)

#pop it cuts the elements from the list
r = [1, 2, 3, 4, "A", "B", "C"]
print(r.index("A"))
print(r.pop(-2))
print(r.pop(4))
print(r.pop(2))
print(r.pop(-1))


