#Import modules
import os
import csv

#Set path for csv file
employeedatapath = os.path.join('..','Resources','employeedata.txt')

#Open file, skip header
with open (employeedatapath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
    #Add CSV data to lists
    employeeid = []
    employeename =[]
    employeedob = []
    employeessn = []
    employeestate =[]
    
    for row in csvreader:
        employeeid.append(row[0])
        employeename.append(row[1])
        employeedob.append(row[2])
        employeessn.append(row[3])
        employeestate.append(row[4])

    #Split full names into list of first and last
    firstname = [name.split()[0] for name in employeename]
    lastname = [name.split()[1] for name in employeename]

    #Convert DOB into required format
    newdob = []
    for date in employeedob:
        newdob.append((date.strip()[5:7])+"/"+(date.strip()[8::]+"/"+(date.strip()[:4])))

    #Replace first 5 digits of SSN with *
    newssn =[]
    for ssn in employeessn:
        newssn.append(('***-**-')+ssn.strip()[7::])

    #Change state to abbreviation
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
    newstate =[us_state_abbrev.get(state) for state in employeestate]

     #zip new data togeter
    newdata = zip(employeeid,firstname,lastname,newdob,newssn,newstate)

#Create path and write text file
outputfile = os.path.join("Output","formattedempdata.txt")

with open(outputfile,"w",newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(newdata)