from random import randrange

# data related to guitar notes - initally just 0 to 11th fret
string1 = ["E","F","F#","G","G#","A","A#","B","C","C#","D","D#"]
string2 = ["B","C","C#","D","D#","E","F","F#","G","G#","A","A#",]
string3 = ["G","G#","A","A#","B","C","C#","D","D#","E","F","F#",]
string4 = ["D","D#","E","F","F#","G","G#","A","A#","B","C","C#",]
string5 = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#",]
string6 = ["E","F","F#","G","G#","A","A#","B","C","C#","D","D#"]
notes = [string1,string2,string3,string4,string5,string6]			# 2D array

stringNumber = randrange(6)
fretNumber = randrange(12)

# let's make it easier - test without #-notes 
while (len(str(notes[stringNumber][fretNumber]))) == 2:
        stringNumber = randrange(6)
        fretNumber = randrange(12)

print("string: " + str(stringNumber+1)+ ", fret: " +  str(fretNumber))

# printing the strings - just to visualize the position
i = 0
while i < stringNumber:
	print ("|---------------|")
	i += 1
if i == stringNumber:
	if fretNumber< 10: print ("|------ " + str(fretNumber)+ " ------|")
	else: print ("|----- " + str(fretNumber)+ " ------|")			# it's just formatng
	i += 1
while i < 6:
	print ("|---------------|")
	i += 1
# expecting an answer form the user
answer = input()

# validating the answer
if str(answer).capitalize()  == str(notes[stringNumber][fretNumber]): print ("Correct!")
else: print ("Wrong! It's: " + str(notes[stringNumber][fretNumber]))
