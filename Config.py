"""
Example
Note: Variables 1-9 - user`s variable, any. Variables 10, 11 - additional functionality for admin. This functionality allows
to see all users and their password, and to see changes with DB during work
"""

# DATA FOR ENTER TO DATABASE
host = "127.0.0.1"
user = "postgres"
password = "123"
db_name = "youth_festival"

# CONFORMITY A TABLE AND DATA (var[0] - Name in GUI, var[1] - name in DB)
var1 = ['Dancers', 'dancers']
var2 = ['Photographs', 'foto']
var3 = ['Guests', 'guest']
var4 = ['Shop', 'shop']
var5 = ['Singers', 'songers']
var6 = ['Souvenirs', 'souvenirs']
var7 = ['Square', 'square']
var8 = ['T_shirt', 't_shirt']
var9 = ['Tatoo', 'tatoo']
var10 = ['Users', 'users']  # necessary       - a___m___n (admin)
var11 = ['Actions', 'actions']  # necessary   - __d___i__ (admin)
vars = [var9, var8, var7, var6, var5, var4, var3, var2, var1]
vars_admin = [var11, var10, var9, var8, var7, var6, var5, var4, var3, var2, var1]
