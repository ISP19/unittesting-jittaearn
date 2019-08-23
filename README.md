## Unit Testing Assignment

by Jitta Koopratoomsiri.


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| large list             |  normal result      |
| 2 items, many times, many orders | 2 item list, items in same order  |
| not a list             |  raises TypeError   |
| Many items, many times, many orders |  list with one duplicates of each  |

## Test Cases for Fraction

| Test case(constructor)           |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |

| Test case(operation)           |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |