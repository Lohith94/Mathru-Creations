from database_setup import Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine=create_engine('sqlite:///mathru.db', connect_args={'check_same_thread':False})

#Bind the above engine to the session
Session=sessionmaker(bind=engine)

#Create a session object
session=Session()

#Items for videos
category1=Category(name="Programs")
session.add(category1)
session.commit()

item1=Item(name="Journey", description="", category=category1)
session.add(item1)
session.commit()

item2=Item(name="Ad-Campaign", description="", category=category1)
session.add(item2)
session.commit()

#Items for Print Media
category2=Category(name="Print Media")
session.add(category2)
session.commit()

item1=Item(name="Magzine", description="", category=category2)
session.add(item1)
session.commit()

#Items for Tidbits
category3=Category(name="Tidbits")
session.add(category3)
session.commit()

item1=Item(name="Producer", description="", category=category3)
session.add(item1)
session.commit()

item2=Item(name="Director", description="", category=category3)
session.add(item2)
session.commit()

item3=Item(name="Journey", description="", category=category3)
session.add(item3)
session.commit()

#Items for Gallery
category4=Category(name="Gallery")
session.add(category4)
session.commit()

item1=Item(name="Photos", category=category4)
session.add(item1)
session.commit()

item2=Item(name="Videos", category=category4)
session.add(item2)
session.commit()

print("Added Items!")
