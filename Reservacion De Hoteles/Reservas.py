import pandas as pd

archivo_excel = "casos_prueba.xlsx"
df = pd.read_excel(archivo_excel)


print("Casos de prueba encontrados:\n")
print(df)


reporte = df.to_string(index=False)
with open("reporte_casos_prueba.txt", "w") as archivo_reporte:
    archivo_reporte.write("Reporte de Casos de Prueba\n")
    archivo_reporte.write(reporte)

print("\nReporte generado exitosamente: reporte_casos_prueba.txt")
