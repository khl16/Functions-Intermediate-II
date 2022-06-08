# <1>
# 1.1

x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(f"x was orginally [ [5,2,3], [10,8,9] ]  and is now {x}")



# ------------------------------------------------------------------------------------------------------
# 1.2

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print("student 1's orginal information was {'first_name':  'Michael', 'last_name' : 'Jordan'}")
print(f"student 1's new information is {students[0]}")

# ------------------------------------------------------------------------------------------------------
# 1.3

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print("sports_directory key code 'soccer' used to say ['Messi', 'Ronaldo', 'Rooney'] ")
print('now has changed to')
for i in range(len(sports_directory['soccer'])):
    print(f"{sports_directory['soccer'][i]} and ")


# ------------------------------------------------------------------------------------------------------
# 1.4

z = [{'x': 10, 'y': 20}] 

z[0]['y'] = 30
print("z used to look like [{'x': 10, 'y': 20}] now " , z)

# ------------------------------------------------------------------------------------------------------
# <2>
# 

students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionarycopy(anyList):
    stringReturn = ''
    for val in anyList:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
print(iterateDictionarycopy(students2))


# ------------------------------------------------------------------------------------------------------
# <3>

def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn
print(iterateDictionary2('last_name',students2))

# ------------------------------------------------------------------------------------------------------
# <4>

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDictonaryInfo(my_dictonary):
    # outputStr = ''
    for key in my_dictonary:
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")
printDictonaryInfo(dojo)








