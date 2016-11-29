import xlrd
import time


def Insertblanks(fValue,nTotalLen):
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
    Price = DataInSingleLine[2]
    Amount = DataInSingleLine[3]
    TotalCost = DataInSingleLine[4]
    Date = DataInSingleLine[5]

    #convert to XX.xx
    Price = '%0.2f' % Price
    TotalCost = '%0.2f' % TotalCost

    Final = Account + "|" +str(int(Code))+"|" + Insertblanks(Price,17) + "|"+  Insertblanks(int(Amount),12)+ "|" + Insertblanks(TotalCost,20)+ "|" + str(int(Date)) + "\r\n"
    return Final

def main(InputFileFull, OutputFileStart):

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
        value = MakeString(table.row_values(i)[:6])
        file_object.write(value)

    file_object.close( )

t1 = time.time()
main('input.xlsx', 'wxxghpsj')
t2 = time.time()

print "time cost is ", t2-t1
