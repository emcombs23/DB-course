from sqlmodel import Session
from models import Faculty, engine

faculty1 = Faculty(firstName="Mahesh", lastName="Maddumala")
faculty2 = Faculty(firstName="Christopher", lastName="Mansour")
faculty3 = Faculty(firstName="Chad", lastName="Redmond")

with Session(engine) as session:
    session.add(faculty1)
    session.commit()