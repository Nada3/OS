from ..window import Window

# pour ajouter une app :
# from .fichier import nom_de_l'app
# puis on l'ajoute à la liste des apps

app_list = []

from .editeur import EditeurTexte
app_list.append(EditeurTexte)

from .keys_repeat import KeysRepeatWindow
app_list.append(KeysRepeatWindow)

from .process import ProcessManagerWindow
app_list.append(ProcessManagerWindow)

# cette App doit être ajoutée en dernier obligatoirement
from .desktop import Desktop
app_list.append(Desktop)
