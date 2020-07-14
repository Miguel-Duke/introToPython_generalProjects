highway_number = int(input('Please enter a highway number:'))

if 1000 > highway_number > 0:
    if (int(highway_number) % 2 == 1):
        direction = 'north/south.'
    else:
        direction = 'east/west.'

    if (highway_number <= 99):
        aux_pri = 'primary'
    else:
        aux_pri = 'auxiliary'
    
    if aux_pri == 'auxiliary':
        serving = (highway_number % 100)
    
    if aux_pri == 'primary':
        print('I-' + str(highway_number), 'is', str(aux_pri) + ',', 'going', direction)
    else:
        print('I-' + str(highway_number), 'is', str(aux_pri) + ',', 'serving I-' + str(serving) + ',', 'going', direction)

elif highway_number >= 1000:
    print(highway_number, 'is not a valid interstate highway number.')
    
else:
    print('0 is not a valid interstate highway number.')
