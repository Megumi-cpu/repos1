# ----------------------------- #
# 🧩 CLASE PADRE
# ----------------------------- #
class VariableEstadistica:
    def __init__(self, df, columna):
        self.df = df
        self.columna = columna
        # elimina valores nulos y los guarda como lista
        self.datos = df[columna].dropna().tolist()

    def cantidad(self):
        return len(self.datos)

    def mostrar_datos(self, n=10):
        print(self.datos[:n])


#ola
