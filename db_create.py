from app import db
from models import User

#create the database and db tables
db.create_all()

#insert
db.session.add(User("Adebayo Adepoju", "08062191817", "mradeybee@gmail.com", "yaba lagos", "Table 1"))
db.session.add(User("Adebayo Adepoju", "08062191817", "mradeybee@gmail.com", "yaba lagos", "Table 2"))

#commit the changes
db.session.commit()