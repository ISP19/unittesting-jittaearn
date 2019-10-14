[![Build Status](https://travis-ci.com/jittaearn/unittesting.svg?branch=master)](https://travis-ci.com/jittaearn/unittesting)
## Unit Testing Assignment

by Jitta Koopratoomsiri.


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| a large list           |  normal result      |
| 2 items, many times, many orders | 2 item list, items in same order  |
| not a list             |  raises TypeError   |
| Many items, many times, many teorders |  list with one duplicates of each  |

## Test Cases for Fraction

| Test case (__init__)   |  Expected Result    |
|------------------------|---------------------|
| not an integer         |  raises TypeError   |


| Test case (__str__)    |  Expected Result    |
|------------------------|---------------------|
| zero as a numerator    |  fraction is equal to zero  |
| zero as a denominator  |     numerator/ 0    |
| zero as both numerator and denominator |        0/0       |
| numerator without denominator | numerator only |


| Test case (__add__)    |  Expected Result    |
|------------------------|---------------------|
| adding positive fraction  |  positive result |
| adding negative fraction  |  negative result |
| adding negative and positive fraction | negative result if negative fraction is larger than that of positive |
| adding a fraction with zero  |    itself     |


| Test case (__sub__)    |  Expected Result    |
|------------------------|---------------------|
| subtracting positive fraction  |  negative if the second fraction is larger than the first, otherwise positive |
| subtracting negative fraction  |  negative result |
| subtracting negative with positive fraction | negative result |
| subtracting positive with negative fraction | positive result |
| subtracting a fraction with zero  |    itself     |


| Test case (__mul__)    |  Expected Result    |
|------------------------|---------------------|
| multiply positive fraction  |  positive result |
| multiply negative fraction  |  positive result |
| multiply negative with positive fraction | negative result |
| multiply fraction with zero  |       0       |


| Test case (__eq__)     |  Expected Result    |
|------------------------|---------------------|
| same simplest form     |        Equal        |
| different simplest form  |      Not Equal      |


| Test case (__gt__)     |  Expected Result    |
|------------------------|---------------------|
| first fraction is greater than the second  |        True         |
| first fraction is smaller than the second  |        False        |
| equal fraction         |        False        |



| Test case (__neg__)    |  Expected Result    |
|------------------------|---------------------|
| positive fraction      |  negative fraction  |
| negative fraction      |  positive fraction  |
| zero                   |  zero               |



