# coding=UTF-8
'''
Created on 18/08/2013

@author: #edsonlead
'''
#pygtk.require('2.0')
import gtk
from random import choice
from About import About 


class GeraSenhas: 
    
    #Metodo Construtor da Classe
    def __init__(self):
        
        self.janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.janela.set_position(gtk.WIN_POS_CENTER)
        self.janela.set_title('Gerador de Senhas' )
        self.janela.set_size_request(340, 170)
        self.janela.set_resizable(True)
        self.fixed = gtk.Fixed()
        self.janela.add(self.fixed)
        
        self.fixed.put(gtk.Label('Comprimento:'), 20, 40)
        self.txtComprimento = gtk.Entry()
        self.txtComprimento.set_size_request(40, 30)
        self.fixed.put(self.txtComprimento, 150, 33)
        
        self.fixed.put(gtk.Label('Senha Gerada:'), 20, 77)
        self.txtSenha = gtk.Entry()
        self.txtSenha.set_size_request(140, 30)
        self.fixed.put(self.txtSenha, 150, 70)
         
        self.botaoGerar = gtk.Button('Gerar Senha')
        self.botaoGerar.set_size_request(110, 30)
        self.botaoGerar.connect('clicked', self.GerarSenha)
        self.fixed.put(self.botaoGerar, 210, 120)
        
        self.botaoAbout = gtk.Button('About')
        self.botaoAbout.set_size_request(105, 30)
        self.botaoAbout.connect('clicked', About)
        self.fixed.put(self.botaoAbout, 20, 120)
        
        self.janela.connect("destroy", gtk.main_quit)
 
        self.janela.show_all()
        
    def GerarSenha(self, widget):
        comprimento = self.txtComprimento.props.text
        try:
            comprimento = int(comprimento)
            if comprimento <= 3:
                    texto = '\n         Comprimento Inválido!\nSenha somente a partir de 4 digitos.'
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, texto)
                    msg.set_position(gtk.WIN_POS_CENTER)
                    msg.run()
                    msg.destroy()
        except:
            texto = '\nComprimento Inválido!'
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, texto)
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            

        else:
            digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            senha = ""
            for char in xrange(comprimento):
                if comprimento > 3:
                    senha += choice(digitos)
                self.txtSenha.props.text = senha
   