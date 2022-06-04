# Calendar Module in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Calendar Module in Python - Hacker Rank Solution START
import calendar

m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())
# Calendar Module in Python - Hacker Rank Solution END
