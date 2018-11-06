# This function read my file
def readFile():
    with open("my_file.txt", "r") as my_fake_db:
        # Read my file and split by row ("\n")
        info = my_fake_db.read().split("\n")
        # Headers: name of the columns
        headers = info[0].split("\t")
        # Data: data from my temperature probe
        data = [row.split("\t") for row in info[1:]]
    return (headers, data)

# From readed file to JSON
def plainFileToJSON(headers, data):
    resultJSON = []
    for row in data:
        tempDict = {}
        tempDict[headers[0]] = row[0]
        tempDict[headers[1]] = row[1]
        resultJSON.append(tempDict)
    return(resultJSON)

# It calls the functions "readFile" and "plainFileToJSON"
# to return a JSON file
def readTxtToJSON():
    headers, data = readFile()
    myJSON = plainFileToJSON(headers, data)
    return(myJSON)