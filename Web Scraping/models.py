from sqlmodel import SQLModel, Field

class Bio(SQLModel, table=True):
    firstName: str = Field(primary_key=True)
    lastName: str = Field(primary_key=True)
    jersyNumber: int | None = None
    position: str | None = None
    height: str | None = None
    weight: int | None = None
    hometown: str | None = None
    academicYear: str | None = None
    highSchool: str | None = None

class Stats(SQLModel, table=True):
    firstName: str = Field(primary_key=True)
    lastName: str = Field(primary_key=True)
    gamesPlayed: int | None = None
    goals: int | None = None
    assists: int | None = None
    points: int | None = None
    plusMinus: int | None = None
    penaltyMinutes: int | None = None

