import function


class CsvOperation:
     def __init__(self,filename):
          self.filename = filename

     def csv_output(self,filename1):
         val=function.read_csv(self.filename)
         function.write_csv(filename1,val)

if __name__ == '__main__':
     result = CsvOperation("Input.csv")
     result.csv_output("Output.csv")






