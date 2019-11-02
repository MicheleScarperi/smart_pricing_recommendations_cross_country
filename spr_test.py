import pandas as pd
import numpy as np
df = pd.read_csv("data_gen_v1.csv", sep="|")
print(df.head())

df_tomerge = pd.read_csv("lookup.csv", sep=";")


#Ideal DF
master = pd.DataFrame(columns = ["gtin", "product_name", "product_desc", "availability", "current_price", "shipping_cost", "product_rating", "vendor_name", "ref_link", "product_img"])



# moving data to the master DF
master["current_price"] = df["Price"]
master["availability"] = df["In_Stock"]
master["ref_link"] = df["ref_link"]
master["product_img"] = df["Product_image"]
master["shipping_cost"] = df["Shipping"]
master["product_desc"] =df["Product_desc"]
master["vendor_name"] = df["Location"]
master["product_rating"] = np.random.randint(1, 6, master.shape[0])
master["Product_ID"] = df["Product_ID"]

#master2 = master.merge(df_tomerge,on="Product_ID")
master.info()
#df_tomerge.head(15)

