import csv 
#import sys
import spacy
def preprocess(requirements_filename, artifacts_filename):

    #loading the english language small model of spacy
    en = spacy.load('en_core_web_sm')
    stopwords = en.Defaults.stop_words
    en.Defaults.stop_words |= {"allow","user","apply"}

    #column that the info is in a csv, NEEDS to be not hardcoded eventually
    req_col = 0
    art_col = 1

    #headers that we want to ignore, NEEDS to be not hardcoded eventually
    num_headers_req = 1
    num_headers_art = 0

    #this is where we would run into issues w the csv with commas, but i dont think it makes sense to create a tsv parser bc it matters more how our final data is organized
    #like for this I can just change the code to just split by new lines for now
    list_req = list(line.split(",")[req_col] for line in open(requirements_filename, 'r'))[num_headers_req:]
    
    ##quick code change to accomodate a file that is only one column but has commas that are important
    #list_req = list(open(requirements_filename, 'r'))[num_headers_req:]
    list_art = list(line.split(",")[art_col] for line in open(artifacts_filename, 'r')if line.split(",")[0].isdigit())[num_headers_art:]

    cleaned_req=[]
    for requirement in list_req:
        tempList = []
        for token in requirement.split():
            if token.lower() not in stopwords:
                tempList.append(token)
        cleaned_req.append(tempList)

    cleaned_art=[]
    for artifact in list_art:
        tempList = []
        for token in artifact.split():
            if token.lower() not in stopwords:
                tempList.append(token)
        cleaned_art.append(tempList)

    return cleaned_req, cleaned_art
