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
#Add timings for both optimal and non optimal searches
Things left to do in this code:
3. Test Large Data
4. Find Time Complexity, look for optimization
'''
def Reorder(List, Dictionary):
    # Sort the List in place based on the frequency from Dictionary
    List.sort(key=lambda x: Dictionary[x], reverse=True)

Keys = ["Test1", "Test2", "Test3"]
Frequency = {key: 0 for key in Keys}

while True:
    print("Current list:", Keys)
    print("Frequency:", Frequency)
    
    Inp = input("Enter your input: ")

    if Inp in Keys:
        # Increment frequency for existing key
        Frequency[Inp] += 1
    else:
        # Add new key and set its frequency to 1
        Keys.append(Inp)
        Frequency[Inp] = 1

    # Reorder the keys based on frequency
    Reorder(Keys, Frequency)




