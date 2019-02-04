--------
A Python Trello API utility Script to create Trello Boards, Cards etc
--------
You can use this script to :

1. Create Trello Boards

2. Assign people to Board

3. Create Trello Cards

4. Assign people to card

5. Copy cards 

6. Add list items to a board

7. Change preference or visibility

You can refer to blog(https://qxf2.com/blog/python-trello-api-utility-script/) for more details. We have used Python Request module to make the API calls.

------
Setup 
------
Update the Trello API Key and Token in conf.py file

Update the data like board name, card name etc in data_conf.py

If you ran into some problems on step (d), please report them as an issue or email Avinash(avinash@qxf2.com)



---------------------------
COMMANDS FOR RUNNING SCRIPT
---------------------------

python test_trello_util.py


--------
ISSUES?
--------

a) If Python complains about an "Import" exception, please 'pip install $module_name'
