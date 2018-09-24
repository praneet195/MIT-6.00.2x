def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,numTrials):
   avg = [0] * 300
   for i in range(numTrials):
       viruses = []
       for j in range(numViruses):
           viruses.extend([SimpleVirus(maxBirthProb, clearProb)])

       patient = Patient(viruses, maxPop)
       for k in range(300):
           avg[k] = float(avg[k]) + patient.update()
    
   for l in range(300):
       avg[l] = avg[l] / float(numTrials)


   pylab.figure("SimpleVirus simulation")
   pylab.title("SimpleVirus simulation")
   pylab.plot(avg,label = "SimpleVirus")
   pylab.xlabel("Time Steps")
   pylab.ylabel("Population of virus")
   pylab.legend()
   pylab.show()
