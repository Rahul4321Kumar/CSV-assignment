import csv


def read_csv(filename):
    try:
        with open(filename)as csv_file:
            print(csv_file.read())
    except:
        print(f'No file name like {filename} check it again')
    

def write_csv(filename,filename1):
    with open(filename, 'r') as csvinput:
        with open(filename1, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all=[]
            print(reader)
            row = next(reader)
            row.append('ProductSaleaTax')
            row.append('ProductFinalPrice')
            all.append(row)
            logic_to_fill_newcolumn(reader,writer,all)
    
def logic_to_fill_newcolumn(reader,writer,all):

    for row in reader:
        row.append(20)
        res = int(row[1])*0.20
        price = int(row[1])+res
        row.append(price)
        all.append(row)
    writer.writerows(all)
    
def csv_output( filename,filename1):
    read_csv(filename)
    write_csv(filename, filename1)

if __name__ == "__main__":
    csv_output("Input.csv","Output.csv")
        
