import random




def rabbitGrowth():
   
    global CURRENTRABBITPOP
    
    p_rabbit = 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)
    for rabbit in range(CURRENTRABBITPOP):
        if random.random()<p_rabbit:
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():

    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    p_eat = CURRENTRABBITPOP/float(MAXRABBITPOP)
    
    for fox in range(CURRENTFOXPOP):
        if random.random()<p_eat:
            if CURRENTRABBITPOP > 10:
                p_fox = 1/3.0
                CURRENTRABBITPOP -= 1
                if random.random()<p_fox:
                    CURRENTFOXPOP += 1
        else:
            p_die = 9/10.0
            if random.random()<p_die:
                if CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):

    rabbit_pop = []
    fox_pop = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_pop.append(CURRENTRABBITPOP)
        fox_pop.append(CURRENTFOXPOP)
    return (rabbit_pop, fox_pop)
    
