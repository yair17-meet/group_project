from model import *


engine = create_engine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()






users = [

{'id':1,'username': 'name1', 'email':'email1','password':'password1', 'erea': 'erea1', 'art':'art1' },
{'id':2,'username': 'name2', 'email':'email2','password':'password2', 'erea': 'erea2', 'art':'art2' },
{'id':3,'username': 'name3', 'email':'email3','password':'password3', 'erea': 'erea3', 'art':'art3' },
{'id':4,'username': 'name4', 'email':'email4','password':'password4', 'erea': 'erea4', 'art':'art4' },

]

groups = [

{'id':1 ,'name': 'group1', 'topic': 'topic1', 'user_id': 1},
{'id':2 ,'name': 'group2', 'topic': 'topic2', 'user_id': 2},
{'id':3 ,'name': 'group3', 'topic': 'topic3', 'user_id': 3},
{'id':4 ,'name': 'group4', 'topic': 'topic4', 'user_id': 4},
]

for user in users:
    newUser = User(id=user['id'], username=user["username"], email=user['email'],password_hash=user['password'], erea = user['erea'], art = user['art'])
    session.add(newUser)
    session.commit()

for group in groups:
    newGroup = Group(id = group['id'], name=group['name'], topic=group['topic'], user_id=group['user_id'])
    session.add(newGroup)
    session.commit()

