class Patient():

    def __init__(self, ssn, dob, insurance_number, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__insurance_number = insurance_number
        self.full_name = first_name + ' ' + last_name
        self.__address = address
        

        
    @property
    def ssn(self):
        return self.__ssn

    @property
    def dob(self):
        return self.__dob

    @property
    def insurance_number(self):
        return self.insurance_number

    # @property
    # def first_name(self):
    #     return self.__first_name

    # @property
    # def last_name(self):
    #     return self.__last_name

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""
    
    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string for the patient's address.")


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# will not change state of object
# cashew.ssn = "838-31-2256"
# cashew.dob = "01-30-90"

# printing will work
# print(cashew.ssn)
# print(cashew.dob)

# These two statements should output nothing (errors?)
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
# print(cashew.full_name)   # "Daniela Agnoletti"

print(dir(cashew))

