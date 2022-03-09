#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]" 

with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()
    # print(starting_letter[0])
with open("Input/Names/invited_names.txt", "r") as file:
    invited_names = file.readlines()
    # print(invited_names[0])

    for name in invited_names:
        new_letter = starting_letter.replace(PLACEHOLDER, name.strip())

        with open(f"Output/ReadyToSend/Letter_for_{name.strip()}.txt", mode =  "w") as file:
            file.writelines(new_letter)
        



