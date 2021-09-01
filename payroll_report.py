"""
Program #: Progamming Project 3B
Programmer: Justin Zhou
Due: 07/10/2021
CS 3A, Summer 2021
Description: (create program that functions as a payroll)
"""
totalgrosspay = 0
totalfed = 0
totalstate = 0
totalfica = 0
print("Enter the following information")
end = False
while end == False:
  user = int(input("\nPlease enter your name or type '0' to quit: "))
  if user < 0:
     user = int(input("Employee number may not be less than zero. \n Please reenter your name or type '0' to quit: "))
  if user == 0:
     print("Total Gross Pay:   ", totalgrosspay)
     print("Total Federal Tax:      ", totalfed)
     print("Total State Tax:      ", totalstate)
     print("Total FICA:            ", totalfica)
     print("Total Net Pay:      ", totalgrosspay - (totalstate + totalfica + totalfed))
     break
  else:
      grosspay = (float(input("Gross pay: ", )))
      if grosspay < 0:
          grosspay = float(input("Gross pay may not be less than zero. \n Re-enter Gross pay:"))
      fed = (float(input("Federal Withholding: ", )))
      if fed < 0:
          fed = float(input("Federal withholding may not be less than zero. \n Re-enter Federal Withholding:"))
      state = (float(input("State Withholding: ", )))
      if state < 0:
          state = float(input("State withholding may not be less than zero. \n Re-enter State Withholding:"))
      fica = (float(input("FICA Withholding: ", )))
      if fica < 0:
          fica = float(input("FICA withholding may not be less than zero. \n Re-enter FICA Withholding:"))
  if grosspay < fed+state+fica:
     print("ERROR: Withholdings cannot exceed gross pay. \n Please re-enter the data for this employee.")
     grosspay_error = (float(input("Gross pay: ", )))
     if grosspay_error < 0:
         grosspay_error = float(input("Gross pay may not be less than zero. \n Re-enter Gross pay:"))
     fed_error = (float(input("Federal Withholding: ", )))
     if fed_error < 0:
         fed_error = float(input("Federal withholding may not be less than zero. \n Re-enter Federal Withholding:"))
     state_error = (float(input("State Withholding: ", )))
     if state_error < 0:
         state_error = float(input("State withholding may not be less than zero. \n Re-enter State Withholding:"))
     fica_error = (float(input("FICA Withholding: ", )))
     if fica_error < 0:
         fica_error = float(input("FICA withholding may not be less than zero. \n Re-enter FICA Withholding:"))
  else:
     totalgrosspay = grosspay + grosspay_error + totalgrosspay
     totalfed = fed + fed_error + totalfed
     totalstate = state + state_error + totalstate
     totalfica = fica + fica_error + totalfica


""" ------------------- Sample Run --------------------
Enter the following information

Please enter your name or type '0' to quit: 7643
Gross pay: 2000
Federal Withholding: 500
State Withholding: 350
FICA Withholding: 2000
ERROR: Withholdings cannot exceed gross pay. 
 Please re-enter the data for this employee.
Gross pay: 2600
Federal Withholding: 50
State Withholding: -40
State withholding may not be less than zero. 
 Re-enter State Withholding:40
FICA Withholding: 50

Please enter your name or type '0' to quit: -2345
Employee number may not be less than zero. 
 Please reenter your name or type '0' to quit: 2345
Gross pay: 4000
Federal Withholding: 250
State Withholding: 50
FICA Withholding: 65

Please enter your name or type '0' to quit: 0
Total Gross Pay:    6600.0
Total Federal Tax:       300.0
Total State Tax:       90.0
Total FICA:             115.0
Total Net Pay:       6095.0
---------------------- End Sample Run ----------------"""