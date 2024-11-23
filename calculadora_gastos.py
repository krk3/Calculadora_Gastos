import tkinter as tk
from tkinter import messagebox

class CalculadoraGastosMensuales:
    def __init__(self, root):
        """Inicializa la ventana principal y configura la interfaz gráfica."""
        self.root = root
        self.root.title("Calculadora de Gastos Mensuales")
        
        # Lista para almacenar los gastos ingresados
        self.gastos = []

        # Título principal
        self.titulo = tk.Label(root, text="Calculadora de Gastos Mensuales", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiqueta y campo de entrada para los gastos
        self.label_gasto = tk.Label(root, text="Monto del Gasto:")
        self.label_gasto.grid(row=1, column=0, padx=10, pady=5)
        self.entrada_gasto = tk.Entry(root)
        self.entrada_gasto.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y menú desplegable para la categoría
        self.label_categoria = tk.Label(root, text="Categoría del Gasto:")
        self.label_categoria.grid(row=2, column=0, padx=10, pady=5)
        self.categorias = ["Alimentación", "Transporte", "Vivienda", "Entretenimiento", "Salud"]
        self.selected_categoria = tk.StringVar()
        self.selected_categoria.set(self.categorias[0])  # Categoría por defecto
        self.dropdown_categoria = tk.OptionMenu(root, self.selected_categoria, *self.categorias)
        self.dropdown_categoria.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar un gasto
        self.boton_agregar = tk.Button(root, text="Agregar Gasto", command=self.agregar_gasto)
        self.boton_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        # Sección para mostrar los gastos
        self.resumen_label = tk.Label(root, text="Resumen de Gastos:", font=("Arial", 14))
        self.resumen_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.lista_resumen = tk.Listbox(root, width=50, height=10)
        self.lista_resumen.grid(row=5, column=0, columnspan=2, pady=10)

        # Botón para ver el total de los gastos
        self.boton_resumen = tk.Button(root, text="Ver Total de Gastos", command=self.mostrar_resumen)
        self.boton_resumen.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_gasto(self):
        """Agrega un gasto a la lista y limpia el campo de entrada."""
        try:
            monto = float(self.entrada_gasto.get())  # Convierte la entrada a un número decimal
            categoria = self.selected_categoria.get()
            
            if monto <= 0:
                messagebox.showerror("Error", "El monto debe ser un valor positivo.")
                return

            # Añadir el gasto a la lista de gastos
            self.gastos.append({"monto": monto, "categoria": categoria})
            self.entrada_gasto.delete(0, tk.END)  # Limpiar el campo de entrada

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido para el monto.")

    def mostrar_resumen(self):
        """Muestra un resumen con todos los gastos y su total."""
        # Limpiar la lista de resumen antes de agregar los nuevos datos
        self.lista_resumen.delete(0, tk.END)

        total_gastos = 0
        # Recorrer los gastos y mostrar cada uno
        for gasto in self.gastos:
            self.lista_resumen.insert(tk.END, f"{gasto['categoria']}: {gasto['monto']} €")
            total_gastos += gasto['monto']
        
        # Mostrar el total de los gastos
        self.lista_resumen.insert(tk.END, f"Total de Gastos: {total_gastos} €")

def ejecutar_aplicacion():
    """Inicia la interfaz gráfica."""
    root = tk.Tk()
    app = CalculadoraGastosMensuales(root)
    root.mainloop()

if __name__ == "__main__":
    ejecutar_aplicacion()
