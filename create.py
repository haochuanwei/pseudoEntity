import pandas as pd
from pseudo.examples.hotel import RandomHotelGenerator as RHG
from pseudo.examples.person import RandomPersonGenerator as RPG

def create_df(method, n):
    entries = []
    for i in range(n):
        entries.append(pd.Series(method().info))
    df = pd.concat(entries, axis=1)
    df = df.transpose()
    return df

rpg = RPG()
rhg = RHG()

people = create_df(rpg.Person, 500)
people.drop_duplicates(subset=['chineseID'],inplace=True)
people.to_csv('people.csv', index=False)
hotels = create_df(rhg.Hotel, 50)
hotels.drop_duplicates(subset=['address'],inplace=True)
hotels.drop_duplicates(subset=['Tel'],inplace=True)
hotels.to_csv('hotels.csv', index=False)

