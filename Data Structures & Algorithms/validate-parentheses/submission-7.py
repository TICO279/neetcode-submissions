class Solution:
    def isValid(self, s: str) -> bool:

        #if we only have 1 or less
        if len(s) < 2:
            return False
        
        
       #We store the corresponding pairs 
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'}

        stack = []
        
        for element in s:
            #if its an opening, we add it to the stack
            if element in pairs.values():
                stack.append(element)
            #if its a closing it has to be in our inputs and the corresponding
            #opening has to be on top of the stack as its the fisrt to go out
            elif element in pairs.keys() and stack and pairs[element] == stack[-1]:
                #we remove the opening from the stack
                stack.pop()
                
            else:
                #anything else its false
                return False



        return True if not stack else False