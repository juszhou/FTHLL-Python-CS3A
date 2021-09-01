"""
Program #: Progamming Project 2A
Programmer: Justin Zhou
Due: 07/05/2021
CS 3A, Summer 2021
Description: (create program that computes a score for an applicant based on their test scores and GPA )
"""
SatMath = int(input('Enter your SAT Math score:'))
SatEng = int(input('Enter your SAT Eng score:'))
GPA = float(input('Enter your GPA:'))
MaxGPA = float(input('Enter the Max GPA:'))
ActWriting = int(input('Enter your ACT Eng score:'))
ActMath = int(input('Enter your ACT Math score:'))
ActReading = int(input('Enter your ACT reading score:'))
ActScience = int(input('Enter your ACT science score:'))
ActGPA = float(input('Enter your GPA:'))
ActMaxGPA = float(input('Enter the Max GPA:'))
totalsat = SatEng + SatMath
totalact = ActMath + ActReading + ActScience + ActWriting
ovrsat = 2/24 * totalsat
ovract = 2/1.8 * totalact
satgpa = GPA/MaxGPA * 100
actgpa = ActGPA/ActMaxGPA * 100
oversat = ovrsat + satgpa
overact = ovract + actgpa


print('Information for the applicant:')
print('SAT scores:')
print('  SAT math?', SatMath)
print('  SAT verbal?', SatEng)
print('  overall GPA', GPA)
print('  max GPA?', MaxGPA)
print()
print('ACT scores:')
print('  ACT English?', ActWriting)
print('  ACT math?', ActMath)
print('  ACT reading?', ActReading)
print('  ACT science?', ActScience)
print('  overall GPA', ActGPA)
print('  max GPA?', ActMaxGPA)
print()
print('Overall score(SAT)=', oversat)
print('Overall score (ACT) =', overact)

""" ------------------- Sample Run --------------------

Enter your SAT Math score:450
Enter your SAT Eng score:530
Enter your GPA:3.4
Enter the Max GPA:4.0
Enter your ACT Eng score:25
Enter your ACT Math score:20
Enter your ACT reading score:18
Enter your ACT science score:15
Enter your GPA:3.5
Enter the Max GPA:4.0

Information for the applicant:
SAT scores:
 SAT math? 450
 SAT verbal? 530
 overall GPA 3.4
 max GPA? 4.0

ACT scores:
 ACT English? 25
 ACT math? 20
 ACT reading? 18
 ACT science? 15
 overall GPA 3.5
 max GPA? 4.0

Overall score(SAT)= 166.66666666666666
Overall score (ACT) = 174.16666666666669

---------------------- End Sample Run ----------------"""

