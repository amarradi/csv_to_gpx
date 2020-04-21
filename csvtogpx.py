
from xml.etree import ElementTree as ET

output = open('test.xml', 'w')

csvFile = 'Datum;Zeit;Zeitzone;Länge;Breite;Geschwindigkeit;Kurs;Adresse;Aufenthaltszeit;'

with open("/home/marcus/dev/data,csv","r",encoding="iso-8859-14") as var_file:
    var_data = var_file.readlines()[4:]
    for index, enumerate in enumerate(var_data):
        file_data = var_data[index].strip().split(';')

        print(index, file_data[0], file_data[1], sep=" ")


root = ET.Element("gpx")
root.set("version", "version 1.1")
trk = ET.SubElement(root, "trk")
name = ET.SubElement(trk, "name")
number = ET.SubElement(trk, "number")
trkseg = ET.SubElement(trk, "trkseg")
trkpt = ET.SubElement(trkseg, "trkpt")
ele = ET.SubElement(trkpt, "ele")
time = ET.SubElement(trkpt, "time")
tree = ET.ElementTree(root)
tree.write("test.xml")

