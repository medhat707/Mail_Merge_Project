#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
# READING ALL NAMES AND SAVE THE IN A LIST
with open("input/letters/starting_letter.txt", "r") as first_file:
    letter_list = first_file.readlines()
    txt = letter_list[0]
    # x= txt.replace("[name]" , "ss")
    # print(x)

with open("input/names/invited_names.txt", "r") as second_file:
    invitation_list = second_file.readlines()

for name in invitation_list:
    x= txt.replace("[name]" , name.strip())
    with  open(f"letter_for_{name.strip()}", mode="w") as third_file:
        other_lines=[]
        for line in letter_list[1:]:
            other_lines.append(line)
        a= " ".join(other_lines)
        third_file.write(x+a)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp