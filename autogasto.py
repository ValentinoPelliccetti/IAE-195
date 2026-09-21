import requests
import pandas as pd

resumen = []

for anio in range(2010, 2027):
    url_pres = f"https://gobiernoabierto.bahia.gob.ar/presupuesto/data/gestorDatos.php?anio={anio}&apertura=Presupuestado&a=1"
    url_gast = f"https://gobiernoabierto.bahia.gob.ar/presupuesto/data/gestorDatos.php?anio={anio}&apertura=Gastos&a=1"

    try:
        data_pres = requests.get(url_pres).json()
        data_gast = requests.get(url_gast).json()
    except ValueError:
        print(f"⚠️ El año {anio} no devolvió JSON válido")
        continue

    # Totales por año
    total_pres = sum(item["valor"] for item in data_pres)
    total_gast = sum(item["valor"] for item in data_gast)

    # Subtotales de Salud
    subtotal_pres_salud = sum(item["valor"] for item in data_pres if item["den"] == "Secretaría de Salud")
    subtotal_gast_salud = sum(item["valor"] for item in data_gast if item["den"] == "Secretaría de Salud")

    # Porcentajes
    porc_pres = (subtotal_pres_salud / total_pres) * 100 if total_pres > 0 else 0
    porc_gast = (subtotal_gast_salud / total_gast) * 100 if total_gast > 0 else 0

    resumen.append({
        "anio": anio,
        "total_presupuesto": total_pres,
        "total_salud_presupuestado": subtotal_pres_salud,
        "porcentaje_salud_presupuestado": porc_pres,
        "total_gastos": total_gast,
        "total_salud_gastos": subtotal_gast_salud,
        "porcentaje_salud_gastos": porc_gast
    })

# Guardar en Excel
df_resumen = pd.DataFrame(resumen)
df_resumen.to_excel("salud_pres_vs_gastos_2010_2026.xlsx", index=False)

print("Excel creado con comparación Presupuestado vs Gastos de Secretaría de Salud 2010-2026")
