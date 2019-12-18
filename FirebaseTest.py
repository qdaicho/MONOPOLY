from firebase import firebase

# URL = 'https://monopolyhack-579e5.firebaseio.com/'

# firebase = firebase.FirebaseApplication('https://monopolyhack-579e5.firebaseio.com/',None)

# result = firebase.get('/MONOPOLYHACK/diceValue',None)#This allows this program to retrieve data for the username key in the database

result = firebase.post('/MONOPOLYHACK', {'diceValue': '21'})

# result2 = firebase.post('/MONOPOLYHACK/diceValue','jeff', '6')
# new_user = "apple"
# result2 = firebase.post('/MONOPOLYHACK/Mahir',  'ABC')
# firebase.post({
#   'MONOPOLYHACK/diceValue': 'Alan The Machine'
# })s

print(result)

result = firebase.post('/MONOPOLYHACK', {'diceValue': '25'})
result = firebase.get('/MONOPOLYHACK/', None)
print(result)
