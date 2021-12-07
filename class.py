import function


class CsvOperation:
     def __init__(self,filename):
          self.filename = filename

     def csv_output(self,filename1,filename2):
          HEADER_VALIDATE=["Product_Name","Product-CostPrice","Country"]
          val=function.read_csv(self.filename)
          function.file_validation(filename2)
          function.column_name_validate(val,HEADER_VALIDATE)
          function.csv_datatype_validate(val)
          function.write_csv(filename1,val)
          

if __name__ == '__main__':
     result = CsvOperation("Input.csv")
     result.csv_output("Output.csv","Example.csv")






