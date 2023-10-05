from peewee import Model, CharField, SqliteDatabase

# Define SQLite database
db = SqliteDatabase('users.db')

# Define User model
class User(Model):
    first_name = CharField()
    last_name = CharField()

    class Meta:
        database = db

    # Define custom logic to generate initials
    def generate_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"

# Initialize the database and create tables
db.connect()
db.create_tables([User])

# Create a new user
new_user = User(first_name='John', last_name='Doe')
new_user.save()

# Use the custom logic
initials = new_user.generate_initials()
print(f"Initials for {new_user.first_name} {new_user.last_name}: {initials}")
