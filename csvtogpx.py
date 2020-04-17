import lxml.etree
import lxml.builder

'''
https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python
'''
from pytz import timezone

output = open('test.xml', 'w', encoding='utf-8')

csvFile = 'Datum;Zeit;Zeitzone;Länge;Breite;Geschwindigkeit;Kurs;Adresse;Aufenthaltszeit;'
europe = timezone('Europe/Berlin')


with open("data.csv","r",encoding="iso-8859-14") as var_file:
    var_data = var_file.readlines()[4:]
    for index, enumerate in enumerate(var_data):
        file_data = var_data[index].strip().split(';')
        print(file_data[0],file_data[1],sep=" ")

E = lxml.builder.ElementMaker()
ROOT = E.root
DOCu = E.docu

FIELD1 = E.field1
FIELD2 = E.field2

the_doc = ROOT(
  DOCu(
    FIELD1('some value1', name='blah1'),
    FIELD2('some value2', name='blah2')
  )
)
print (lxml.etree.tostring(the_doc, pretty_print=True))