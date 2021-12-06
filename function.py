import csv


def read_csv(filename):
    with open(filename)as csv_file:
        reader = csv.reader(csv_file)
        lst=[]
        for i in reader:
            test_list = list(filter(None, i))
            lst.append(test_list)
    return lst
    

def write_csv(filename1, val):
        with open(filename1, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            all = []
            row = val[0]
            row.append('ProductSaleaTax')
            row.append('ProductFinalPrice')
            all.append(row)
            logic_to_fill_newcolumn(val,writer,all)
    
def logic_to_fill_newcolumn(val,writer,all):
    
    for row in val[1:]:
        row.append(20)
        res = int(row[1])*0.20
        price = int(row[1])+res
        row.append(price)
        print(row)
        all.append(row)
    writer.writerows(all)
    
def csv_output( filename,filename1):
    val=read_csv(filename)
    write_csv(filename1, val)

if __name__ == "__main__":
    csv_output("Input.csv","Output.csv")
        
