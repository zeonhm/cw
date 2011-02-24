# Filename: cp_2010_paperbq3.py
# Name: Lee Hui Min
# Centre No / Index No: 3024 /
# Description: Read from URESOURCE.DAT, get extra info based on loan, perform validation and append to LOAN.DAT

import time
import datetime

def CREATELOAN():
##    try:
##        # Open loan file for append
##        loan_file = open("LOAN.DAT","r")
##
##        # Initialise student id list
##        student_id_list = []
##        student_detail_lines = loan_file.readlines()
##
##        # Loop through each record for the student id
##        for student_line in student_detail_lines:
##            # Slice to get student id in loan file
##            stu_id = student_line[5:10]
##            # Append student id to student id list
##            student_id_list.append(stu_id)
##        
##    except IOError:
##        # display file input/output errors
##        print("Error! Cannot read from input file or write to output file.")
        
    try:
        # Open updated resource file for reading
        uresource_file = open("URESOURCE.DAT","r")
        
        # Skip first line and read the other lines
        heading_line = uresource_file.readline()
        
        # Read record details
        detail_lines = uresource_file.readlines()
        
        # Initialise resource number list
        resourceno_list = []
        
        # Loop through each record
        for resource_line in detail_lines:
            # Slice to get resource number
            resource_no = resource_line[0:5]
            
            # Append resource number to resource number list
            resourceno_list.append(resource_no)
            
        # Open loan file for append
        loan_file = open("LOAN.DAT","a")

        # Initialise student id list for counting
        student_id_list = []

        # Allow multiple loans
        userinput = False
        while not userinput:
            # Get and Validate resource number
            valid_resourceno = False
            while not valid_resourceno:
                resourceno = input("Enter resource number: ")
                # Presence check
                if len(resourceno) == 0:
                    print("Invalid! Empty input. Please try again.")
                # Length check
                elif not len(resourceno) == 5:
                    print("Invalid! Input should be exactly 5 characters. Please try again.")
                # Isdigit check
                elif not resourceno.isdigit():
                    print("Invalid! Must be a number. Please try again.")
                # Compare with resource number list
                elif resourceno not in resourceno_list:
                    print("Invalid! Resource does not exist. Please try again.")
                else:
                    valid_resourceno = True
                    
            # Get and Validate Student ID
            valid_student_id = False
            while not valid_student_id:
                student_id = input("Enter Student ID: ")
                # Presence check
                if len(student_id) == 0:
                    print("Invalid! Empty input. Please try again.")
                # Length check (5 characters)
                elif not len(student_id) == 5:
                    print("Invalid! Input should be exactly 5 characters. Please try again.")
                # Check first character is 'S'
                elif not student_id[0].upper() == 'S':
                    print("Invalid! First character should be 's' or 'S'. Please try again.")
                # Check that the next 4 characters isdigit
                elif not student_id[1:5].isdigit():
                    print("Invalid! Student ID should consist for 4 digits after S. Please try again.")
                # Check number of records loaned by student
                elif not student_id_list.count(student_id) < 3:
                    print("Invalid! Student has already loaned a maximum of 3 records. Please try again.")
                else:
                    valid_student_id = True

            # Add student id into list
            student_id_list.append(student_id)
                    
            # Get and Validate Student Name
            valid_student_name = False
            while not valid_student_name:
                student_name = input("Enter Student Name: ")
                # Presence check
                if len(student_name) == 0:
                    print("Invalid! Empty input. Please try again.")
                # Length check (30 characters)
                elif len(student_name) > 30:
                    print("Invalid! Student Name should be no longer than 30 characters. Please try again.")
                else:
                    valid_student_name = True
                    
            # Auto Generate/ Calculate DateDueBack (DDMMYY)
            current_date = datetime.date.today()
            date_due_back = current_date + datetime.timedelta(7)
            date_due_back = date_due_back.strftime("%d%m%y")

            # Initial empty field for evaluation
            evaluation = ""

            # Write valid records into file
            loan_file.write("{0:5s}{1:5s}{2:30s}{3:6s}{4:50s}".format(resourceno, student_id, student_name, date_due_back, evaluation) + "\n")
            
            # Additional loans
            loan = input("Do you still wish to enter loans (Y for yes, N for no): ")
            if loan.upper() == 'N':
                userinput = True
        
        # Close file
        uresource_file.close()
        loan_file.close()

    except IOError:
        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

# main
if __name__ == "__main__":
    CREATELOAN()

    
