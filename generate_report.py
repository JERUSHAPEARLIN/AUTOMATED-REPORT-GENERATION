import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


df = pd.read_csv('sales_data.csv')
summary = df.groupby("Region")["Sales"].sum().reset_index()


plt.figure(figsize=(6, 4))
plt.bar(summary['Region'], summary['Sales'], color='skyblue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()


pdf = FPDF()
pdf.add_page()


pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Automated Sales Report", ln=True)


pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 10, "Region", 1)
pdf.cell(50, 10, "Total Sales", 1)
pdf.ln()


pdf.set_font("Arial", '', 12)
for i in range(len(summary)):
    pdf.cell(50, 10, summary['Region'][i], 1)
    pdf.cell(50, 10, str(summary['Sales'][i]), 1)
    pdf.ln()

pdf.ln(10)
pdf.image("sales_chart.png", x=10, w=180)

pdf.output("sales_report.pdf")
print("✅ Report generated: sales_report.pdf")
