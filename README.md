# IAE-195
🇦🇷 [Español](#español) | 🇬🇧 [English](#english)

## Español

### Objetivo
Analiza qué porcentaje del presupuesto público y del gasto ejecutado se destina a la Secretaría de Salud en Bahía Blanca entre 2010 y 2026, comparándolo con el nivel nacional, con la recaudación de tasas municipales vinculadas a salud, y con el gasto en salud (% del PBI) de otros países.

### Fuente de datos
- Presupuesto y gasto ejecutado por secretaría (Bahía Blanca): Portal de Gobierno Abierto de la Municipalidad de Bahía Blanca (gobiernoabierto.bahia.gob.ar).
- Presupuesto y gasto en salud a nivel nacional: Presupuesto Abierto - Ministerio de Economía
- Recaudación de tasas municipales de salud
- Gasto en salud (% del PBI) por país: OCDE
  
### Contenido del repositorio
- `autogasto.py`: script en Python que consulta la API pública de datos abiertos de Bahía Blanca, obtiene presupuesto y gasto ejecutado por secretaría año a año (2010–2026), y calcula el monto y porcentaje correspondiente a la Secretaría de Salud.
- `Salud_y_gastos_2010-2026.xlsx`: resultado consolidado, con 4 hojas:
  - *Pre y gas Bahia Blanca*: presupuesto vs. gasto ejecutado en salud, a nivel municipal.
  - *Pre y gas Argentina*: mismo análisis a nivel nacional.
  - *Tasas de salud*: recaudación de tasas municipales vinculadas a salud.
  - *Paises %PBi y PBI pc*: gasto en salud (% del PBI) vs. PBI per cápita, comparación internacional.

### Cómo correr el script
```bash
pip install requests pandas openpyxl
python autogasto.py
```
Genera un Excel (`salud_pres_vs_gastos_2010_2026.xlsx`) con el resumen anual.


---

## English

### Goal
Analyzes what share of the public budget and executed spending goes to the Health Department in Bahía Blanca between 2010 and 2026, comparing it against the national level, municipal health-related tax revenue, and health spending (% of GDP) across countries.

### Data sources
- Budget and executed spending by department (Bahía Blanca): Bahía Blanca Municipality Open Data Portal (gobiernoabierto.bahia.gob.ar).
- National health budget and spending: Presupuesto Abierto - Ministerio de Economía
- Municipal health tax revenue: 
- Health spending (% of GDP) by country: OCDE

### Repository contents
- `autogasto.py`: Python script that queries Bahía Blanca's public open-data API, retrieves yearly budgeted and actual spending by department (2010–2026), and computes the Health Department's amount and percentage.
- `Salud_y_gastos_2010-2026.xlsx`: consolidated output, with 4 sheets (municipal budget vs. spending, national comparison, health-related municipal taxes, international % GDP vs. GDP per capita comparison).

### How to run
```bash
pip install requests pandas openpyxl
python autogasto.py
```
