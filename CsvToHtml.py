import os
import pandas as pd
import webbrowser as wb
import random as rand


def ReadCsvFile(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        allData = []
        for dataField in df:
            data = []
            data.append(str(dataField))
            for eachData in df[str(dataField)].tolist():
                data.append(eachData)
            allData.append(data)
        return allData
    else:
        print("No such file!!")
        return None


def createHtmlTableRow(data):
    htmlSring = "<tr>"
    for i in data:
        htmlSring += "<td>"+str(i)+"</td>"
    htmlSring += "</tr>"
    return htmlSring


def convertToHtmlTable(table):
    htmlString = '<table height = "500" width = "500" border ="1" align = "center">'
    for tableRow in table:
        htmlString += createHtmlTableRow(tableRow)
    htmlString += "</table>"
    return htmlString


def convertToTable(csvList):
    length = len(csvList[0])
    csv_length = len(csvList)
    table = []
    for item in range(0, length):
        row = []
        for csv_item in range(0, csv_length):
            row.append(csvList[csv_item][item])
        table.append(row)
    return table


def createHtmlCode(htmlTableData):
    bgColor = input("Preferred background color : ")
    bgColor = 'bgcolor = "'+bgColor+'"' if not bgColor ==  "" else bgColor 
    htmlString = "<html>"
    htmlString += "<head>"
    htmlString += "<title>"
    htmlString += "table"
    htmlString += "</title>"
    htmlString += "</head>"
    htmlString += "<body "+bgColor+">"
    htmlString += htmlTableData
    htmlString += "</body>"
    htmlString += "</html>"
    return htmlString


def generateHtml(htmlString):
    try:
        print("\nTo overwrite enter file path without extension")        
        fileName = input("Html file name : ")
        fileName = fileName if not fileName ==  "" else "html"+str(rand.randint(0,10))
        f = open(fileName+'.html', 'w')
        f.write(htmlString)
        f.close()
        wb.open_new_tab(fileName+'.html')     
    except Exception as ex:
        print(ex)


def run():
    path = input("\nCsv file path : ")
    path.replace("\\", "/")
    csv = ReadCsvFile(path)
    if not csv == None:
        table = convertToTable(csv)
        htmlTableData = convertToHtmlTable(table)
        html = createHtmlCode(htmlTableData)
        generateHtml(html)
    print("Exiting....")

print("\nCSV to HTML Converter v-1.11...")
run()
