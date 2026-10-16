class Solution:
    def climbStairs(self, n: int) -> int:
        #Think Decision Trees
        #Either add 1 or add 2
        #Use Cache aka Memoization to skip the duplicate trees
        #Can have an array to stores values at positions i
        #To make space compl better we can only use 2 variables
        #Answer is fibonacci series in reverse
        one, two = 1, 1
        #n-1 because the first two values are always 1
        #after than till 0th index we traverse n-1 times only
        for i in range(n-1):
            #store one in temp var cause we update it
            temp = one
            #modify one by adding itself and two value
            #this gives no of steps needed from one 
            one += two
            #set value of initial one i.e., temp to two
            two = temp
        #no of distinct steps is the value of one
        return one
        '''
        # More efficient way
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
        '''
