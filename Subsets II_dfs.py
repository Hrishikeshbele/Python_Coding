'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Idea:

dfs(nums = [1,2,2], path = [], res = [])
|
|__ dfs(nums = [2,2] , path = [1], res = [[]])
|    |__ dfs(nums = [2] , path = [1,2], res = [[],[1]])
|    	  |__ dfs(nums = [] , path = [1,2,2], res = [[],[1], [1,2]])
|    	  	   # next: res = [[],[1],[1,2],[1,2,2]]
|    	  	   # for loop will not be executed
	 
|__ dfs(nums = [2] , path = [[2]], res = [[],[1],[1,2],[1,2,2]])
|    |__ dfs(nums = [] , path = [[2,2]], res = [[],[1],[1,2],[1,2,2],[2])
|    	  	   # next iteration: res =  [[],[1],[1,2],[1,2,2],[2],[2,2])
|    	  	   # for loop will not be executed
|
|for there two cases we skip the iteration to avoid generate duplicate subsets using continue .
| dfs(nums =[2, 2] , path =[1],res =  [[], [1], [1, 2], [1, 2, 2]])  
| dfs( nums =[1, 2, 2] , path =[] ,res = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]) 

'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.helper(nums,[],res)
        return res
    def helper(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.helper(nums[i+1:],path+[nums[i]],res)
        

