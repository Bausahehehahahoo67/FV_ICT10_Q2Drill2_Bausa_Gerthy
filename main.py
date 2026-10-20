from pyscript import document, display

original_members = {"Gerthy Bruces Bausa", "Jericho Tuvieron Magsalin", "Joaquin Gabriel Mallari Castor", "Eran James Sangayab Diaz V", "Louie Vonn Medrana Lee", "Carlos Ezequiel Barja Borromeo", "Philip Joaquin Ponce"} #the original team

def checkers_membershippers (e):
    First = document.getElementById("first").value #gets user input on firstname field
    Last = document.getElementById("last").value #gets user input on lastname field
    Full_name =  Full_name = First + " " + Last #combines values of "First" and "Last" to create fullname
    members_list = Full_name.join(sorted(original_members)) #Combines "Full_name" and "original_members" to create the final list of members
    display(members_list, target = "result") #displays via "result" div id