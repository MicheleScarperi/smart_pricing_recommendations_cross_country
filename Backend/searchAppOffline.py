import pandas as pd
from tkinter import *

root = Tk()
root.title("Mediamarkt Smartphone Comparison Tool")
lbl = Label(root, text="Search for your phone here:")
lbl.grid(row=0, column=0)
sb = Entry()
sb.grid(row=1, column=0)


def clicked():

    text=sb.get()
    height = 5
    width = 5
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            b = Label(root, text=text)
            b.grid(row=i + 1, column=j + 1)


btn = Button(root, text="Search", command=clicked)
btn.grid(column=0, row=2)




mainloop()


# read merged product CSV
data = pd.read_csv("merged.csv", index_col=0)
# enter search query, make uppercase and separate by word - HAS TO BE REPLACED WITH THE PUSH REQUEST DATA
search_words = str.upper("Samsung Galaxy S10e 128gb").split()


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


# execute function and save results in search_results
search_results = search_query(data, "productname", search_words, 0)
