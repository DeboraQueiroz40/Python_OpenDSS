"""
Created on Tue Nov 24 14:54:59 2020

@author: César Tzanno
"""

import matplotlib.pyplot as plt
import win32com.client
from pylab import *
import py_dss_interface



class DSS():

    def __init__(self, end_modelo_DSS):

        # Criar a conexão entre Python e OpenDSS
        self.dssObj = win32com.client.Dispatch("OpenDSSEngine.DSS")
        self.end_modelo_DSS = end_modelo_DSS


        # Inciar o Objeto DSS
        if self.dssObj.start(0) == False:
            print ("Problemas em iniciar o OpenDSS")
        else:
            # Criar variáveis para as principais interfaces
            self.dssText = self.dssObj.Text
            self.dssCircuit = self.dssObj.ActiveCircuit
            self.dssSolution = self.dssCircuit.Solution
            self.dssCktElement = self.dssCircuit.ActiveCktElement
            self.dssBus = self.dssCircuit.ActiveBus



    def compile_DSS(self):

        # Limpar informações da última simulação
        self.dssObj.ClearAll()

        self.dssText.Comand = "compile " + self.end_modelo_DSS



    def versao_DSS(self):

        return self.dssObj.Version

    def solve_DSS_snapshot(self, multiplicador_carga):

        # Configurações
        self.dssText.Comand = "Set Mode=SnapShot"
        self.dssText.Comand = "Set ControlMode=Static"

        # Resolve o Fluxo de Potência
        self.dssSolution.Solve()

    def plot_tensao(self):
        Va = self.dssCircuit.AllNodeVmagPUByPhase(1)
        plt.plot(["A", "B", "C", "D"], Va)


 #if __name__ == "__main__":

# Criar um objeto da classe DSS
objeto = DSS(r"C:\Users\César Tzanno\Documents\POLI\4º ano\8º semestre\Laboratório de Sistemas de Potência\Atividades\4\redeTeste.dss")

# -*- coding: utf-8 -*-
print ("Versão do OpenDSS: " + objeto.versao_DSS() + "\n")

objeto.dssSolution.Solve()

dss = py_dss_interface.DSSDLL()
#dss.text("solve")
#dss.text("plot profile")