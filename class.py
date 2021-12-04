import function


class CsvOperation:
     def __init__(self,filename):
          self.filename = filename

     def csv_output(self,filename1):
         function.read_csv(self.filename)
         function.write_csv(self.filename, filename1)

if __name__ == '__main__':
     result = CsvOperation("Product1.csv")
     result.csv_output("Output.csv")






