from ..window import Window

# pour ajouter une app :
# from .fichier import nom_de_l'app
# puis on l'ajoute à la liste des apps

app_list = []

from .test import App
app_list.append(App)

from .process import ProcessManagerWindow
app_list.append(ProcessManagerWindow)

from .menu import Menu
app_list.append(Menu)

# cette App doit être ajoutée en dernier obligatoirement
from .desktop import Desktop
app_list.append(Desktop)
