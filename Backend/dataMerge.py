import pandas as pd
import requests


def xrate(xfrom, xto):  # CURRENCY CONVERTER FUNCTION

    url = 'https://api.exchangerate-api.com/v4/latest/' + xfrom

    response = requests.get(url)
    data = response.json()
    return data["rates"][xto]


def price_fix(df):
    df["price"] = df["price"].str.replace(",9", ".9")
    df["price"] = df["price"].str.replace(",", "")
    df["price"] = df["price"].str.replace("-", "")
    df["price"] = df["price"].astype("float")


def price_fixpt(df):
    df["price"] = df["price"].str.replace("\n", "")
    df["price"] = df["price"].str.replace("€", "")
    df["price"] = df["price"].astype("float")


def price_fixes(df):
    df["price"] = df["price"].str.replace(",-", "")
    df["price"] = df["price"].str.replace(",", ".")
    df["price"] = df["price"].astype("float")


# Austria
Austria = pd.read_excel("mediamarkt_data/xlsx/mediaAT.xlsx")
Austria["productlink"] = "mediamarkt.at" + Austria["productlink"]
price_fix(Austria)
Austria["country"] = "Austria"
Austria["productname"] = Austria["productname"].str[1:]

# Belgium
Belgium = pd.read_excel("mediamarkt_data/xlsx/mediaBE.xlsx")
Belgium["productlink"] = "mediamarkt.be" + Belgium["productlink"]
price_fix(Belgium)
Belgium["country"] = "Belgium"
Belgium["productname"] = Belgium["productname"].str[1:]

# Switzerland
Switzerland = pd.read_excel("mediamarkt_data/xlsx/mediaCH.xlsx")
Switzerland["productlink"] = "mediamarkt.ch" + Switzerland["productlink"]
price_fix(Switzerland)
Switzerland["price"] = Switzerland["price"] * xrate("CHF", "EUR")
Switzerland["country"] = "Switzerland"
Switzerland["productname"] = Switzerland["productname"].str[1:]

# Spain
Spain = pd.read_excel("mediamarkt_data/xlsx/mediaES.xlsx")
Spain["productlink"] = "mediamarkt.es" + Spain["productlink"]
price_fixes(Spain)
Spain["productname"] = Spain["productname"].str.replace("Móvil - ", "")
Spain["country"] = "Spain"
Spain["productname"] = Spain["productname"].str[1:]

# Greece
Greece = pd.read_excel("mediamarkt_data/xlsx/mediaGR.xlsx")
Greece["productlink"] = "mediamarkt.gr" + Greece["productlink"]
price_fix(Greece)
Greece["country"] = "Greece"
Greece["productname"] = Greece["productname"].str[1:]

# Hungary
Hungary = pd.read_excel("mediamarkt_data/xlsx/mediaHU.xlsx")
Hungary["productlink"] = "mediamarkt.hu" + Hungary["productlink"]
Hungary["price"] = Hungary["price"].astype("float") * xrate("HUF", "EUR")
Hungary["country"] = "Hungary"
Hungary["productname"] = Hungary["productname"].str[1:]

# Italy
Italy = pd.read_excel("mediamarkt_data/xlsx/mediaIT.xlsx")
Italy["productlink"] = "mediaworld.it" + Italy["productlink"]
Italy["price"] = Italy["price"].str.replace(",", ".").astype("float")
Italy["country"] = "Italy"

# Netherlands is Broken

# Poland
Poland = pd.read_excel("mediamarkt_data/xlsx/mediaPL.xlsx")
Poland["productlink"] = "mediamarkt.pl" + Poland["productlink"]
Poland["price"] = Poland["price"].str.replace(" ", "")
price_fix(Poland)
Poland["price"] = Poland["price"] * xrate("PLN", "EUR")
Poland["country"] = "Poland"
Poland["productname"] = Poland["productname"].str[1:]

# Portugal
Portugal = pd.read_excel("mediamarkt_data/xlsx/mediaPT.xlsx")
Portugal["productlink"] = "mediamarkt.pt" + Portugal["productlink"]
price_fixpt(Portugal)
Portugal["country"] = "Portugal"

# Sweden
Sweden = pd.read_excel("mediamarkt_data/xlsx/mediaSE.xlsx")
Sweden["productlink"] = "mediamarkt.se" + Sweden["productlink"]
price_fix(Sweden)
Sweden["price"] = Sweden["price"] * xrate("SEK", "EUR")
Sweden["country"] = "Sweden"
Sweden["productname"] = Sweden["productname"].str[1:]

# Turkey
Turkey = pd.read_excel("mediamarkt_data/xlsx/mediaTR.xlsx")
Turkey["productlink"] = "mediamarkt.com.tr" + Turkey["productlink"]
price_fix(Turkey)
Turkey["price"] = Turkey["price"] * xrate("TRY", "EUR")
Turkey["country"] = "Turkey"
Turkey["productname"] = Turkey["productname"].str[1:]

merged = pd.concat([Austria, Belgium, Switzerland, Spain, Greece, Hungary,
                    Italy, Poland, Portugal, Sweden, Turkey], ignore_index=True)

merged = merged[pd.notnull(merged['productname'])]

merged["productname"] = merged["productname"].str.replace(" GB", "GB")
merged["productname"] = merged["productname"].str.replace("Dual SIM", "DualSIM")
merged["productname"] = merged["productname"].str.replace("Smartphone ", "")
merged["productname"] = merged["productname"].str.replace("Smartfon ", "")


merged.to_csv("merged.csv")
# merged.to_excel("merged.xlsx")
