class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
 
        def par ( open , close , path ) :
            if len( path ) == 2 * n :
                ans.append ( "".join(path[:]))
                return 
            if open != n :
                path.append ("(")
                par (open + 1 , close , path )
                path.pop ()

            if close != open  :
                path.append (")")
                par (open  , close+1 , path )
                path.pop ()
        ans =[]
        par (0,0 ,[])
        return ans 

            
            

        
























        
        
            