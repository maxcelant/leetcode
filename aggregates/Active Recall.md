```dataview
table last_attempt, rating,
  date(last_attempt + dur(rating + " days")) as next_review
from ""
where last_attempt and rating
sort date(last_attempt + dur(rating + " days")) asc
```
