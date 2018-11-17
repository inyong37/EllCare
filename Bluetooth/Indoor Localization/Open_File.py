# -*- coding: UTF-8 -*-

# Reference
# File: https://wikidocs.net/26

# Using readline function
'''
f = open("data.txt", 'r')
lines =f.readlines()
for line in lines:
    print(line)
f.close()
'''

# Using readlines function
'''
f = open("data.txt", 'r')
line = f.readline()
print(line)
f.close()
'''

# Using write function
'''
f = open("data.txt", 'r')
t = open("test.txt", 'w')
lines =f.readlines()
for line in lines:
    print(line)
    t.write(line)
f.close()
t.close()
'''
