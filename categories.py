import sqlite3
import os
import sys

args = sys.argv[1:]

if len(args) == 0:
    print "use -h for help\n use --rebuild for restore the db\n or --render <CategoryID>"
elif len(args) == 1
    if args[0] == "-h":
        print "use --rebuild for restore the db\n or --render <CategoryID>"
    elif args[0] == "--rebuild"
        print "Restoring database"
elif len(args) == 2 and args[0] == "--rebuild":


#
# def Challenge():
#     try:
#         os.remove('./db.db')
#     except Exception as e:
#         raise
#
#     try:
#         # Create table
#         conn.execute('''CREATE TABLE Categories
#                      (CategoryID integer,
#                      CategoryName text,
#                      CategoryLevel integer,
#                      BestOfferEnabled int,
#                      CategoryParentID int,
#                         FOREIGN KEY (CategoryParentID) REFERENCES supplier_groups(group_id))''')
#
#
#         # Save (commit) the changes
#         conn.commit()
#
#         # We can also close the connection if we are done with it.
#         # Just be sure any changes have been committed or they will be lost.
#         conn.close()
#     except Exception as e:
#         raise
# conn = sqlite3.connect('db.db')
