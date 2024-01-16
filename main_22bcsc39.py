from typing import List, Dict, Optional
import re


def readPatientsFromFile(filePath):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    #######################
    #### PUT YOUR CODE HERE
    #######################
    
    """
    with open(filePath, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            patient_id = int(parts[0])
            visit_data = parts[1:]
            if patient_id not in patients:
                patients[patient_id] = []
            patients[patient_id].append(visit_data)

    return patients
    """   
    
    try:
        with open(filePath, 'r') as file:
            for line_num, line in enumerate(file,1):
                line = line.strip()
                fields = line.split(',')
                

                # Check if the number of fields is correct
                if len(fields) != 8:
                    print(f"Invalid number of fields ({len(fields)}) in line: {line_num}")
                    continue

                try:
                    patient_id = int(fields[0])
                    visit_date = fields[1]
                    temperature = float(fields[2])
                    heart_rate = int(fields[3])
                    respiratory_rate = int(fields[4])
                    systolic_bp = int(fields[5])
                    diastolic_bp = int(fields[6])
                    spo2 = int(fields[7])
                except ValueError:
                    print(f"Invalid data type in line: {line_num}")
                    continue

                # Check data ranges
                #condition to check valid temperature ranges
                if not (35 <= temperature <= 42):
                    print(f"Invalid temperature value ({temperature}) in line: {line_num}")
                    continue
                #condition to check valid heart rate ranges
                if not (30 <= heart_rate <= 180):
                    print(f"Invalid heart rate value ({heart_rate}) in line: {line_num}")
                    continue
                #condition to check valid respiratory rate ranges
                if not (5 <= respiratory_rate <= 40):
                    print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line_num}")
                    continue
                #condition to check valid systolic blood pressure ranges
                if not (70 <= systolic_bp <= 200):
                    print(f"Invalid systolic blood pressure value ({systolic_bp}) in line: {line_num}")
                    continue
                #condition to check valid diastolic blood ranges
                if not (40 <= diastolic_bp <= 120):
                    print(f"Invalid diastolic blood pressure value ({diastolic_bp}) in line: {line_num}")
                    continue
                #condition to check valid oxygen saturation ranges
                if not (70 <= spo2 <= 100):
                    print(f"Invalid oxygen saturation value ({spo2}) in line: {line_num}")
                    continue

                # Add visit data to the dictionary
                if patient_id not in patients:
                    patients[patient_id] = []
                patients[patient_id].append(
                    [visit_date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, spo2])

    except FileNotFoundError:
        print(f"The file '{filePath}' could not be found.")
    except Exception as e:
        print("An unexpected error occurred while reading the file.")

    return patients

                
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    
    # CHECK IF patientId IS VALID

    if patientId!=0 and patientId not in patients:
        print("patient with id {} not found".format(patientId))
        return 


    for patient_id, visits in patients.items():
        if patientId == 0 or patient_id==patientId:
            print(f"Patient ID: {patient_id}\n")     # CONDITION TO PRINT patientId
            
            for visit in visits:
                if len(visit) == 7:
                    date, temp, hr, rr, sbp, dbp, spo2 = visit

                    # DISPLAYS PATIENT DATA

                    print(f" Visit Date: {date}")
                    print(f" Temperature: {temp} C")
                    print(f" Heart Rate: {hr} bpm")
                    print(f" Respiratory Rate: {rr} bpm")
                    print(f" Systolic Blood Pressure: {sbp} mmHg")
                    print(f" Diastolic Blood Pressure: {dbp} mmHg")
                    print(f" Oxygen Saturation: {spo2}%\n")
   
                    # CONDITION IF INVALID visit data FORMAT
                else:
                    print("Invalid visit data format.")  
             
    
    
            

