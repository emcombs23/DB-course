from sqlmodel import Session, select
from models import engine, Bio, Stats
import pandas as pd
from sqlalchemy import func


with Session(engine) as session:
    #SELECT Everything from Bio
    statement = select(Bio)

    #Select only first_name, last_name, and position from Bio.
    statement = select(Bio.firstName, Bio.lastName, Bio.position)

    #Find players with weight > 200.
    statement = select(Bio.firstName, Bio.lastName, Bio.weight).where(Bio.weight > 200)

    #Find players where position == "Goaltender" OR weight > 170.
    statement = (
        select(Bio.firstName, Bio.lastName, Bio.position, Bio.weight)
        .where((Bio.position == "Goaltender") | (Bio.weight > 170))
        .order_by(Bio.weight.desc())
    )

    #Find players where position == "Goaltender" AND weight > 190
    statement = (
        select(Bio.firstName, Bio.lastName, Bio.position, Bio.weight)
        .where((Bio.position == "Goaltender") | (Bio.weight > 190))
    )

    #Last Name Begins with "S"
    statement = (
        select(Bio.firstName, Bio.lastName)
        .where(Bio.lastName.like("S%"))
    )
    
    #Show players ordered by position, then last_name.
    statement = (
        select(Bio.firstName, Bio.lastName, Bio.position)
        .order_by(Bio.position, Bio.lastName)
    )
    
    #Group Bio by position and count players.
    statement = (
        select(Bio.position, func.count().label('NumPlayers'))
        .group_by(Bio.position)
        .order_by(func.count().desc())
    )

    #Average weight per position, but only groups with avg > 190.
    statement = (
        select(Bio.position, func.avg(Bio.weight).label('AvgWeight'))
        .group_by(Bio.position)
        .having(func.avg(Bio.weight) > 190)
        .order_by(func.avg(Bio.weight).desc())
    )

    #Join Bio and Stats to show first_name, last_name, and games_played.
    statement = (
        select(Bio.firstName, Bio.lastName,Stats.GP)
        .join(Stats, (Bio.firstName == Stats.FirstName)&(Bio.lastName == Stats.LastName))
    )
    records = session.exec(statement).all()

df = pd.DataFrame(records)
print(df)
'''
recordsList = []
for record in records:
    recordsList.append(record.model_dump())
for element in recordsList:
    print(element)

df = pd.DataFrame(recordsList)
print(df)
'''

