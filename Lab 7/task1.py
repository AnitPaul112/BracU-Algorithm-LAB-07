
def parent_find(parent, i):
    if parent[i] == i:
        return i
    return parent_find(parent, parent[i])
def merge(parent, size, i, j): 

    pi = parent_find(parent, i)
    pj = parent_find(parent, j)
    if pi == pj:        

        return size[pi]

    if size[pi] < size[pj]:
        pi, pj = pj, pi
    parent[pj] = pi
    size[pi] += size[pj]
    return size[pi]  


f1 = open("input1.txt","r")
f2 = open("output1.txt","w")
n, k = map(int, f1.readline().split())

parent = list(range(n+1))          
size = [1]*(n+1)           

for _ in range(k):        
    i, j =  map(int, f1.readline().split())
    output =merge(parent, size, i, j)
    f2.write(f"{output}\n")

f1.close()
f2.close()



