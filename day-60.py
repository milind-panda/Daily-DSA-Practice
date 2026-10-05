class Solution:
    def printList(self, head):
        result = []
        
        current = head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
      
