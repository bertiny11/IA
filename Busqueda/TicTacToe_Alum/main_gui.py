import tkinter as tk
from tkinter import messagebox
from tictactoeAlum import *
from minimaxAlum import * 

class TicTacToeGUI:
    # Clase para manejar la Interfaz Gráfica del TicTacToe.
    #   Disclaimer: Esta clase ha sido creada con la ayuda de Gemini 3.0

    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("TicTacToe (IA Minimax)")
        
        self.juego = nodoInicial()
        
        self.visual = {1: "❌", -1: "⭕", 0.0: " "}
        # En caso de que no se visualicen correctamente los iconos, utilice el siguiente diccionario
        # self.visual = {1: "X", -1: "O", 0.0: " "}
        self.colores_jugador = {1: "red", -1: "blue", 0.0: "white"}
        self.botones = {}
        self.CrearGUI() 
        self.ventana.update_idletasks()
        self.ventana.update()

        if messagebox.askyesno("¿Quién comienza?", "¿Desea que la IA (X) empiece la partida?"):
            self.jugador_actual = 1
            self.EjecutarTurno()
        else:
            self.jugador_actual = -1
        
        self.ActualizarGUI_Msg()

    def CrearGUI(self):
        self.tableroV = tk.Frame(self.ventana)
        self.tableroV.pack(padx=20, pady=10)

        self.etiqueta_estado = tk.Label(self.ventana, text="", font=('Arial', 12))
        self.etiqueta_estado.pack(pady=5, padx=5)
        self.etiqueta_estado.config(font=('Arial', 14))

        for fila in range(3):
            for col in range(3):
                valor_celda = self.juego.tablero[fila, col]
                btn = tk.Button(self.tableroV, 
                                text=self.visual[valor_celda],
                                font=('Helvetica', 38), width=2, height=1, 
                                fg=self.colores_jugador[valor_celda],
                                command=lambda r=fila, c=col: self.GestionarMov(r, c))
                btn.grid(row=fila, column=col, padx=1, pady=1) 
                self.botones[(fila, col)] = btn

    def EjecutarTurno(self, jugada=None):
        # Ejecuta el turno del jugador actual (-1: MIN; 1 MAX).
        juego_terminado = False
        
        if self.jugador_actual == 1:
            self.ActualizarGUI_Msg("IA: Calculando movimiento...")
            self.ventana.update() 
            self.juego = PSEUDOminimax(self.juego) 
            
        elif self.jugador_actual == -1 and jugada:
            self.juego = aplicaJugada(self.juego, jugada, -1)
            
        self.ActualizarGUI_tablero()
        
        if terminal(self.juego):
            self.ComprobarTerminal()
            juego_terminado = True
        else:
            self.jugador_actual = opuesto(self.jugador_actual)
            self.ActualizarGUI_Msg()
            
        return juego_terminado

    def GestionarMov(self, fila, col):
        # Maneja el evento de click del usuario, valida y realiza el movimiento
        jugada_usuario = Jugada(fila, col)
        
        if self.jugador_actual == -1 and esValida(self.juego, jugada_usuario):
            juego_terminado = self.EjecutarTurno(jugada_usuario)
            if not juego_terminado:
                self.EjecutarTurno() 

        elif not esValida(self.juego, jugada_usuario):
            messagebox.showerror("Movimiento Inválido", "¡Esa casilla ya está ocupada!")

    def ActualizarGUI_tablero(self):
        for r in range(3):
            for c in range(3):
                valor = self.juego.tablero[r, c]
                self.botones[(r, c)].config(text=self.visual[valor], fg=self.colores_jugador[valor])

    def ActualizarGUI_Msg(self, mensaje=None):
        if mensaje:
            self.etiqueta_estado.config(text=mensaje)
        elif not terminal(self.juego):
            simbolo = self.visual[self.jugador_actual]
            self.etiqueta_estado.config(text=f"¡Tu turno! Juega con {simbolo}")

    def ComprobarTerminal(self):
        ganador = utilidad(self.juego)

        if ganador == 100:
            msg = "GANA MAX (IA)"
        elif ganador == -100:
            msg = "GANA MIN (JUGADOR)"
        elif ganador == 0:
            msg = "EMPATE"

        self.etiqueta_estado.config(text=msg, font=('Arial', 14, ))
        self.ventana.update_idletasks()
        self.ventana.update()

        if messagebox.askyesno("¿Quieres la revancha?", "¿Deseas echar otra partida?"):
            self.juego = nodoInicial()
        
            # Se resetean las casillas a su estado inicial
            for btn in self.botones.values():
                btn.config(state=tk.NORMAL)
                
            if messagebox.askyesno("¿Quién comienza?", "¿Desea que la IA (X) empiece la partida?"):
                self.jugador_actual = 1
                self.EjecutarTurno()
            else:
                self.jugador_actual = -1

            self.ActualizarGUI_tablero()
            self.ActualizarGUI_Msg()
        else:
            for btn in self.botones.values():
                btn.config(state=tk.DISABLED)
        
            self.ventana.after(1000, self.ventana.destroy) 
        
if __name__ == '__main__':
    interfaz = tk.Tk()
    juego_gui = TicTacToeGUI(interfaz)
    interfaz.mainloop()