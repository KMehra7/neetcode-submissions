class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqMap = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        print(prereqMap)

        visiting = set()

        def dfs(course):
            if course in visiting: return False
            if prereqMap[course] == []: return True

            visiting.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq): return False
            visiting.remove(course)
            prereqMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True