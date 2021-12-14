# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:02:53 2021

@author: Fernando Gioppato
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class Variaveis:
    
    def __init__(self, coluna):
        
        self._coluna = coluna
        pass
        

    def n(self, dados):
        """ Retorna o tamanho da amostra. """
        
        n = dados.shape[0]
            
        return n
    
    
    def renda(self, dados):
        """ Retorna uma série com a renda dos indivíduos do grupo. """
        
        renda = dados[self._coluna].sort_values()
        
        return renda
    
    
    def renda_total(self, dados):
        """ Retorna a renda total do grupo. """
        
        renda_total = np.sum(dados[self._coluna])
        
        return renda_total


    def renda_acumulada(self, dados):
        """ Retorna uma série com a proporção da renda acumulada dos indivíduos. """
    
        renda_acum = np.cumsum(self.renda(dados)) / self.renda_total(dados)
        
        return renda_acum
    
        
class Gini(Variaveis):
    
    
    def _props(self, grupos, dados):
        
        """ Calcula as proporçõe de população e renda dos grupos para a decomposição. """
        
        self._medias = [np.mean(grupo[self._coluna]) for grupo in grupos]
        
        pop = [self.n(dados = grupo) / self.n(dados = dados) for grupo in grupos]
        renda = [self.renda_total(dados = grupo) / self.renda_total(dados = dados) for grupo in grupos]
        
        x =  np.array([ [x for _,x in sorted(zip(self._medias, pop))],
                        [y for _,y in sorted(zip(self._medias, renda))] ])
        
        return x
    
        
    def gini(self, dados):
        
        """ Calcula o Índice de Gini do conjunto de dados. """
    
        
        gini = 1 - ((1 / self.n(dados)) * np.sum(self.renda_acumulada(dados) + self.renda_acumulada(dados).shift()))
        
        return round(gini, 5)


    def decomp(self, grupos, dados):
        
        """ Decompõe o índice de gini entre os conjuntos passados. """
        
        prop = self._props(grupos, dados)
        
        vetores = np.array([ prop[0] ,
                             prop[1] ,
                             np.cumsum(prop[1]) ,
                             np.cumsum(np.cumsum(prop[1]))  
                          ])
                       
        ghs = np.array( [ self.gini( dados = grupo ) for grupo in grupos ] )
        
        gh = [x for _,x in sorted(zip(self._medias, ghs))]
                       
        ge = 1 - np.sum( vetores[3] * vetores[0] )
                                     
        gk = np.sum(vetores[0] * vetores[1] * gh)
                       
        gs = self.gini(dados = dados) - ge - gk
                                      
        return (gh, round(ge, 5), round(gk, 5), round(gs, 5))
        
        
    
    def lorenz(self, dados):
        
        """ Plota a Curva de Lorenz do conjunto passado como argumento. """
        
        n = self.n(dados = dados)
        eixo_x = np.arange(1, n+1)/n
        y = self.renda_acumulada(dados = dados)
        idx = self.gini(dados = dados)
    
        fig, ax = plt.subplots()
        
        
        ax.plot(eixo_x, y, color = 'blue')
        ax.plot(np.arange(0, n+1)/n,
                np.arange(0, n+1)/n, 
                linestyle = '--',
                color = 'black',
                linewidth = 1)
        ax.fill_between(eixo_x, y1 = eixo_x, y2 = y, alpha = .3)
        ax.margins(0)
        ax.set_title('Curva de Lorenz', fontsize = 16, loc = 'left')
        ax.set_xlabel(r'$\pi_i$', loc = 'right', fontsize = 15)
        ax.set_ylabel(r'$\phi_i$', loc = 'top', rotation = 0, fontsize = 15)
            
        texto = f'Índice de Gini: {round(idx, 4)}'
        ax.annotate(text = texto, xy = (.07, .8), fontsize = 12)
        
        plt.show()