
import xlrd
import time
import sys

def HandleHyphen(string):
	lens = len(string)
	if string.find("-") != -1:
		string = string.replace("-", " ", 10) 
	return string

def Appendblanks(fValue,nTotalLen):
    # print fValue
    strValue = str(fValue)
    lenIn = len(strValue)
    nBlanks = nTotalLen - lenIn
    StrOut = ""

    for i in range(0, nBlanks):
        StrOut = StrOut + " "
    return strValue + StrOut


def Insertblanks(fValue,nTotalLen):
    #print fValue
    strValue = str(fValue)

    lenIn = len(strValue)
    nBlanks = nTotalLen - lenIn
    StrOut = ""

    for i in range(0,nBlanks):
        StrOut = StrOut + " "
    return StrOut + strValue


def MakeString(DataInSingleLine):
    Account = DataInSingleLine[0]
    Code = DataInSingleLine[1]
    Limit = DataInSingleLine[2]
    Class = DataInSingleLine[3]

    Price = DataInSingleLine[4]
    Amount = DataInSingleLine[5]
    TotalCost = DataInSingleLine[6]
    Refund = DataInSingleLine[7]
    Date = DataInSingleLine[8]
    BuyerID = str(DataInSingleLine[9])

    BuyerID = HandleHyphen(BuyerID)

    #convert to XX.xx
    Price = '%0.2f' % Price
    TotalCost = '%0.2f' % TotalCost
    Refund = '%0.2f' % Refund
    
    #make final string
    Final = Account + "|" + \
            str(int(Code))+"|" +\
            Insertblanks(int(Limit),4)+ "|" +\
            Class+"|" +\
            Insertblanks(Price,17) + "|"+\
            Insertblanks(int(Amount),12)+ "|" +\
            Insertblanks(TotalCost,20)+ "|" + \
            Insertblanks(Refund, 20) + "|" + \
            str(int(Date)) + "|" + \
            BuyerID.ljust(40) + \
            "\r\n"
    return Final

def main(InputFileFull, OutputFileStart):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    #get current time
    CurrentTime = str(time.strftime("%Y%m%d"))
    strOutput = OutputFileStart + CurrentTime + ".txt"
    #read file
    data = xlrd.open_workbook(InputFileFull)
    #check length
    NumberOfSheet = len(data.sheets())

    if NumberOfSheet != 1:
        print("shit!")
    else:
        print("OK!")


    #read data in first sheet
    table = data.sheets()[0]
    #read
    file_object = open(strOutput, 'w')
    StringList = []

    nrows = table.nrows
    for i in range(nrows):
        if i == 0:
            continue
        value = MakeString(table.row_values(i)[:10])
    	file_object.write(value)

    file_object.close( )

main('input.xlsx', 'wxxgpsjg')

