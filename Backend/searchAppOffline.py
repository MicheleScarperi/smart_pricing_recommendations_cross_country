import pandas as pd
from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

data = pd.read_csv("merged.csv", index_col=0)

def search_query(df, column, search, search_leeway=0):
    """inputs: df: dataFrame, search: list of search words, leeway: disregards n items from the search words
    output: filtered dataFrame that contains search results"""

    df["search_eval_col"] = df[column].str.upper()  # uppercase column to be searched
    df["score"] = 0  # initialize score counter

    # for every search word, iterate through the entire df
    for word in search:
        for index in df.index:

            # if the search word is found at the given location, increment score for that row
            if word in df.at[index, "search_eval_col"]:
                df.at[index, "score"] = df.at[index, "score"] + 1

    # finds the rows with the score closest to the number of keywords (considering leeway)
    count = len(search)
    while count > -1:

        iterdf = df[(df["score"] > count)]  # iterates through the scores (decrementing the keyword number)
        if len(iterdf.index) == 0:  # if the result would be empty (no match for query)
            count = count-1         # decrements the number of keywords
        else:
            result = df[(df["score"] > count-search_leeway)]   # when result is found (with leeway),
            result.drop(columns=['search_eval_col', 'score'], inplace=True)  # drops extra columns and returns
            return result

    return "Error! Not found."  # if loop ends without result, returns error
#search_words = str.upper("Samsung Galaxy S10e 128gb").split()


root = Tk()
root.title("Mediamarkt Smartphone Comparison Tool")
lbl = Label(root, text="Search for your phone here:")
lbl.grid(row=0, column=0)



sb = Entry()
sb.grid(row=1, column=0)

frame = Frame()
frame.grid(row=1, column=1)

def clicked():

    for widget in frame.winfo_children():
        widget.destroy()

    proddname = Label(frame, text="Product Name", anchor="w", width=20)
    proddname.grid(row=0, column=0)
    link = Label(frame, text="Product Link", anchor="w", width=30)
    link.grid(row=0, column=1)
    price = Label(frame, text="Price (EUR)", anchor="w", width =10)
    price.grid(row=0, column=2)
    status = Label(frame, text="Availability", anchor="w")
    status.grid(row=0, column=3)
    country = Label(frame, text="Country", anchor="w")
    country.grid(row=0, column=4)



    search_words = str.upper(sb.get()).split()

    results = search_query(data, "productname", search_words, 0)

    height = len(results)

    for i in range(height):  # Rows
         b = Label(frame, text=results.iloc[i,0], anchor="w", justify=LEFT, width=20, wraplength=150)
         b.grid(row=i + 1, column=0)

         c = Label(frame, text=results.iloc[i,1], anchor="w", justify=LEFT, width=30, fg="blue", cursor="hand2")
         c.grid(row=i + 1, column=1)
         c.bind("<Button-1>", callback)

         d = Label(frame, text=str(int(results.iloc[i, 2])) + " EUR", anchor="e", justify=RIGHT, width=10)
         d.grid(row=i + 1, column=2)


btn = Button(root, text="Search", command=clicked)
btn.grid(column=0, row=2)




mainloop()



