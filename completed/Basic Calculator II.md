---
tags:
  - stack
  - medium
  - meta
link: https://neetcode.io/problems/basic-calculator-ii?list=neetcode250
last_attempt: 2025-10-19
rate:
  - ★★★★
---
#### Problem
You are given a string `s` which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-(2^31), (2^31)-1]`.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

**Example 1:**

```java
Input: s = "3+2*2"

Output: 7
```

#### Notes
---


#### Code
---

```python
class Solution:
    def calculate(self, s: str) -> int:
        # Used to keep track of the current number as we loop
        num = 0
        # Keeps track of all the numbers as we travel the string
        # When we see a multiplication or division, we will pop the top value
        # and perform the operation before adding the result back to the stack
        stack = []
        # The current operation to perform 
        # in the case of + or -, we simply add that value to the stack
        op = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                # This is a simple way to create a multi digit number
                # one digit at a time from bigendian side
                num = num * 10 + int(ch)
            # If the current char is not a digit or space
            # or it's the last value in the string
            # then we want to perform the operation on it
            if (not ch.isdigit() and not ch == " ") or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                # Reset the number to zero
                # to prepare for the next one
                num = 0
                # The operation for the next eval is the current char
                op = ch
        # The stack at the end represents all of the values that
        # need to be combined to give the result
        return sum(stack)



```

#### Follow Up: *"What about O(1) space?"*

```python
def calculator(s: str) -> int:
  s = s.replace(' ', '')
  prev = 0
  total = 0
  num = 0
  op = '+'
  for n in s + '+':
    if n.isnumeric():
      num = num * 10 + int(n)
    else:
      if op == '+':
        prev = num
        total += num
      elif op == '-':
        prev = -num
        total -= num
      elif op == '*':
        total -= prev
        prev = (prev * num)
        total += prev
      elif op == '/':
        total -= prev
        prev = int(prev / num)
        total += prev
      op = n
      num = 0
  return total
```