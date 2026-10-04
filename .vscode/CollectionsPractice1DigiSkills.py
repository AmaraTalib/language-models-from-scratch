My_list=[1,2,3,4,5]
My_list.append(6)
print(My_list)

tuple=("Isl","Rwp","karachi")
print(tuple[1])

A={12,15,16,18,19,20}
B={18,19,20,12,89}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

Personal={"name":"Amara","age":20,"Semester":6}
for key,value in Personal.items():
   print(key,":",value)