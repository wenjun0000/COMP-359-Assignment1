#Implement a program that orders keys based on user query frequency during execution. 
#That is, upate the order over the use of the program so that sequential search operates faster.
'''
Pseudocode:
Initialize a list named keys containing the keys.
Initialize a dictionary frequenc to store query counts for each key.
Increment(key):
	If key exists in keys:
    	Increment frequency[key]
    	Call Resorting()
 
Resorting():
	Sort keys in descending order of their frequency from frequency dictionary.
 
Main Program:
	While user provides input:
    	Read the Increment(key)
    	Call Resorting(key)
    	Output the updated keys list
 
Things left to do in this code:
1. Create and sort code into functions
2. Add Comments
3. Test Large Data
4. Find Time Complexity, look for optimization
'''
def Reorder(List, Dictionary):
    
    
#Needs to be worked upon 



Keys= ["Test1","Test2", "Test3"]
Frequency={Keys[0]:0, Keys[1]:0, Keys[2]:0}
while True:
    
    
    print("Current list:")
    print(Keys)
    print(Frequency)
    Inp=input("Enter your input")
    if Inp in Keys:
        CurrentVal=Frequency[Inp]
        Frequency[Inp]=CurrentVal+1
        Reorder(Keys,Frequency)
    else:
        Keys.append(Inp)
        Frequency[Keys[(len(Keys)-1)]]= 1

    





