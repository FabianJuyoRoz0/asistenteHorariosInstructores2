from reportlab.pdfgen import canvas

fileName= 'Reporte.pdf'

pdf = canvas.Canvas(fileName)
pdf.setTitle('Reporte')
pdf.save()