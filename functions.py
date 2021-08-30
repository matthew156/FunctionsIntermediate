# Question 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['x'] = 30

print(students)
print(sports_directory)
print(z)


#Question  2&3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(arr, key, key2):
    for i in arr:
        print(f'first_name - {i[key]} last_name - {i[key2]}')

iterate_dictionary(students, 'first_name', 'last_name')



#Question 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

locationslength = len(dojo['locations'])
instructorslength = len(dojo['instructors'])



def printInfo(arr):
    print(f'{locationslength} LOCATIONS')
    print(dojo.get('locations'))
    print(f'{instructorslength} INSTRUCTORS')
    print(dojo.get('instructors'))
print(printInfo(dojo))

