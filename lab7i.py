#!/usr/bin/env python3
# Student ID: [seneca_id]
def function1():
    # To modify the global 'schoolName', we must declare it as global.
    global schoolName # This line is added/changed from the original problem description to modify global scope
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    # This already correctly targets the global 'schoolName' as per original instructions.
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName) # This will now print 'SICT'
function2()
print('print() in main on schoolName:', schoolName)