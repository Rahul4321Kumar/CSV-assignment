"""We import function module which contain all function which
   perform all csv peration and its validation too.
"""
import csv


class CsvValidation:
    def __init__(self, input_file, csv_data, header):
        self.input_file = input_file
        self.csv_data = csv_data
        self.header = header

    def file_validation(self):
        """This function is use to check file is valid or not"""
        try:
            if not self.input_file.endswith(".csv"):
                raise FileNotFoundError
        except FileNotFoundError:
            print("input_file is not a valid csv file")
        else:
            print("Its a valid csv file")

    def csv_datatype_validate(self):
        """This function is use to check datatype of csv_file_content"""
        for data in self.csv_data[1:]:
            try:
                if isinstance(data[0], str) and isinstance(data[2], str):
                    print("Data are in correct format")
                    if isinstance(data[1], int):
                        print("Data are in correct format")
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                error_message = (
                    'Data are not in correct format typecast'
                    ' the data in appropriate datatype'
                    )
                print(error_message)

            else:
                if isinstance(data[0], str) and isinstance(data[2], str):
                    print("Data are in correct format")
                    if isinstance(int(data[1]), int):
                        print("Data are in correct format")
                    else:
                        raise ValueError
                else:
                    raise ValueError
        print("All data are in appropriate format")

    def column_name_validate(self):
        """This function is used to check header of csv"""
        if self.csv_data[0] == self.header:
            print("All header matched")
        else:
            print("Issue in header do changes in input of HEADER_VALIDATE")


class ReadCsvData:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_csv(self):
        """This function is used to read csv file content and store
        in a variable(reading_csv_data)
        """
        with open(self.input_file) as csv_input:
            reader = csv.reader(csv_input)
            reading_csv_data = []
            for read_data in reader:
                test_list = list(filter(None, read_data))
                reading_csv_data.append(test_list)

        return reading_csv_data


class WriteCsvData:
    def __init__(self, output_file, csv_data):
        self.output_file = output_file
        self.csv_data = csv_data

    def write_csv(self):
        """This function is used to create new csv
        file with extra two column
        """
        with open(self.output_file, 'w') as csv_output:
            writer = csv.writer(csv_output, lineterminator='\n')
            all = []
            row = self.csv_data[0]
            row.append('ProductSaleaTax')
            row.append('ProductFinalPrice')
            all.append(row)
            for row in self.csv_data[1:]:
                row.append(20)
                res = int(row[1]) * 0.20
                price = int(row[1]) + res
                row.append(price)
                all.append(row)
            writer.writerows(all)


if __name__ == '__main__':
    header_validate = ["Product_Name", "Product-CostPrice", "Country"]
    csv_read_object = ReadCsvData("Input.csv")
    csv_data = csv_read_object.read_csv()
    csv_validate_object = CsvValidation("Input.csv", csv_data, header_validate)
    csv_write_object = WriteCsvData("Output.csv", csv_data)
    csv_validate_object.file_validation()
    csv_validate_object.csv_datatype_validate()
    csv_validate_object.column_name_validate()
    csv_read_object.read_csv()
    csv_write_object.write_csv()
