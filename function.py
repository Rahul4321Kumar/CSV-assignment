import csv


def readcsv(filename1):
    with open(filename1, 'r') as csvinput:
        writecsv("output.csv",csvinput)


def writecsv(filename2,csvinput):
    with open(filename2, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        # print(reader[0])
        row.append('ProductSaleaTax')
        row.append('ProductFinalPrice')
        all.append(row)
        # print(all)

        for row in reader:
            row.append(20)
            res = int(row[1])*0.20
            price = int(row[1])+res
            row.append(price)

            all.append(row)

        writer.writerows(all)

if __name__ == "__main__":
    readcsv("Product1.csv")
        
