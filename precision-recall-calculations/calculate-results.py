import csv

## This python script calculates the precision and recall for 
##  GitRE traceability links.

#Data must appear in the .csv file in the follow form:
#   req,issue
#   1,34
#   2,35

def readDatabase(filename: str) -> list:
    list = []
    line_count = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                if not(row[0]=='req' and row[1]=='issue'):
                    print("Columns not set up properly in " + filename)
                    return [];            
                # for element in row:
                #     header.append(element)
                line_count += 1
            else:
                list.append((row[0],row[1]))
                line_count += 1
    return list

def calculatePrecisionAndRecall(oracle: list, testSet: list) -> None:
    found = []      #true positives
    missed = []     #false negatives
    for item in oracle:
        #Iterate over each element, do not edit the oracle.
        success = False         #whether the item is found.
        for test in testSet:
            if item == test:
                success = True
                break
        if success:
            found.append(item)
            testSet.remove(item)
        else:
            missed.append(item) 
    truePos = len(found)
    falseNeg = len(missed)
    falsePos = len(testSet)
    # print("True Positives:", truePos)
    # print("False Negatives:", falseNeg)
    # print("False Positives:", falsePos)
    precision = round(truePos * 100 / (truePos + falsePos)) #, 0)
    print("Precision:\t", precision)
    recall = round(truePos * 100 / (truePos + falseNeg)) #, 0)
    print("Recall:\t\t", recall)

def runAllTests() -> None:
    oracleFiles = ['keepass-oracle-set.csv', 'peering-oracle-set.csv', 'gammaj-oracle-set.csv']
    testFiles = [['keepass-m1.csv','keepass-m2.csv','keepass-m3.csv'],
                 ['peering-m1.csv','peering-m2.csv','peering-m3.csv'],
                 ['gammaj-m1.csv','gammaj-m2.csv','gammaj-m3.csv']]
    for i in range(len(oracleFiles)):
        oracle = readDatabase(oracleFiles[i])
        testFileList = testFiles[i]
        for testName in testFileList:
            testSet = readDatabase(testName)
            print("Oracle:", oracleFiles[i], "Test File:", testName)
            calculatePrecisionAndRecall(oracle, testSet)
                
if __name__ == "__main__":
    runAllTests()
