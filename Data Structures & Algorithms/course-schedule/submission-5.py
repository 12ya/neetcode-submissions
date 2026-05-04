class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def findPath(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for prereq in preMap[course]:
                if not findPath(prereq):
                    return False
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if not findPath(course):
                return False
        
        return True