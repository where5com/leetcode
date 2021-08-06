"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None: return []
        current=[root]
        result=[]
        while len(current):
            temp=[]
            childrens=[]
            for node in current:               
                childrens.extend(node.children)
                temp.append(node.val)
            result.append(temp)
            current=childrens
        return result