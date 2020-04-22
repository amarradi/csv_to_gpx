
from xml.etree import ElementTree as ET


csvFile = 'Datum;Zeit;Zeitzone;Länge;Breite;Geschwindigkeit;Kurs;Adresse;Aufenthaltszeit;'
"""
Dateiformate
Datum: dd.mm.yyyy
Zeit: hh:mm:ss
Länge: dezimal
Breite: dezimal
Geschwindigkeit: integer
Kurs: integer
Adresse: nicht relevant
Aufenthaltszeit: nicht relevant
"""

with open('/home/marcus/dev/data.csv', 'r', encoding='iso-8859-14') as f:
    first_line = f.readline().strip()
with open('/home/marcus/dev/data.csv', 'r', encoding='iso-8859-14') as var_file:
    var_data = var_file.readlines()[4:]
    root = ET.Element("gpx")

    root.set("version", "version 1.1")
    trk = ET.SubElement(root, "trk")
    name = ET.SubElement(trk, "name")
    name.text = str(first_line)
    number = ET.SubElement(trk, "number")
    trkseg = ET.SubElement(trk, "trkseg")


    for index, enumerate in enumerate(var_data):
        file_data = var_data[index].strip().split(';')
        #Testausgabe
        print(index, file_data[0], file_data[1], file_data[2], file_data[3], file_data[4], file_data[5], sep=" ")
        trkpt = ET.SubElement(trkseg, "trkpt")
        trkpt.set("lon", str(file_data[3]))
        trkpt.set("lat", str(file_data[4]))
        time = ET.SubElement(trkpt, "time")
        tmp = str(file_data[0]).split(".")
        time.text = tmp[2]+"-"+tmp[1]+"-"+tmp[0]+"T"+str(file_data[1])+"Z"
        ele = ET.SubElement(trkpt, "ele")
        ele.text = str(file_data[5])

tree = ET.ElementTree(root)
tree.write("test.xml")

