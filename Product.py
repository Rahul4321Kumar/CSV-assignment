def output():
    import pandas as pd
    df = pd.read_csv("ProductDetailsedit.csv")
    number = 0.20
    percentage = "{:.0%}".format(number)
    df["ProductSalesTax"] = percentage
    
    df["ProductFinalPrice"] =df["ProductCostPrice"]*(number)+df["ProductCostPrice"]
    
    

    df.to_csv("ProductDetailsedit.csv", index=False)

output()

# import csv

# with open('ProductDetailedits.csv','r') as csvinput:
#     with open('newOutput.csv', 'w') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(csvinput)

#         all = []
#         row = next(reader)
#         print(row)
#         # print(row.append("new"))
#         row.append('ProductFinalPrice')
#         row.append('ProductFinalPrice')
#         # print(row)
#         all.append(row)
#         # print(all)

#         for row in reader:
#             row.append(row[0])
#             # print(row[0])
#             all.append(row)

#         writer.writerows(all)
#         print(all)