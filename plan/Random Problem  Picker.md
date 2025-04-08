```bash
ls | sed -n "$(( (RANDOM % $(ls | wc -l)) + 1 ))p"
```

