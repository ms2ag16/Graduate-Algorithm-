# Employee info
""" DFS loop over the Employee Lists and sum the value """
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        print emap
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)

if __name__=="__main__":
    apple=Employee(1,5,[2,3])
    pear=Employee(2,3,[])
    orange=Employee(3,2,[])
    Solved=Solution()
    employees=[apple,orange,pear]
    print Solved.getImportance(employees,1)
