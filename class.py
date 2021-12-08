"""We import function module which contain all function which
   perform all csv peration and its validation too.
"""
import function


class CsvOperation:
     """This is class based implementation of CsvOperation."""
     def __init__(self,input_file):
          self.input_file = input_file

     def csv_output(self,output_file):
          """This function handle all csv operations."""
          header_validate=["Product_Name","Product-CostPrice","Country"]
          csv_data=function.read_csv(self.input_file)
          function.file_validation(output_file)
          function.column_name_validate(csv_data,header_validate)
          function.csv_datatype_validate(csv_data)
          function.write_csv(output_file,csv_data)
          

if __name__ == '__main__':
     result = CsvOperation("Input.csv")
     result.csv_output("Output.csv")






