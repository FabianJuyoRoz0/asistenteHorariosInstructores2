import xml.etree.ElementTree as ET

archivo_xml= ET.parse('C:/Users/FABIAN/Documents/GitHub/asistenteHorariosInstructores2/PE-04_1.xml')

raiz = archivo_xml.getroot()

print(raiz)

for i in raiz.findall('./Data'):
    print(i)
    print(i.text.encode('utf8'))