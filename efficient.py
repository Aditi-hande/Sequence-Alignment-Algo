from argparse import ArgumentParser
#from time import process_time
from time import *
import tracemalloc

delta = 30
alpha_dict = {
    'A' : {
        'A': 0,
        'C': 110,
        'G': 48,
        'T': 94
    },
    'C' : {
        'A': 110,
        'C': 0,
        'G': 118,
        'T': 48
    },
    'G' : {
        'A': 48,
        'C': 118,
        'G': 0,
        'T': 110
    },
    'T' : {
        'A': 94,
        'C': 48,
        'G': 110,
        'T': 0
    }
}

aligned_s1 = ''
aligned_s2 = ''

def getInput(filename="input.txt"):
    inputfile = open(filename, 'r')
    input = inputfile.readlines()
    inputfile.close()
    
    s1 = input[0].strip('\n')
    s2 = ''
    indices1 = []
    indices2 = []

    for i in range(1, len(input)):
        line = input[i].strip('\n')

        if line.isdigit():
            if len(s2) == 0:
                indices1.append(int(line))
            else:
                indices2.append(int(line))
        else:
            s2 = line

    return s1, s2, indices1, indices2

def generateString(s, indices):

    new_s = s

    for i in range(0, len(indices)):
        pre_s = new_s[0 : int(indices[i]) + 1]
        post_s = new_s[int(indices[i]) + 1 : len(new_s)]
        new_s = pre_s + new_s + post_s
    
    return new_s

def findOptimalSolValue(x, y, OPT):

    x_final = [] 
    y_final = []

    m = len(x)
    n = len(y)

    while m > 0 and n > 0:
        #diagonal move
        if OPT[m][n] == OPT[m-1][n-1] + alpha_dict[x[m - 1]][y[n - 1]]:
            x_final.append(x[m-1])
            y_final.append(y[n-1])
            m = m - 1
            n = n - 1
        #horizontal move
        elif OPT[m][n] == OPT[m-1][n] + delta:
            x_final.append(x[m-1])
            y_final.append("_")
            m = m - 1
        #vertical move
        elif OPT[m][n] == OPT[m][n-1] + delta:
            x_final.append("_")
            y_final.append(y[n-1])
            n = n - 1

    while (m > 0):
        x_final.append(x[m-1])
        y_final.append("_")
        m = m - 1
    
    while (n > 0):
        x_final.append("_")
        y_final.append(y[n-1])
        n = n - 1

    x_final.reverse()
    y_final.reverse()

    return ''.join([str(elem) for elem in x_final]), ''.join([str(elem) for elem in y_final])

def findDPSol(x, y):
    m = len(x)
    n = len(y)

    OPT = [[0 for i in range(n+1)] for j in range(m+1)]

    #Base Cases
    for i in range(0, m+1):
        OPT[i][0] = delta * i

    for i in range(0, n+1):
        OPT[0][i] = delta * i

    #recurrence relation
    for i in range (1, m+1):
        for j in range (1, n+1):
            OPT[i][j] = min(OPT[i - 1][j - 1] + alpha_dict[x[i - 1]][y[j - 1]], OPT[i - 1][j] + delta, OPT[i][j - 1] + delta)

    #find solution value
    x, y = findOptimalSolValue(x, y, OPT)

    return x, y, OPT[m][n]

def findEfficientDPSol(x, y):

    m = len(x)
    n = len(y)

    OPT = [[0 for i in range(2)] for j in range(m+1)]

    #Base Cases
    for i in range(0, m+1):
        OPT[i][0] = delta * i

    #recurrence relation
    for j in range(1, n+1):
        OPT[0][1] = j * delta

        for i in range(1, m+1):
            OPT[i][1] = min(OPT[i - 1][0] + alpha_dict[x[i - 1]][y[j - 1]], OPT[i - 1][1] + delta, OPT[i][0] + delta)

        for i in range (0,m + 1):
            OPT[i][0] = OPT[i][1]

    return OPT

def findDCSol(x, y):
    
    global aligned_s1, aligned_s2

    m = len(x)
    n = len(y)

    if m <= 2 or n <= 2:
        x_new, y_new, optSolCost = findDPSol(x, y)
        aligned_s1 = aligned_s1 + x_new
        aligned_s2 = aligned_s2 + y_new

        return 

    yl = y[0 : n//2]
    yr = y[n//2 : len(y)]

    OPT_l = findEfficientDPSol(x, yl)

    x_rev = x[::-1]
    yr_rev = yr[::-1]
    OPT_r = findEfficientDPSol(x_rev, yr_rev)

    OPT_r = OPT_r[::-1]

    min_val = OPT_l[0][1] + OPT_r[0][1]
    min_idx = 0

    for i in range(m + 1):
        if min_val > OPT_l[i][1] + OPT_r[i][1]:
            min_val = OPT_l[i][1] + OPT_r[i][1]
            min_idx = i
    
    xl = x[0 : min_idx]
    xr = x[min_idx : m+1]

    findDCSol(xl, yl)
    findDCSol(xr, yr)

def findOptimialSolution(s1, s2):
    findDCSol(s1, s2)

    solCost = 0
    for i in range(len(aligned_s1)):
        if aligned_s1[i] != "_" and aligned_s2[i] != "_":
            solCost = solCost + alpha_dict[aligned_s1[i]][aligned_s2[i]]
        else:
            solCost = solCost + delta

    return solCost

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("inputfilename", type=str)
    parser.add_argument("outputfilename", type=str)
    args = parser.parse_args()

    s1, s2, indices1, indices2 = getInput(args.inputfilename)

    s1 = generateString(s1, indices1)
    s2 = generateString(s2, indices2)
    
    startTime=time()
    tracemalloc.start ()

    #aligned_s1, aligned_s2, solCost = findDPSol(s1, s2)
    solCost = findOptimialSolution(s1, s2)
    
    time_taken = (time() - startTime) * 1000
    currentUsage,peakUsage = tracemalloc.get_traced_memory()
    peakUsage = peakUsage/1024
    
    with open(args.outputfilename, "w") as f:
        f.write (str(solCost) + "\n")
        f.write(aligned_s1 + "\n")
        f.write(aligned_s2 + "\n")
        f.write(str(time_taken) + "\n")
        f.write(str(peakUsage))