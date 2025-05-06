from spire.doc import *
from spire.doc.common import *

doc = Document()
section = doc.AddSection()
paragraph = section.AddParagraph()
paragraph.AppendText("Hello World!")
doc.SaveToFile("output.pdf", FileFormat.PDF)
doc.Close()