from pyscript import document, display

original_members = {"Gerthy Bruces Bausa", "Jericho Tuvieron Magsalin", "Joaquin Gabriel Mallari Castor", "Eran James Sangayab Diaz V", "Louie Vonn Medrana Lee", "Carlos Ezequiel Barja Borromeo", "Philip Joaquin Ponce"} #the original team

def checkers_membershippers (e):
    First = document.getElementById("first").value #gets user input on firstname field
    Last = document.getElementById("last").value #gets user input on lastname field
    Full_name =  Full_name = First + " " + Last #combines values of "First" and "Last" to create fullname. a space is used to create a proper space between the two names
    original_members.add(Full_name) #combines the original set of members + user's name, also if i used "+" it wont work because two different types
    members_list = f"{'<br>'.join(sorted(original_members))}" #f string, sorts names by alphabetical order
    document.getElementById("result").innerHTML = members_list #displays via "result" div id. if i used display it would just bunch up like a paragraph, but now it displays like a proper vertical list