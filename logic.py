class Logic:

    __sumCredit = 0.00
    __sumGPA = 0.00

    def __init__(self, listCredit, listGPV):    # gpv-grade point value

        self.__listCredit = listCredit
        self.__listGPV = listGPV

        
    def getGPA(self):

        if len(self.__listCredit) == len(self.__listGPV):

            listGPA = []

            for i in range(len(self.__listCredit)):     # credit hours multiply by grade point value
                listGPA.append(self.__listCredit[i] * self.__listGPV[i])


            for item in self.__listCredit:      # get sum of credits
                self.__sumCredit += item
                
            for item in listGPA:      # get sum of GPA
                self.__sumGPA += item


            return round(self.__sumGPA/self.__sumCredit,2)
        else:
            return -1.00