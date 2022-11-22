from parser import parsexml
from preprocessing import preprocess
from matching import matcher
import sys

inputs_path = "../data/"

requirements_filename = sys.argv[1] #this is the cleaned file for requirements
if (requirements_filename.split(".")[1] == "xml"):
    requirements_filename = parsexml(requirements_filename) #parses xml into csv and returns a .csv file name to operate on
artifacts_filename = sys.argv[2] 
list_req, list_art = preprocess(inputs_path + requirements_filename, inputs_path + artifacts_filename)
matcher(list_req, list_art)