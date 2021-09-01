"""
Program #: Progamming Project 5
Programmer: Justin Zhou
Due: 07/26/2021
CS 3A, Summer 2021
Description: (Create a class that includes a patient and procedure functionality)
"""

#  imports
from Patient import Patient
from Procedure import Procedure

#  initializing each class
sample_patient = Patient('James', 'Edward', 'Jones', '123 Main Street',
                         'Billings', 'Montana', '59000', '406-555-1212')
sample_proc = Procedure('Physical Exam', '8-24-2019', 'Dr. Irvine', 250)
sample_proc2 = Procedure('X-ray', '8-24-2019', 'Dr. Jamison', 500)
sample_proc3 = Procedure('Blood test', '8-24-2019', 'Dr. Smith', 200)

#  printing data
print(str(sample_patient))
print()
print(str(sample_proc))
print()
print(str(sample_proc2))
print()
print(str(sample_proc3))

#  printing total cost
proc_cost = sample_proc.charge
proc2_cost = sample_proc2.charge
proc3_cost = sample_proc3.charge
total_cost = sample_proc.charge + sample_proc2.charge + sample_proc3.charge
print('\nThe total charges of the three procedures is: ', total_cost)

""" ------------------- Sample Run --------------------
First Name: James
Middle Name: Edward
Last Name: Jones
Address: 123 Main Street
City: Billings
State: Montana
ZIP: 59000
Phone: 406-555-1212

Procedure:Physical Exam
ExamDate:8-24-2019
Practitioner:Dr. Irvine
Charge:250

Procedure:X-ray
ExamDate:8-24-2019
Practitioner:Dr. Jamison
Charge:500

Procedure:Blood test
ExamDate:8-24-2019
Practitioner:Dr. Smith
Charge:200

The total charges of the three procedures is:  950

Process finished with exit code 0

---------------------- End Sample Run ----------------"""
