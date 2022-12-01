[toc]
## 02_find_all_links
### regular expression
#### +
`"o+k"` == "ok" or "ook" or "oook" ...  (one or more times)
#### *
`"o*k"` == "k" or "ok" or "ook" or "oook" ... (zero or more times)
#### ?
`"o?k"` == "k" or "ok" (zero or one time)

[aeiou]     matches all 'a e i o u' letters in the string "google runoob taobao".
[^aeiou]    matches all letters in the string "google runoob taobao" except  'a e i o u'.
[A-Z]       represents a range, matching all uppercase(大写) letters, [a-z] represents all lowercase（小写） letters.
.           matches all single character except "\n" and "\r".
[\s\S]      matches all. s matches all whitespace characters, including newlines, and \S non-whitespace
characters, excluding（不包括） newlines（换行）.
\w          Match letters, numbers, underscores(下划线）. Equivalent to [A-Za-z0-9_]

## 04_rename_with_slice
### try_exception
try must have a except followed
#### single-branch
try:
    ...
except IndexError as e:
    print(e)
#### multi-branch
try:
    ...
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
#### universal
try:
    ...
except Exception as e:
    print(e)

#### else
when error not appear , do the else