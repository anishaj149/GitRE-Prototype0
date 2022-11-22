import xml.etree.ElementTree as ET
import csv

def parsexml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    path = "../misc/"
    # CREATE CSV FILE
    csvfile = open(path + xml_file.split(".")[0] + ".csv",'w',encoding='utf-8')
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

    return path + xml_file.split(".")[0] + ".csv"
