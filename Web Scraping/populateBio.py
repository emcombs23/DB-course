from sqlmodel import Session
from models import Bio, engine
import pandas as pd

def generate_bio_instances():
    data = pd.read_csv('hurst_hockey_roster.csv')
    bio_instances = []
    for index, row in data.iterrows():
        bio_instance = Bio(
            firstName=row['FirstName'],
            lastName=row['LastName'],
            jersyNumber=row['JerseyNumber'],
            position=row['Position'],
            height=row['Height'],
            weight=row['Weight'],
            academicYear=row['AcademicYear'],
            hometown=row['Hometown'],
            highSchool=row['Highschool']
        )
        bio_instances.append(bio_instance)
    return bio_instances

with Session(engine) as session:
    bio_instances = generate_bio_instances()
    session.add_all(bio_instances)
    session.commit()
