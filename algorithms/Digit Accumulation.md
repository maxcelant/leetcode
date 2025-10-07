Take the current number, multiply it by 10 then add the next number to that output. 
```python
def numify(s):
    num = 0
    for d in s:
        num = num * 10 + int(d)
    return num

print(numify('152'))
```

```
1
15
152
```

Used in:
- [[Basic Calculator II]]