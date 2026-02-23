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

