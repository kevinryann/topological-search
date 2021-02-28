#Importing module
import matkul_13519191 as matkul

#This function is used to set up processed_file to be used later on
#By setting up, it means that this fnction will return a list of 
#class of matkuls derived from processed_input which will later 
#be used in the further part of the algorithm
def setup():
    matkul_arr = []
    with open("processed_input_13519191.txt", 'r') as file:
        for line in file :
            tmpline = line.strip() #Stripping the row in txt file
            tmp = tmpline.split(',') #Splitting row with ',' as key character
            for i in range(1, len(tmp)): 
                tmp[i] = tmp[i].lstrip() #lstrip to strip substring and removing ' ' in front of the same substring
            req_arr = []
            if len(tmp)>1 :
                for i in range(1, len(tmp)):
                    req_arr.append(tmp[i])
            tmp_matkul = matkul.matkul(tmp[0],req_arr) #Initializing matkul class
            matkul_arr.append(tmp_matkul) #Appending the matkul into a list which will be returned later in this function.
    return matkul_arr