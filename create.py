import random
import pandas as pd
from pseudo.examples.hotel import RandomHotelGenerator as RHG
from pseudo.examples.person import RandomPersonGenerator as RPG
from pseudo.relationship import Lodging

def create_df(ents):
    entries = []
    for x in ents:
        entries.append(pd.Series(x.info))
    df = pd.concat(entries, axis=1)
    df = df.transpose()
    return df

rpg = RPG()
rhg = RHG()

people_obj = [rpg.person() for i in range(0, 50)]
hotels_obj = [rhg.hotel()  for i in range(0, 10)]
lodges_obj = [Lodging(random.choice(people_obj), random.choice(hotels_obj)) for i in range(0, 1000)]

people = create_df(people_obj)
hotels = create_df(hotels_obj)
people.drop_duplicates(subset=['chineseID'],inplace=True)
people.to_csv('people.csv', index=False)
hotels.drop_duplicates(subset=['address'],inplace=True)
hotels.drop_duplicates(subset=['Tel'],inplace=True)
hotels.to_csv('hotels.csv', index=False)

lodgings = create_df(lodges_obj)
lodgings.to_csv('lodgings.csv', index=False)


