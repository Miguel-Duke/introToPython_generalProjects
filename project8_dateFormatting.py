# Project 8 for intro to python by Mike Schwartz!
# Date formatting


'''
The ISO 8601 Standard date format for Information Interchange indicates that a date be written as such:

                        yyyy-MM-dd     (eg.   2012-07-02,     1999-12-05,    1998 -01-27 )      

                                    where yyyy represents the four digit year

                                    MM represents a two digit numerical month

                                    dd represents a two digit numerical day

 

Chinese date format is specified as:    yyyy-M-d

Macedonean date format is specified as:     d.M.yyyy.

                                   where yyyy represents the four digit year

                                    M represents a one  or two digit numerical month, as appropriate

                                    d represents a one or two digit numerical day, as appropriate

       

You are to write a program which converts dates  from Chinese  and Macedonean formats to ISO format.  The program will repeat the following until the user wishes to exit:

    *   ask the user which format they will be entering  (C - Chinese or M-Macedonean)

    *  accept the user input

    *   output the ISO version of the date that was input

 

Your program should handle user input errors such as:

  * leading blanks

  * blanks within the input string

Your program should delegate any large operations to functions which should be DEFINED AN IMPORTED MODULE, for example  month conversion to mFormat,  MMformat.
'''

import project8_dateFormattingModule    # At the start of the program we import the module that contains our functions.

gatheringInfo = True    # As long as this variable remains true the program will continue to run!

while gatheringInfo == True:
    dateFormat, userDate = project8_dateFormattingModule.getUserInput()   # Here we grab information from the user and make sure that any important values are set correctly 
    errorCheck = True                                                     # for times when someone wants to run the program repeatedly.
    reformatting = True
    contProgram = True
    while errorCheck == True:
        dateArray = project8_dateFormattingModule.checkDate(userDate, dateFormat)    # Here we have a function that verifies the format and characters in the date.
        if dateFormat == 'C':     # We set each variable to its date value here depending on the format we were given.
            year = dateArray[0]
            month = dateArray[1]
            day = dateArray[2]
        else:
            day = dateArray[0]
            month = dateArray[1]
            year = dateArray[2]
        
        if 0 > int(day) > 31 or 0 > int(month) > 12:    # A final check to make sure that the day and month values are reasonable.
            errorCheck = False
            reformatting = False
            contProgram = False
        else:
            errorCheck = False
    while reformatting == True:
        day, month = project8_dateFormattingModule.datePadding(day, month)    # Here we display the final output in the given ISO format.
        print('The ISO 8601 standard format for this date is:', year + '-' + month + '-' + day)
        reformatting = False
    while contProgram == True:    # Finally we ask them if the have another date in mind!
        keepFormatting = input('Do you have another date to format? \n Enter Y for yes \n Enter N for no \n >').capitalize()
        if keepFormatting == 'Y':
            contProgram = False
        elif keepFormatting == 'N':
            contProgram = False
            gatheringInfo = False
        else:
            continue    # This continue statement will keep asking them if they have another date until they provide valid input.
                

    
        
    