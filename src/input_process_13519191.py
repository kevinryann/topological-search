#Function to process input file
#By processing, it means that this function is used to remove '.' character from the input txt
#and store a processed input into an external txt file called processed_input.txt

def process_input(file) :
    directory = "../test/"+file
    with open(directory, 'r') as infile, open("processed_input_13519191.txt", 'w') as outfile :
        tmp = infile.read().replace('.', '') #Replacing '.' with an empty string
        outfile.write(tmp) #Writing it to processed_input.txt
