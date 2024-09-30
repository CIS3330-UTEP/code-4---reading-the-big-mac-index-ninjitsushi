import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    YearPriceData = df[(df['year'] == year) & (df['iso_a3'] == country_code)] 
    #^^This line filters data from pandas df by year and price
   
    mean_price = YearPriceData['dollar_price'].mean()    
    #^^This line gets the average of the dollar prices in the df from the specific date chosen
   
    return round(mean_price, 2) if not pd.isna(mean_price) else None    
    #This line returns the avg of the price to 2 decimal places and also checks if the value is missing in the df
    


def get_big_mac_price_by_country(country_code):
    YearPriceData = df[(df['iso_a3'].str.lower() == country_code)]
    #^^The line above filters data in the df by the country code and assures that it looks for the letters are lowercase

    mean_price = YearPriceData['dollar_price'].mean()
    #^^The line above gets the average of all the dollar prices based on the country code

    return round(mean_price, 2) if not pd.isna(mean_price) else None    
    #This line returns the avg of the price to 2 decimal places and also checks if the value is missing in the df



def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass # Remove this line and code your user interface