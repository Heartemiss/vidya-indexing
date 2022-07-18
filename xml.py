from ast import parse
from platform import platform
from pydoc import pager
from lxml import etree

param = ["Developer", "Platform", "Publisher", "WikipediaURL", "Title", "Version", "Region", "ReleaseDate"]

def parseXML(xmlFile, name):
    
    with open(xmlFile) as fobj:
        xml = fobj.read()
        
    #root = etree.parse(xmlFile).getroot()
    root = etree.fromstring(xml)
    exception = "missing data"
    
    for elem in root.getchildren():
        for x in param:
            try:
                y = elem.find(x).text
            except:
                y = exception
            else:
                if y is None:
                    y = exception
                else:
                    y = y
            print(x + ": " + y)
        print()
    
    
if __name__ == "__main__":
        parseXML("xml\psx.xml", "psx")