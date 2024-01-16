
# Information System for Electronic Medical Records
## Table of Contents

 Function 1: readPatientsFromFile()

Function 2: displayPatientData()

Function 3: displayStats()

Function 4: addPatientData() 

Function 5: findVisitsByDate()

Function 6: findPatientsWhoNeedFollowUp()

Function 7: deleteAllVisitsOfPatient()

 

# Program Features
The program will provide the following features, plus more as described in 
the function sections below:
• A function to read patient data from a plaintext file.
• A function to display various statistics about the patients, such as the 
average vital signs about the patients or for a specific patient.
• A function to display patient data for all patients or for a specific 
patient by ID.
• A function to add new patient data to the patient list.
• A function to find patient visits in a certain month or year
• A function to find patients who need follow-ups depending on their 
vital statistics
• A text-based interface to list the patients and allow the user to select 
which feature they would like to use.


# WALKTHROUGH

### 1) Function 1: readPatientsFromFile()
This function reads patient data from a plaintext file and returns a dictionary, 
returns a dictionary where each key is a unique patient ID and the 
corresponding values are 2-dimensional lists storing information about 
each visit (where each visit's information is stored in its own inner-list)

### 2)   Function 2: displayPatientData()
This function displays patient data for all patients or a given patient ID
### 3) Function 3: displayStats()
This function prints the average of each vital sign for all patients or for a specified patient
### 4) Function 3: displayStats()
This function prints the average of each vital sign for all patients or for a 
specified patient.
### 5) Function 4: addPatientData()
This function adds new patient data to the patients dictionary and appends 
this same data to the text file
### 6) Function 5: findVisitsByDate()
This function finds the visits by date provided and returns a list of tuples. See 
below.
### 7) Function 6: findPatientsWhoNeedFollowUp()
### 8)  Function 7: deleteAllVisitsOfPatient()


## Screenshots

![image](https://github.com/jibijen/python_project/assets/148977004/555ff33b-a9ec-4792-85ab-aa825178fcf9)

