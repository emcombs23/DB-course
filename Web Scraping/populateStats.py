from sqlmodel import Session
from models import Stats, engine
import pandas as pd

def generate_stats_instances():
    data = pd.read_csv('hurst_hockey_Stats.csv')
    stats_instances = []
    for index, row in data.iterrows():
        stats_instance = Stats(
            Number=row['Number'],
            FirstName=row['First'],
            LastName=row['Last'],
            GP=row['GP'],
            G=row['G'],
            A=row['A'],
            PTS=row['PTS'],
            SH=row['SH'],
            SH_PCT=row['SHOTPCT'],
            plus_minus=row['PLUSMINUS'],
            PPG=row['PPG'],
            SHG=row['SHG'],
            FG=row['FG'],
            GWG=row['GWG'],
            GTG=row['GTG'],
            OTG=row['OTG'],
            HTG=row['HTG'],
            UAG=row['UAG'],
            PN_PIM=row['PN-PIM'],
            MIN=row['MIN'],
            MAJ=row['MAJ'],
            OTH=row['OTH'],
            BLK=row['BLK']
        )
        stats_instances.append(stats_instance)
    return stats_instances

with Session(engine) as session:
    stats_instances = generate_stats_instances()
    session.add_all(stats_instances)
    session.commit()
