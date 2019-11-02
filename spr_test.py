import pandas as pd
import numpy as np
df1 = pd.read_csv("data_gen_v1.csv", sep="|", index_col=0)
#print(df1.head())

df2 = pd.read_csv("lookup.csv", sep=";", index_col=0)


#Ideal DF
master = pd.DataFrame(columns = ["gtin", "product_name", "product_desc", "availability", "current_price", "shipping_cost", "product_rating", "vendor_name", "ref_link", "product_img"])



# moving data to the master DF
master["current_price"] = df1["Price"]
master["availability"] = df1["In_Stock"]
master["ref_link"] = df1["ref_link"]
master["product_img"] = df1["Product_image"]
master["shipping_cost"] = df1["Shipping"]
master["product_desc"] =df1["Product_desc"]
master["vendor_name"] = df1["Location"]
master["product_rating"] = np.random.randint(1, 6, master.shape[0])
#master["Product_ID"] = df1["Product_ID"]

#masterMerged = pd.merge(master, df2)
#print(df1.head())
#print(df2.head())
#print(masterMerged.head())

theMerge = pd.merge(left=master, right=df2,how='left',left_on='Product_ID', right_on='Product_ID')
print(theMerge.head())


