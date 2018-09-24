def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
    avg = [0] * 300
    avg1 = [0] * 300
    for i in range(numTrials):
        viruses = []
        for j in range(numViruses):
            viruses.extend([ResistantVirus(maxBirthProb, clearProb , resistances, mutProb )])

        patient = TreatedPatient(viruses, maxPop)
        for k in range(300):
            if k == 150:
                patient.addPrescription("guttagonol")  
            patient.update()
            avg[k] = float(avg[k]) + patient.getTotalPop()
            avg1[k] = float(avg1[k]) + patient.getResistPop(["guttagonol"]) 
     
    for l in range(300):
        avg[l] = avg[l] / float(numTrials)
        avg1[l] = avg1[l] / float(numTrials)
        
    pylab.figure("ResistantVirus simulation")
    pylab.title("ResistantVirus simulation")
    pylab.plot(avg,label = "Total Virus Population")
    pylab.plot(avg1,label = "Resistant Virus Population")
    pylab.xlabel("time step")
    pylab.ylabel("#viruses")
    pylab.legend()
    pylab.show()
