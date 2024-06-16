import pandas as pd
excel_path = "Product.xlsx"
df = pd.read_excel(excel_path) #don't forget to pip install openpyxl

product = eval(input("product : "))
amount = eval(input("amount : "))


def get_price(product):
    label_column_index = df.columns.get_loc('Name')
    price_column = df.columns[label_column_index + 1] #plus 1 to acess the price column
    price_value = df.loc[df['Name'] == product, price_column].values[0]
    return price_value
    
def get_stock(product):
    label_column_index = df.columns.get_loc('Name')
    amount_column = df.columns[label_column_index + 2] #plus 2 to acess the amount column
    amount_value = df.loc[df['Name'] == product, amount_column].values[0]
    return amount_value

def decrese_stock(product,amount):
    label_column_index = df.columns.get_loc('Name')
    amount_column = df.columns[label_column_index + 2]
    row_index = df.index[df['Name'] == product].tolist()[0]
    df.at[row_index, amount_column] -= amount

def cal(product, amount):
    try :
        price = get_price(product)
        stock = get_stock(product)
        if stock < amount:
            print(f"1 {product} for {price} bath")#โจทย์เป็นงี้ช่ะ ถ้าจำไม่ผิด
        else :
            print(f"{amount} {product} for {amount*price} bath")
            left = stock - amount
            decrese_stock(product,left)
            
    except :
            print("error fix it yourself i'm gonna go eat breakfast")

cal(product,amount) #ใส่ชื่อของกับจำนวนนะจ้ะ