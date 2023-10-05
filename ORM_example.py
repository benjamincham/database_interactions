from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Initialize SQLite database
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
new_user = User(name='John', age=30)
session.add(new_user)
session.commit()

# Query data
for user in session.query(User).filter_by(name='John'):
    print(user.id, user.name, user.age)
