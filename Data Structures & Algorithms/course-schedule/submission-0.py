class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #DFS with Cycle Detection
        
        #Create an adjancey list, this is a map, course i:[] to prereq list
        prereqMap = { i:[] for i in range(numCourses) }
        
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        #VisitSet to check cycle, store all courses along the CURRENT DFS PATH
        visitSet = set() #Lookup in Set is O(1)

        def dfs(course):
            #Check base cases
            #If Cycle is there return False
            if course in visitSet:
                return False
            #If there are no prereqs for the course then it means it can be completed, return True then
            if prereqMap[course] == []:
                return True
            #Add to visitSet the course and run dfs(course) on it's prerequisties
            visitSet.add(course)
            for prereq in prereqMap[course]:
                #If even 1 prereq can't be completed return False immediately for the main function
                if not dfs(prereq): 
                    return False
            #Remove course from visitSet since we no longer are visiting it
            visitSet.remove(course)
            #Since we know this course can be visited, we make the values as []
            #So 2nd base case can be returned immediately and we dont need to iterate again
            prereqMap[course] = []
            return True
        
        #Loop like this in case graph is not fully connected
        #eg, 1 -> 2 is one pair and another is 3 -> 4. For such cases
        #we need to loop through each pair
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
                
