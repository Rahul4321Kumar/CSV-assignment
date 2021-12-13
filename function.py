"""This module contains all csv inbuilt function to read anf write csv file"""
import csv


def file_validation(input_file):
    """This function is use to check file is valid or not"""
    try:
        if not input_file.endswith(".csv"):
            raise FileNotFoundError
    except FileNotFoundError:
        print("input_file is not a valid csv file")
    else:
        print("Its a valid csv file")


def csv_datatype_validate(csv_data):
    """This function is use to check datatype of csv_file_content"""

    for data in csv_data[1:]:
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


def column_name_validate(csv_data, header):
    """This function is used to check header of csv"""

    if csv_data[0] == header:
        print("All header matched")
    else:
        print("Issue in header do changes in input of HEADER_VALIDATE")


def read_csv(input_file):
    """This function is used to read csv file content
    and store in a variable(reading_csv_data)
    """
    with open(input_file) as csv_input:
        reader = csv.reader(csv_input)
        reading_csv_data = []
        for read_data in reader:
            test_list = list(filter(None, read_data))
            reading_csv_data.append(test_list)
    return reading_csv_data


def write_csv(output_file, csv_data):
    """This function is used to create new csv file with extra two column"""
    with open(output_file, 'w') as csv_output:
        writer = csv.writer(csv_output, lineterminator='\n')
        all = []
        row = csv_data[0]
        row.append('ProductSaleaTax')
        row.append('ProductFinalPrice')
        all.append(row)
        logic_to_fill_newcolumn(csv_data, writer, all)


def logic_to_fill_newcolumn(csv_data, writer, all):
    """This function is used to fill data in newly created columns"""
    for row in csv_data[1:]:
        row.append(20)
        result = int(row[1]) * 0.20
        price = int(row[1]) + result
        row.append(price)
        all.append(row)
    writer.writerows(all)


def csv_output(input_file, output_file):
    """This function is used to handle all csv file_validation
    and its operation
    """
    header_validate = ["Product_Name", "Product-CostPrice", "Country"]
    csv_data = read_csv(input_file)
    csv_datatype_validate(csv_data)
    column_name_validate(csv_data, header_validate)
    write_csv(output_file, csv_data)
    file_validation(input_file)


if __name__ == "__main__":
    csv_output("Input.csv", "Output.csv")
