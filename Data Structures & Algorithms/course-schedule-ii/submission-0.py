class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #This is TOPOLOGICAL SORTING
        #Adjaceny List and DFS with Cycle Detection
        #Create the adjaceny list
        prereqMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        #Create a visited set to see if course is in current dfs path
        #a cycle set to check for cycles
        visited, cycle = set(), set()
        res = []
        def dfs(course):
            #If cycle present return False, we visited course twice
            #return [] in end
            if course in cycle: return False
            #If course has been visited then we can skip it since we 
            #dont need to visit it twice and dont need
            #to stop our alogirthm
            if course in visited: return True

            #Check Cycles here
            cycle.add(course)
            for pre in prereqMap[course]:
                if dfs(pre) == False : return False
            cycle.remove(course)
            #If no cycles found then add the course to visited set
            #and also to result res
            visited.add(course)
            res.append(course)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False : return []
        
        return res

