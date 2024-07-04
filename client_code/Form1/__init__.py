from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    Name = self.text_box_1.text
    Email = self.text_box_2.text
    Address = self.text_box_3.text
    BirthDate = self.date_picker_1.date
    Gender = self.drop_down_2.selected_value
    Password = self.text_box_4.text
    anvil.server.call('submit', Name=Name, Email=Email, Address=Address, BirthDate=BirthDate, Gender=Gender, Password=Password)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass
