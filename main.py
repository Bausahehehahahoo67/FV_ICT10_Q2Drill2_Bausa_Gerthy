from pyscript import document, display

original_members = {"Gerthy Bruces Bausa", "Jericho Tuvieron Magsalin", "Joaquin Gabriel Mallari Castor", "Eran James Sangayab Diaz V", "Louie Vonn Medrana Lee", "Carlos Ezequiel Barja Borromeo", "Philip Joaquin Ponce"}

def checkers_membershippers (e):
    First = document.getElementById("first").value
    Last = document.getElementById("last").value
    Full_name = First + Last
    members_list = Full_name.join(sorted(original_members))
    display(members_list, target = "result")