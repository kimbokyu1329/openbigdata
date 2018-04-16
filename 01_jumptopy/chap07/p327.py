from xml.etree.ElementTree import Element,dump,SubElement

note = Element("note")
to = Element("to")
to.text="Tove"

note.append(to)
SubElement(note,"from").text= "1asdfsf"
dummy=Element("dummy")
note.insert(0,dummy)
note.remove(dummy)

note.attrib["date"]="20180412"
dump(note)
