#Import modules
import input_process_13519191 as input_process
import matkul_13519191 as matkul
import setup_13519191 as setup

file = str(input("Masukkan nama file : ")) #Read file

input_process.process_input(file) #Processing file read and writing it to processed_input.txt

matkul_arr = setup.setup() #Setting up array of matkul based on input

urutan_matkul = [] #Intializing empty list for matkul's order

#Initializing variables
not_done = True #Used later to check if solution has been found
error = False #Used later to check if solution can't be met

while not_done :
    ada_nol = False #Boolean to check if there is one or multiple matkul has the degree of 0
    matkul_sems_list = [] #List to list all matkul in the semester
    array_of_derajat = [matkul_arr[i].derajat for i in range(len(matkul_arr))] #List of all matkul's derajat (used to prevent confusion of decrementing degrees)

    matkul_sems_list = [matkul_arr[i] for i in range(len(matkul_arr)) if matkul_arr[i].derajat == 0] #List of all matkul which has degree == 0

    #Check if solution can't be met
    if matkul_sems_list == [] :
        error = True
        print("Tidak bisa disusun")
        break
    urutan_matkul.append(matkul_sems_list)

    #Decreasing the degree of the matkuls connected to the matkul with degree=0
    for i in range(len(matkul_arr)):
        if (array_of_derajat[i] == 0) :
            matkul_arr[i].derajat -= 1
            for j in range(len(matkul_arr)):
                if i != j and (matkul_arr[i].name in matkul_arr[j].req_arr) :
                    matkul_arr[j].derajat -= 1

    #Decreasing the size of matkul_arr
    matkul_arr = [matkul_arr[i] for i in range(len(matkul_arr)) if matkul_arr[i].derajat >= 0]

    #Check if solution has been met or solution can't be met
    not_done = False
    for i in range(len(matkul_arr)):
        not_done = not_done or matkul_arr[i].derajat >= 0

#Printing out matkul list per semester if program is not error
if not(error) :
    index = 1
    for listmatkul in urutan_matkul :
        print("Semester %d : " % index)
        for i in range(len(listmatkul)-1):
            print(listmatkul[i].name, end=", ")
        print("%s." % listmatkul[len(listmatkul)-1].name)
        index += 1