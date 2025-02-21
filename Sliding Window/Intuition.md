- Because of the nature of sliding window problems. You usually only need to have a left pointer, the right can made in the loop.

```python

l = 0
for r in range(len(foo)):
    ...

```

- The window doesn't always need to necessarily be a data structure, sometimes a counter will do!
- The most important thing is answering _"what causes the window to shrink?"_.
- 
