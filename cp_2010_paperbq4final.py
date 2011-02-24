# Filename: cp_2010_paperbq4.py
# Name: Lee Hui Min
# Centre No / Index No: 3024 /
# Description: A report should be generated and displayed which will list the resources, which are still out on loan, grouped by date due back.

import time
import datetime
from collections import OrderedDict

def REPORT():
    try:
        # Open and read from LOAN.DAT for date due back, student id, student name
        loan_file = open("LOAN.DAT","r")

        # Read lines from loan file
        detail_loans = loan_file.readlines()
        
        # Open and read from RESOURCE.DAT for resource number, title, resource type
        resource_file = open("RESOURCE.DAT","r")

        # read heading line from resource file
        heading_line = resource_file.readline()

        # read the remaining records
        detail_resource = resource_file.readlines()

        # Loop number of records in LOAN.DAT (For loop)
        for record in detail_loans:
            # If evaluation field not empty
            if record[46:96] != (" " * 50):
                # Remove record from list
                detail_loans.remove(record)

        # Order the dictionary according to dates
        d = OrderedDict()

        # Min date = date due back of the first record in the loan file; Max date = date due back of the last record in the loan file
        minimum_date = time.strptime(detail_loans[0][40:46],"%d%m%y")
        minimum_date = time.strftime("%Y%m%d", minimum_date)
        min_year = int(minimum_date[0:4])
        min_month = int(minimum_date[4:6])
        min_day = int(minimum_date[6:8])
        minimum_date = datetime.date(year = min_year, month = min_month , day = min_day)
        
        maximum_date = time.strptime(detail_loans[-1][40:46],"%d%m%y")
        maximum_date = time.strftime("%Y%m%d", maximum_date)
        max_year = int(maximum_date[0:4])
        max_month = int(maximum_date[4:6])
        max_date = int(maximum_date[6:8])
        maximum_date = datetime.date(year = max_year, month = max_month, day = max_date)

        for n in range((maximum_date - minimum_date).days + 1):
            date = minimum_date + datetime.timedelta(n)
            print (date)
            d[date] = []

        # For the number of records:
        for records in detail_loans:
            #Create temp list for every valid record consisting resource number, title , resource type, student id and student name --> inefficient
            resource_number = records[0:5]
            student_id = records[5:10]
            student_name = records[10:40]
            for record in detail_resource:
                resource_no = record[0:5]
                if resource_no == resource_number:
                    title = record[5:35]
                    resource_type = record[41:42]
            if resource_type == 'C':
                resource_type = 'CD'
            else:
                resource_type = 'DVD'
            temp = [resource_number, title, resource_type, student_id, student_name]
            # Append the list to the valid date due back in the dictionary
            date_due_back = time.strptime(records[40:46], "%d%m%y")
            date_due_back = time.strftime("%Y-%m-%d", date_due_back)
            #d[date_due_back].append(temp)
            d[date_due_back] = temp

        for dates,lists in d.items():
##            dates = str(dates)
##            dates = time.strptime(dates,"%d%m%y")
            dates = time.strftime("%d-%m-%Y", dates)
            # Print date
            print(dates)
            # Print dotted line
            print('-' * 75)
            # For the number of lists in the dictionary
            for i in range(len(lists)):
                # Print the records in the dictionary with that key
                print(lists[i])
            print ("Number of resources: " + str(len(lists))) # number of resources

        # Close file
        loan_file.close()
        resource_file.close()

    except IOError:
        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

# main
if __name__ == "__main__":
    REPORT()
