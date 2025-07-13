#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as nfiles:
    names = nfiles.read()
with open("Input/Letters/starting_letter.txt") as lfiles:
    letter_template = lfiles.read()
    names_list = names.splitlines()
for name in names_list:
    name = name.strip()
    personalized_letter = letter_template.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as output_file:
        output_file.write(personalized_letter)
print("Letters created successfully in the 'ReadyToSend' folder.")