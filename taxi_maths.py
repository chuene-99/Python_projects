#this program operates as a taxi maths calculator in South Africa.
try:
    taxi_fee=int(input('taxi fee per passenger:'))
    amount=int(input('amount sent forward:'))
    people=int(input('no. of people:'))
except:
    print('please enter numeric value')
    quit()
change=amount-(taxi_fee*people)
print('change:',change)
