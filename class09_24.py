import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')

print(df) #Prints the data frame

country_code = "RUS"

query_text = f"(iso_a3 == '{country_code}')" #getting the country code in the query

# print(len(df)) #print length of entire data frame
sub_df = df.query(query_text)
print(sub_df) #prints length of data frame with the condition

# print(sub_df)

# print(sub_df.loc[21]) #relies on the index
# print("\n")
# print(sub_df.iloc[21])

print(sub_df['dollar_price'].mean())

new_query = f"date > '2012-01-01' and date < '2012-12-31'"

new_date_df = df.query(new_query)

print(new_date_df)