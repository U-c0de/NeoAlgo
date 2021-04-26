'''
Given an array of N elements , find it's prefix sum array. In Competitive Programming, many times we need to calculate prefix sum array to solve our problem.
'''

# Prefix Sum code in Python 
R = 4
C = 5
  
# calculating new array 
def prefixSum2D(a) : 
    global C, R 
    psa = [[0 for x in range(C)]  
              for y in range(R)]  
    psa[0][0] = a[0][0] 
  
    # Filling first row  
    # and first column 
    for i in range(1, C) : 
        psa[0][i] = (psa[0][i - 1] + 
                       a[0][i]) 
    for i in range(0, R) : 
        psa[i][0] = (psa[i - 1][0] + 
                       a[i][0]) 
  
    # updating the values in  
    # the cells as per the  
    # general formula 
    for i in range(1, R) : 
        for j in range(1, C) : 
  
            # values in the cells of  
            # new array are updated 
            psa[i][j] = (psa[i - 1][j] + 
                         psa[i][j - 1] - 
                         psa[i - 1][j - 1] + 
                           a[i][j]) 
  
    # displaying the values 
    # of the new array 
    for i in range(0, R) : 
        for j in range(0, C) : 
            print (psa[i][j],  
                   end = " ") 
        print () 
  
# Driver Code 
a = [[ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ]] 
  
prefixSum2D(a)

'''
Test Case 1: Input a = [[ 1, 1, 1, 1, 1 ], 
                        [ 1, 1, 1, 1, 1 ], 
                        [ 1, 1, 1, 1, 1 ], 
                        [ 1, 1, 1, 1, 1 ]] 

            Output: 1 2 3 4 5 
                    2 4 6 8 10 
                    3 6 9 12 15 
                    4 8 12 16 20

Time Complexity: O(R*C)
Space Complexity: O(R*C)
'''