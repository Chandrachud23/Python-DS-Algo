#Recursive Function to replace all occurrences of pi in a given with 3.14
def replacePieHelper(string, start):
    
    if len(string) < 2 or start == len(string):
        return string

    replacePieHelper(string, start + 1)

    if(string[start] == 'p' and string[start + 1] == 'i'):
        string[start:start + 2] = ['3', '.', '1', '4']
        
# Function to replace pi with 3.14        
def replacePi(string):
    replacePieHelper(string, 0)
 
# Driver Code
if __name__ == "__main__":
    string = "pippppiiiipi"
    string = list(string)

    replacePi(string)
 
    string = ''.join(string)
    print(string)
