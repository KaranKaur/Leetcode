class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        indegrees = [[] for _ in xrange(numCourses)]   # which courses this
        # course needs as a prereq
        outdegrees = [0] * numCourses  # How many courses each course is
        # prereq of

        for p in prerequisites:
            outdegrees[p[0]] += 1  # in the pair p, the first entry is the
            # prereq for the second entry
            indegrees[p[1]].append(p[0])
        queue = deque()
        for i in xrange(numCourses):
            if outdegrees[i] == 0:
                queue.append(i)
        k = 0  # keeps track of how many courses have been "taken" so far

        # All courses whose prereq conditions have been met are in the queue
        while queue:
            curr = queue.popleft()
            k += 1
            for j in indegrees[curr]:
                outdegrees[j] -= 1
                if outdegrees[j] == 0:
                    queue.append(j)
        return k == numCourses

# Python code
# https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-+-E)-time-and-O(V-+-E)-space



# Generally helpful code, but in C++
# https://leetcode.com/problems/course-schedule/discuss/58509/18-22-lines-C
# ++-BFSDFS-Solutions