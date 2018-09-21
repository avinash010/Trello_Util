"""
Sample test to test trello util
"""
from trello_util import Trello_Util
from conf import key,token
import time
from data_conf import board_name,list_names,sample_board,sample_cards,member_ids,member_username

def test_trello_util(key,token):
    # Creating an object of Trello Util
    test_obj = Trello_Util(key,token)
    # Get the board names from conf
    board_names=board_name
    # Get Trello board names
    board_name_lists = test_obj.get_board_names()
    # Get the names which are already used from the board names 
    board_names_already_present=[x for x in board_names if any(x in y or y in x for y in board_name_lists)]
    # Do a diff and get the board names which can be used
    rem_board_name= list(set(board_names)-set(board_names_already_present))
    print "Remaining board names from current list: ",rem_board_name
    new_board_name = rem_board_name[0]
    
    # Create a new board
    result_flag = test_obj.add_board(new_board_name)
    if result_flag == True:
        print "Able to add card with name %s"% new_board_name
    else :
        print "Not able to add with name %s"% new_board_name
    
    # Add members to board
    result_flag = test_obj.add_member_board(new_board_name,member_ids)
    if result_flag == True:
        print "Able to add member to board"
    else :
        print "Not able to add member to board"
    
    # Add list (swim lane) to board
    result_flag = test_obj.add_list(new_board_name,list_names)
    if result_flag == True:
        print "Able to add list"
    else :
        print "Not able to add list"

    # Copy card to new board from an sample board
    result_flag = test_obj.copy_card(sample_board,sample_cards,new_board_name,"TODO")
    if result_flag == True:
        print "Able to copy card"
    else :
        print "Not able to copy card"
    
    # Assign member to copied board
    for card in sample_cards:
        test_obj.add_member_card(new_board_name,card,member_username)
    
    # Change preference or visibility (public,private or org )
    test_obj.change_preferences(new_board_name,"public")
    

if __name__ == '__main__':
    test_trello_util(key=key,token=token)
