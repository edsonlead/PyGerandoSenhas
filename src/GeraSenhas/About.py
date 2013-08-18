'''
Created on 18/08/2013

@author: #edsonlead
'''
import pygtk
#pygtk.require('2.0')
import gtk

class About:
    def __init__(self,texto,janela=None):
        texto = "Gerador de Senhas\n\nAutor: Edson Silva\n#edsonlead\n\nedsonlead@blog.br"
        dialogo = gtk.MessageDialog(janela,gtk.DIALOG_MODAL,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,texto)
        dialogo.set_markup(texto)
        dialogo.run()
        dialogo.destroy()