# This is the module for week 8's project date formatting!

def getUserInput():
    dateFormat = input('Will this date format be Chinese: C or Macedonean: M \n >').capitalize()
    while dateFormat != 'C' and dateFormat != 'M':
        dateFormat = input('Please choose a format of either Chinese: C or Macedonean: M \n >')
    if dateFormat == 'C':
        print('The format for Chinese is yyyy-mm-dd')
    else:
        print('The format for macedonean is dd.mm.yyyy')
    userDate = input('What date would you like to re-format? \n >')
    return dateFormat, userDate

def checkDate(date, setup):
    date = date.strip()
    while date.find('  ') != -1:
        date = date.replace('  ', ' ')
    if setup == 'C':
        date = date.replace(' ', '-')
        date = date.replace('.', '-')
        date = date.replace('--', '-')
        dateList = date.split('-')
    
    else:
        date = date.replace(' ', '.')
        date = date.replace('-', '.')
        date = date.replace('..', '.')
        dateList = date.split('.')

    return dateList

def datePadding(D, M):
    if len(D) == 1:
        D = '0' + D
    if len(M) == 1:
        M = '0' + M
    return D, M