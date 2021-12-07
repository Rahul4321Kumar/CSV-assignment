import csv


def file_validation(filename2):
    if not filename2.endswith(".csv"):
        raise FileNotFoundError("filename2 is not a valid csv file")
    else:
        print("Its a valid csv file")

def csv_datatype_validate(val):
    for i in val[1:]:
        if isinstance(i[0],str):
            print("all data are in correct format")
        else:
            print("data in productname are not in correct format")

        if isinstance(i[1],int):
            print("all data are in correct format")
        else:
            print("data in costprice are not in correct format")
            isinstance(int(i[1]),int)

        if isinstance(i[2],str):
            print("all data are in correct format")
        else:
            print("data in country are not in correct format")


def column_name_validate(val,header):
        print(val[0])
        if val[0]==header:
            print("All header matched")
        else:
            print("Issue in header do changes in input of HEADER_VALIDATE")
        
    
        
def read_csv(filename):
    with open(filename)as csv_file:
        reader = csv.reader(csv_file)
        lst=[]
        for read_data in reader:
            test_list = list(filter(None, read_data))
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
        all.append(row)
    writer.writerows(all)
    
def csv_output( filename,filename1,filename2):
    HEADER_VALIDATE=["Product_Name","Product-CostPrice","Country"]
    val=read_csv(filename)
    csv_datatype_validate(val)
    column_name_validate(val,HEADER_VALIDATE)
    write_csv(filename1, val)
    file_validation(filename2)
    

if __name__ == "__main__":
    csv_output("Input.csv","Output.csv","Example.csv")
        
