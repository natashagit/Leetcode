class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # input: gas and cost
        # output: starting index or -1 if can travel around circuit
        # check if total sum of gas<sum of cost then no travel can be done
        # update the total at each point for gas-cost
        # if total<0 then set total to 0 and result to new candidate i+1
        
        if sum(gas)<sum(cost):
            return -1
        total = 0
        result = 0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                result = i+1
        return result
