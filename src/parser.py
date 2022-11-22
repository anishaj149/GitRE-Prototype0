import xml.etree.ElementTree as ET
import csv
import os
import os.path

def parsexml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    file = "../misc/reqs.csv"

    #delete reqs file if it already exists
    if os.path.isfile(file):
        os.remove(file)
    # CREATE CSV FILE
    csvfile = open(file,'w', encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)

    # ADD THE HEADER TO CSV FILE
    csvfile_writer.writerow(["requirements"])
    parsed_reqs = []
    for req in root.findall('.//{req_document.xsd}req/{req_document.xsd}text_body'):
        req_txt = req.text
        if(req_txt):
            req_txt = req_txt.replace("\n", "")
            parsed_reqs.append(req_txt)
            csv_line = [req_txt]
            # ADD A NEW ROW TO CSV FILE
            csvfile_writer.writerow(csv_line)
    csvfile.close() 
    
    return file

