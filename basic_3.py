import os
from time import process_time
import argparse
import psutil

# fixed cost for space
delta = 30
# fixed cost for mismatch
dict_alpha = {
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

# generate actual strings from the baseStrings given
def GenerateString (baseString, indices):
    multipliedString = baseString

    for i in range (0, len (indices)):

        pre_index = multipliedString[0 : int(indices[i]) + 1]
        post_index = multipliedString[int(indices[i]) + 1 :]
        multipliedString = pre_index + multipliedString + post_index
    
    #print(multipliedString)
    return multipliedString
    
def getInputFile(filename="input.txt"):
    # inputfile = open("input.txt", 'r')
    # input = inputfile.readlines()
    # inputfile.close()
    
    with open(filename, 'r') as f:
        input = f.readlines()
    f.close ()
    
    string1 = input[0].strip('\n')
    string2 = ''
    indices1 = []
    indices2 = []

    for i in range(1, len(input)):
        line = input[i].strip('\n')

        if line.isdigit():
            if len(string2) == 0:
                indices1.append(int(line))
            else:
                indices2.append(int(line))
        else:
            string2 = line

    # print(string1)
    # print(string2)
    # print(indices1)
    # print(indices2)

    return s1, s2, indices1, indices2
    
def BasicDPAlignment(string1, string2)
    
    m = len (string1)
    n = len (string2)
    
    matchedString1 = ''
    matchedString2 = ''
    
    dp = [[0 for i in range (n + 1)] for i in range (m + 1)]
    
    #initializing the dp matrix for cases when one of the string is of length 0
    for i in range(m + 1):
        dp[i][0] = i * delta
        
    for i in range (n + 1):
        dp[0][i] = i * delta
    
    #actual dp calculation to find minnimum cost for vertical/digonal/horizontal cases
    for i in range (1, m + 1):
        for j in range (1, n + 1):
        dp[i][j] = min (dp[i-1][j] + delta, dp[i][j - 1] + delta,dp[i - 1][j - 1] + alpha_dict[string2[i-1]][string1[j-1])
        
    i = n
    j = m

    while i > 0 and j > 0:
        diagonal = dp[j - 1][i - 1] + alpha_dict[string1[j - 1]][string2[i - 1]]
        up = dp[j-1][i] + delta
        left = dp[j][i - 1] + delta

        if dp[j][i] == diagonal:
            matchedString1 += string1[j - 1]
            matchedString2 += string2[i - 1]

            i -= 1
            j -= 1
        
        elif left < diagonal and left < up:
            matchedString1 += '_'
            matchedString2 += string2[i-1]

            i -= 1
            
        elif diagonal <= left and diagonal <= up:
            matchedString1 += '_'
            matchedString2 += '_'

            i -= 1
            j -= 1
        else:
            matchedString1 += string1[j -1]
            matchedString2 += '_'

            j -= 1

    while i > 0:
        matchedString1 += '_'
        matchedString2 += string2[i-1]
        i -= 1

    while j > 0:
        matchedString1 += string1[j - 1]
        matchedString2 += '_'

        j -= 1

    matchedString1 = matchedString1[::-1]
    matchedString2 = matchedString2[::-1]

    return [matchedString1, matchedString
    2, dp[m][n]]
    


