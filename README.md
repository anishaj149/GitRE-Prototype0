# GitRE
Protype 0 for importing and parsing natural language requirements and creating traceability links between requirements and git issues and pull requests. 

## Code structure
1. src - matcher and parser 
2. data - git artifacts and requirement repository
3. output - matchings (matrices and lists)
4. precision-recall-calculations - calculating data for Table 2 in paper.

## Instructions for Run Matching
1. Select one of three pairs of issues/requirements (keepass, peering, gammaj) from the `data` folder
2. Run the driver file in the `src` folder through the terminal: `python3 driver.py <requirements-filename> <artifacts-filename>`
3. Examine the matches in the `matchesList.csv` and the match matrix in `matchingsMatrx.csv` both located in the `output` folder

