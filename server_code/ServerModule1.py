import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def submit(Name, Email, Address, BirthDate, Gender, Password):
    app_tables.new_user.add_row(Name=Name, Address=Address, Email=Email, BirthDate=BirthDate, Gender=Gender, Password=Password)
