import numpy as np

rnd = np.random.RandomState(7)

ArmATrueProb = 0.4
ArmBTrueProb = 0.5

priorA = [1,1]
priorB = [1,1] 

for trial in range(100):
    sampleA = rnd.beta(priorA[0], priorA[1])
    sampleB = rnd.beta(priorB[0], priorB[1])
    
    SuccCheck = rnd.random_sample()
    
    if sampleA > sampleB:
        if SuccCheck<ArmATrueProb:
            priorA[0] = priorA[0]+1;
        else:
            priorA[1] = priorA[1]+1;
    else:
        if SuccCheck<ArmBTrueProb:
            priorB[0] = priorB[0]+1;
        else:
            priorB[1] = priorB[1]+1;
        
    if trial%10 == 9:
        print("run " + str(trial))
        print("A =  Beta(" + str(priorA[0]) + "," + str(priorA[1]) + ")")
        print("B =  Beta(" + str(priorB[0]) + "," + str(priorB[1]) + ")")
