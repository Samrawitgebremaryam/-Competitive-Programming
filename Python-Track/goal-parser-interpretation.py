class Solution:
    def interpret(self, command: str) -> str:
        result=''
        for i in range (len(command)):
            if command[i]=='(' and command[i+1]==')':
                result+='o'
            elif command[i]=='(' and command[i+1]=='a':
                result+='al'
            elif command[i]=='G':
                result+='G'
        return result



        