#Initializing a class for matkul whick contains attributes as following :
#An array of required matkuls or requisites (req_arr)
#Name of the matkul (name)
#Degree of the matkul (derajat)

class matkul:
    def __init__(self, name, req):
        self.req_arr = []
        self.name = name
        self.derajat = len(req)
        for char in req :
            self.req_arr.append(char) #Appending all required matkul to the array