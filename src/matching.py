import sys
import csv

def matcher(list_req, list_art):
    table = [[0 for req in list_req] for artifact in list_art] #overlap of req and art
    wordIndex = {} # track words in requirements and artifacts

    ##### add all words in the requirements to the map
    for i in range(len(list_req)):
        for rWord in list_req[i]:
            #if the word isn't in the map yet, add it
            if wordIndex.get(rWord) == None:
                wordIndex[rWord] = {i}
            #else, add the req it occurs in to the existing set
            else:
                wordIndex[rWord].add(i)

    ##### go through all the artifacts
    for i in range(len(list_art)): 
        # for each word in the artifact
        for gWord in list_art[i]:
            if wordIndex.get(gWord) != None:
                #find which reqs it occurs in and +1 match to the table
                for reqInd in wordIndex.get(gWord):
                    table[i][reqInd] += 1
    
    buildSpreadsheet(table, list_req, list_art)
    formatting(table,list_req, list_art)


def buildSpreadsheet(table,list_req, list_art):
    f = open('../output/matchingsMatrix.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow([" "] + [" ".join(line) for line in list_req ])

    for i in range(len(table)):
        s =[" ".join(list_art[i])] + [str(number) for number in table[i]]
        writer.writerow(s)

    # close the file
    f.close()


#format:
#Issue,Requirement
def formatting(table,list_req, list_art):
    f = open('output/correctFormat.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)

    # write headings on to the csv file
    writer.writerow(["Issues"] + ["Requirements"])

    # write a row to the csv file for each issue/requirements combo with more than one word matching
    for i in range(len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] > 0:
                s = [str(i+1)] + [str(j + 1)]
                writer.writerow(s)
    f.close()



   
    
