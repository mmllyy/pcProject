from db import  DBHelp
from item import UserItem

db_ = DBHelp()
print(db_.exist('user',1))
item = UserItem(1,'summer',20,'','')
db_.save(item)
