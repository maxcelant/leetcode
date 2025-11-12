---
tags:
  - strings
  - easy
  - meta
link: https://leetcode.com/problems/goat-latin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-12
rate:
  - ★★★★★
---
#### Problem
You are given a string `sentence` that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

- If a word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, or `'u'`), append `"ma"` to the end of the word.
    - For example, the word `"apple"` becomes `"applema"`.
- If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add `"ma"`.
    - For example, the word `"goat"` becomes `"oatgma"`.
- Add one letter `'a'` to the end of each word per its word index in the sentence, starting with `1`.
    - For example, the first word gets `"a"` added to the end, the second word gets `"aa"` added to the end, and so on.

Return _the final sentence representing the conversion from sentence to Goat Latin_.

**Example 1:**

**Input:** sentence = "I speak Goat Latin"
**Output:** "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

#### Notes
Not much to say for this one

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for i, s in enumerate(sentence.split(' ')):
            word = s
            if s[0].lower() in vowels:
                word += "ma"
            else:
                word = word[1:] + s[0] + "ma"
            res.append(word + ('a' * (i + 1)))
        return ' '.join(res)
```
