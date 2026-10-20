from pyscript import document
from difflib import get_close_matches 
#a fuzzy-matching function hehehheh 
# so if " Zyreen Naguitt" it ccan suggest the acc one in the list that is similar to it



members = ["Zyren Naguit", "Brixen Rabacca", "Sean Young", "Kiel Sunga", "Andrei Viray"]

def check_nm(event):
    fname = document.getElementById("fname").value.strip().lower()
    lname = document.getElementById("lname").value.strip().lower()
    name = combine(fname, lname)
    msg = document.getElementById("msg")

    if not fname or not lname: #check if the input r present
        msg.innerText = "Please input both fields"
        return

    nm_members = [] 
    for member in members: # looks at each name in the list ; casefold() lower cases everything for case insensitive comparison
        nm_members.append(member.casefold()) # after converting it ; it adds it to the new list (nm_member)

    if name.casefold() in nm_members: # checks if in the new list
        msg.innerText = f"Congratulations {name}! You are now part of the ICT club."
        return

    similar = get_close_matches(name.casefold(), nm_members, n=1, cutoff= 0.65) 
    #format - 1stArgu: user input ; 2ndArgu: list that the input will be compare to ; n=1 return atleast 1 sugestion; 
    #cutoff=0.65 : only return if it is 65% similar

    if similar: #the possible name
        for member in members:
            if member.casefold() == similar[0]: #0 is first in index counting so first possible match
                msg.innerText = f"Did you mean {member}?"
                return
    msg.innerText = f"Sorry {name}, your name is not on the list." # if the similar is empty; false
        
def combine(name1, name2): #combine first and last name
    initial_name = [name1, name2]
    final_name = " ".join(initial_name)
    return final_name.title()




    

    



    