def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    

    # TO CHECK THAT patients IS A DICTIONARY
    if not isinstance(patients,dict):
        print("Error: 'patients' should be a dictionary.")
        return
    
    # TO CHECK IF ENTERED patientId is valid
    try:
        patientId = int(patientId)
    except ValueError:
        print("Error: 'patientId' should be an integer.")
        return
    
    # TO CHECK IF DATA FOUND FOR SPECIFIC patientId
    if patientId != 0 and patientId not in patients:
        print("No data found for patient with ID {}.".format(patientId))
        return

    # Calculate averages for each vital sign
    temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = num_visits = 0

    if patientId == 0:                 # IF patientId IS ZERO,THEN IT PRINTS AVERAGE DATA FOR ALL PATIENTS
        print("data for all patients:")
        for visits in patients.values():
            for visit in visits:
                temp_sum += visit[1]
                hr_sum += visit[2]
                rr_sum += visit[3]
                sbp_sum += visit[4]
                dbp_sum += visit[5]
                spo2_sum += visit[6]
                num_visits += 1
        patient_name = "All Patients"
    else:                             # ELSE IT PRINTS AVERAGE DATAS FOR ANY SPECIFIC ID
        visits = patients[patientId]
        for visit in visits:
            temp_sum += visit[1]
            hr_sum += visit[2]
            rr_sum += visit[3]
            sbp_sum += visit[4]
            dbp_sum += visit[5]
            spo2_sum += visit[6]
            num_visits += 1
        patient_name = "Patient {}".format(patientId)
    
    # IF TOTAL VISIT IS ZERO THEN NO DATA FOUND WILLL BE PRINTED
    if num_visits == 0:
        print("No data found for {}.".format(patient_name))
        return
    
    # PRINT THE AVERAGE VALUES OF ANY ID

    print("Vital Signs for {}:".format(patient_name))
    print(" Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
    print(" Average heart rate:", "%.2f" % (hr_sum / num_visits), "bpm")
    print(" Average respiratory rate:", "%.2f" % (rr_sum / num_visits), "bpm")
    print(" Average systolic blood pressure:", "%.2f" % (sbp_sum / num_visits), "mmHg")
    print(" Average diastolic blood pressure:", "%.2f" % (dbp_sum / num_visits), "mmHg")
    print(" Average oxygen saturation:", "%.2f" % (spo2_sum / num_visits), "%")



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
   
    try:
        # Check date format
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
            return
        
        # extract year, month, and day
        year, month, day = map(int, date.split('-'))
        
        # Check if the date is valid
        if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
            print("Invalid date. Please enter a valid date.")
            return
        
        # Check other input values

        # CHECK IF TEMPERATURE IS VALID
        if not (35.0 <= temp <= 42.0):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return
        # CHECK IF HEART RATE IS VALID
        if not (30 <= hr <= 180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return
         # CHECK IF RESPIRATORY RATE IS VALID
        if not (5 <= rr <= 40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return
         # CHECK IF SYSTOLIC BLOOD PRESSURE IS VALID
        if not (70 <= sbp <= 200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return
         # CHECK IF DIASTOLIC BLOOD PRESSURE IS VALID
        if not (40 <= dbp <= 120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return
         # CHECK IF OXYGEN SATURATION IS VALID
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return
        
        # Add new visit data to the dictionary

        new_visit = [date, temp, hr, rr, sbp, dbp, spo2]
        if patientId not in patients:
            patients[patientId] = []
        patients[patientId].append(new_visit)
        
        # Append new data to the patients.txt file

        with open(fileName, 'a') as file:
            file.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")
        
        # TO CHECK IF ANY UNECPECTED ERROR OCCURED
        
        print(f"Visit is saved successfully for Patient #{patientId}")
    except Exception as e:
        print("An unexpected error occurred while adding new data:", e)


   
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    
    #condition to check patients id from year,month 
    for patient_id, patient_visits in patients.items():
        for visit in patient_visits:
            visit_date = visit[0]
            visit_year, visit_month,_ = visit_date.split('-')
            
            if year is None or (year is not None and visit_year == str(year)):
                if month is None or (month is not None and visit_month == str(month).zfill(2)):
                    visits.append((patient_id, visit))



    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    #### PUT YOUR CODE HERE
    #######################

    for patient_id, visits in patients.items():
        for visit in visits:
            heart_rate = visit[2] # Heart rate is at index 2 in the visit data
            systolic_bp = visit[4] # Systolic BP is at index 4 in the visit data
            diastolic_bp = visit[5] # Diastolic BP is at index 5 in the visit data
            oxygen_saturation = visit[6] # Oxygen saturation is at index 6 in the visit data

            if (heart_rate > 100 or heart_rate < 60 or
                systolic_bp > 140 or diastolic_bp > 90 or
                oxygen_saturation < 90):
                followup_patients.append(patient_id)
                break # No need to check other visits for this patient

    return followup_patients


  


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
   
   #delete specific patient id from the text file
   
    if patientId in patients:
        del patients[patientId]
        try:
            with open(filename, 'w') as file:
                for patient_id, visits in patients.items():
                    for visit in visits:
                        line = f"{patient_id},{','.join(map(str, visit))}\n"
                        file.write(line)
            print(f"Data for patient {patientId} has been deleted.")   
        except Exception as e:                                         #exception handling
            print("An error occurred while updating the file:", e)     #condition to print if error occured
    else:
        print(f"No data found for patient with ID {patientId}")        #prints no data found






###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            #patientID=int(patientID)
            displayStats(patients, patientID)
        elif choice == '5':
          year = input("Enter year (YYYY) (or 0 for all years): ")
          month = input("Enter month (MM) (or 0 for all months): ")
          if month == '0':
            visits = findVisitsByDate(patients, int(year) if year != '0' else None)
          else:
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                  int(month))
          if visits:
            for visit in visits:
              print("Patient ID:", visit[0])
              print(" Visit Date:", visit[1][0])
              print(" Temperature:", "%.2f" % visit[1][1], "C")
              print(" Heart Rate:", visit[1][2], "bpm")
              print(" Respiratory Rate:", visit[1][3], "bpm")
              print(" Systolic Blood Pressure:", visit[1][4], "mmHg")
              print(" Diastolic Blood Pressure:", visit[1][5], "mmHg")
              print(" Oxygen Saturation:", visit[1][6], "%")
          else:
            print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients_new.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
