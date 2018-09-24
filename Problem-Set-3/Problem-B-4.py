class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
      

        # TODO
        super().__init__(maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
        return self.mutProb

    def isResistantTo(self, drug):
     
        
        # TODO
        try:
            return self.resistances[drug]
        except KeyError:
            return False


    def reproduce(self, popDensity, activeDrugs):
       
        # TODO
        self.popDensity = popDensity
        self.activeDrugs = activeDrugs
        if all([self.isResistantTo(i) for i in self.activeDrugs]) == True:
            probab = random.random()
            if probab <= self.maxBirthProb * (1 - self.popDensity):
                new_resistances = self.resistances.copy()
                for key in self.resistances.keys():
                    probabi = random.random()
                    if probabi <= self.getMutProb():
                        if self.resistances[key] == True:
                            new_resistances[key] = False
                        else:
                            new_resistances[key] = True
                return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
            else:
                raise NoChildException
        else:
            raise NoChildException
            

class TreatedPatient(Patient):
  

    def __init__(self, viruses, maxPop):
       

        # TODO
        super().__init__(viruses, maxPop)
        self.prescription = []


    def addPrescription(self, newDrug):
       
        # TODO
        self.newDrug = newDrug
        if self.newDrug not in self.prescription:
            self.prescription.append(self.newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.prescription


    def getResistPop(self, drugResist):
     

        # TODO
        self.drugResist = drugResist
        resist_pop = 0
        for i in self.viruses:
            if all([i.isResistantTo(j) for j in self.drugResist]) == True:
                resist_pop += 1
        return resist_pop


    def update(self):
       

        # TODO
        viruses_copy = self.viruses[:]
        for i in viruses_copy:
            if i.doesClear() == True:
                self.viruses.remove(i)
                
        popDensity = len(self.viruses)/self.maxPop
        
        viruses_copy_2 = self.viruses[:]
        for j in viruses_copy_2:
            try:
                j.reproduce(popDensity, self.prescription)
                self.viruses.append(j)
            except NoChildException:
                continue    
                

# correctCorrect
