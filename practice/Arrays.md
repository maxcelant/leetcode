#### Flattening a List of Lists

```python title:"Flattening a list of lists"
def flatten(arrs):
    for i in range(1, len(arrs)):
        arrs[i] = merge(arrs[i - 1], arrs[i])
    return arrs[-1]

def merge(a1, a2):
    p1, p2 = 0, 0
    res = []
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:
            res.append(a1[p1])
            p1 += 1
        else:
            res.append(a2[p2])
            p2 += 1
    
    while p1 < len(a1):
        res.append(a1[p1])
        p1 += 1
    
    while p2 < len(a2):
        res.append(a2[p2])
        p2 += 1

    return res 

arrs = [[1,2,3], [4,5,6], [2,3,4], [1, 2]]
print(flatten(arrs))
```

- Since the current index always has the "merged" list, we grab it on next iteration by doing `i-1`, so that we continuously add to the most recent merging.

>![[Pasted image 20250310171057.png]]

#### ...