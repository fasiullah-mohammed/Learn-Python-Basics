Travel=input('How far you would like to travel in miles? ')

Travel=int(Travel)
if Travel<=3:
  print('Please walk')

elif Travel>3 and Travel<300:
  print('Please drive')

else:
   print('fly')
