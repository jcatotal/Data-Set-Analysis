import csv
import collections

#Opens the CSV File for Requests
a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
csvReader = csv.reader(a)

#Opens the CSV File for Stations
b = open('Fire_Stations.csv', 'r+')
csvReader2 = csv.reader(b)

#Simple Intro
def main():
    print('====================================')
    print('\n')
    print('      FIRE DEPARTMENT DATA SET      ')
    print('\n')
    print(' This program allows you to see and ')
    print('   explore a data set of Chicago.   ')
    print('\n')
    print('====================================')
    print('\n \n')
    input('     Press any key to continue.     ')
    print('\n')
    options()


#GUI
def options():
    print('\n===== Options =====\n')
    print('1. Display number of Fire Requests in Data Set.\n')
    print('2. Display number of EMS requests in Data Set.\n')
    print('3. Display number of Inspection Requests in Data Set.\n')
    print('4. Display number of Fire Stations in the City of Chicago.\n')
    print('5. Show a List of all Fire Stations.\n')
    print('6. Access function that counts requests within a certain day.\n')
    print('7. Close this program.\n')
    x = int(input('Please enter number of option: '))
    if x == 1:
        fire_count()
    elif x == 2:
        ems_count()
    elif x == 3:
        inspect_count()
    elif x == 4:
        station_count()
    elif x == 5:
        StationList()
    elif x == 6:
        dayData()
    elif x == 7:
        exit()
    else:
        print('That is not a valid option. \nPlease enter a valid number.')

    
##Used this as reference when understanding csv 
'''
a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
csvReader = csv.reader(a)

def first_line():
    head = next(csvReader)
    first = next(csvReader)
    print(first)

def three_line():
    head = next(csvReader)
    first = next(csvReader)
    second = next(csvReader)
    third = next(csvReader)
    print(first)
    print(second)
    print(third)

'''
#Counts the number of fire requests
def fire_count():
    a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
    csvReader = csv.reader(a)
    fire_count = 0
    for row in csvReader:
        if row[2]== 'FIRE':
            fire_count = fire_count + 1

    print('\n===================')
    print('\nNumber of Fire Requests in Data Set: ', fire_count)
    input('\nPress any key to return to Options.')
    options()

#Counts the number of ems requests
def ems_count():
    a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
    csvReader = csv.reader(a)
    ems_count = 0
    for row in csvReader:
        if row[2] == 'EMS':
            ems_count = ems_count + 1

    print('\n===================')
    print('\nNumber of Emergency Medical Service Requests in Data Set: ', ems_count)
    input('\nPress any key to return to Options.')
    options()

#Counts the number of inspection requests
def inspect_count():
    a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
    csvReader = csv.reader(a)
    inspect = 0
    for row in csvReader:
        if row[2] == 'INSPECTION':
            inspect = inspect + 1

    print('\n===================')
    print('\nNumber of Inspection Requests in Data Set: ', inspect)
    input('\nPress any key to return to Options.')
    options()

#Counts the number of fire stations
def station_count():
    b = open('Fire_Stations.csv', 'r+')
    csvReader2 = csv.reader(b)
    stations = 0
    for row in csvReader2:
        if row[2] == 'CHICAGO':
            stations = stations + 1

    print('\n===================')
    print('\nNumber of Fire Stations in Chicago: ', stations)
    input('\nPress any key to return to Options.')
    options()

#Shows CSV file for fire stations
def StationList():
    b = open('Fire_Stations.csv', 'r+')
    csvReader2 = csv.reader(b)
    for row in csvReader2:
        print(row)

    print('\n===================')
    input('\nPress any key to return to Options.')
    options()

#Counts the number of Requests with a day
def dayData():
    a = open('FOIA_Request_Log_-_Fire.csv', 'r+')
    csvReader = csv.reader(a)

    print('Use this function to view a number of requests')
    print('   within a valid date within the Data Set.   ')
    print('     i.e dates that do not contain #####      ')
    dayCount = 0
    x = str(input('\nEnter a date in X/X/XXXX format (ex. 9/9/2015): \n'))
    for row in csvReader:
        if row[3] == x:
            dayCount = dayCount + 1

    if dayCount == 0:
        print('This is not a valid date in the Data Set. Please enter a valid date.')
        dayData()
    else:
        print('\nThe number of requests made on ', x ,'is: ', dayCount)

    options()

    
main()

    


    
