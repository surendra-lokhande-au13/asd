class Solution(object):
    def nextGreaterElement(self, nums1, a):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        ans=[]
        for i in range(len(a)-1,-1,-1):
            if not stack: # for last elm 
                d[a[i]]=-1
            elif stack and stack[-1]>a[i]: 
                d[a[i]]=stack[-1]
            elif stack and stack[-1]<a[i]:
                while stack and stack[-1]<=a[i]:
                    stack.pop()
                if stack:
                    d[a[i]]=stack[-1] 
                elif not stack:
                    d[a[i]]=-1
            
            stack.append(a[i])
            
        for elm in nums1:
            ans.append(d[elm])
        return ans
