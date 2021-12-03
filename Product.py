import csv
def output():
    import pandas as pd
    df = pd.read_csv("Product1.csv")
    number = 0.20
    percentage = "{:.0%}".format(number)
    df["ProductSalesTax"] = percentage
    
    df["ProductFinalPrice"] =df["ProductCostPrice"]*(number)+df["ProductCostPrice"]
    
    

    df.to_csv("Product1.csv", index=False)




def read():
    with open('Product1.csv','r') as csvinput: 
        reader = csv.reader(csvinput)
        for i in reader:
            print(i)


read()
output()

# Output:-
# PS C:\Users\rahul\OneDrive\Desktop\New folder (17)> python -u "c:\Users\rahul\OneDrive\Desktop\New folder (17)\Product.py"
# ['ProductName', 'ProductCostPrice', 'Country']
# ['Mobile', '30000', 'India']      
# ['Laptop', '40000', 'India']      
# ['Gold', '80000', 'Dubai']        
# ['Steel', '15000', 'England']     
# ['SportsBike', '200000', 'Europe']
# ['Watch', '5000', 'Japan']
# PS C:\Users\rahul\OneDrive\Desktop\New folder (17)> 