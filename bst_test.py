#Miguel Salvador | Program #5 | Dec 5, 2025
"""
Binary Search Tree implementation for storing social media profiles.
Supports insert, retrieve, display (in-order), and remove operations.
"""
import pytest
from bst import Node
from bst import BST
from social_media import SocialMedia

#the nodes constructor

#checks to see if the data is stored properly
def test_Node_constructor_valid_data_storing():
    original = SocialMedia("123456789", 3, 2)
    new_node = Node(original)

    assert new_node.get_data() == original

#checks to see left is set to None
def test_Node_constructor_valid_left_is_none():
    original = SocialMedia("123456789", 3, 2)
    new_node = Node(original)

    assert new_node.get_left() is None

#checks to see right is set to None
def test_Node_constructor_valid_right_is_none():
    original = SocialMedia("123456789", 3, 2)
    new_node = Node(original)

    assert new_node.get_right() is None

#I test both set and get left since you can't test them without each other
def test_Node_get_and_set_left_node():
    original = SocialMedia("123456789", 3, 2)
    duplicate = SocialMedia("987654321", 3, 2)

    node1 = Node(original)
    node2 = Node(duplicate)

    node1.set_left(node2)
    #I check to see if get left is pointing to the right node and if its data was not altered in the process
    assert node1.get_left() == node2
    assert node1.get_left().get_data() == duplicate

def test_Node_get_and_set_right_node():
    original = SocialMedia("123456789", 3, 2)
    duplicate = SocialMedia("987654321", 3, 2)

    node1 = Node(original)
    node2 = Node(duplicate)

    node1.set_right(node2)

    assert node1.get_right() == node2
    assert node1.get_right().get_data() == duplicate




########################################################

#the tests for the tree's constructor

def test_constructor_empty_retrieve():
    tree = BST()
    #since tree is empty it should not retrieve 
    result = tree.retrieve("HI!")

    assert result is None
    

def test_constructor_remove_when_empty():
    tree = BST()
    #tree is empty and it should not crash
    result = tree.remove("Howdy")

    assert result is None

def test_constructor_display_when_empty(capsys):
    tree = BST()
    #tree is empty and should not display anything

    tree.display()
    #this will catch is is being displayed
    catch = capsys.readouterr().out
    #catch should be empty since nothing to display

    assert catch == ""

def test_constructor_insert_empty():
    tree = BST()

    original = SocialMedia("123456789", 3, 2)
    tree.insert(original)
    #now we check to see if it was 

    result = tree.retrieve("123456789")

    assert result == original

########################################################

#test cases for the insert function

#will insert into an empty list and then retrieve it
def test_insert_into_empty():
    tree = BST()
    obj = SocialMedia("123456789", 3, 2)

    tree.insert(obj)
    #retrieve will return the data in the node found
    result = tree.retrieve("123456789")

    assert result == obj

#this function will add two nodes, the second having to traverse to the left
def test_insert_two_nodes_goes_left():

    tree = BST()
    left = SocialMedia("123456789", 3, 2)
    root = SocialMedia("987654321", 3, 2)

    tree.insert(root)
    #should insert to the left
    tree.insert(left)

    assert tree.retrieve("123456789") == left
    assert tree.retrieve("987654321") == root

#function will add two nodes and for the second one will traverse to the right to insert
def test_insert_two_nodes_goes_right():
    tree = BST()
    root = SocialMedia("123456789", 3, 2)
    right = SocialMedia("987654321", 3, 2)

    tree.insert(root)
    #should insert to the right
    tree.insert(right)

    assert tree.retrieve("123456789") == root
    assert tree.retrieve("987654321") == right

#this will make sure that duplicates are not inserted in the tree
def test_insert_duplicate_not_allowed():
    tree = BST()
    original = SocialMedia("123456789", 3, 2)
    duplicate = SocialMedia("123456789", 3, 2)

    tree.insert(original)
    #since duplicate has same username it should keep the original username(original)
    with pytest.raises(ValueError):
        tree.insert(duplicate)

    

def test_insert_non_socialMedia_invalid():
    tree = BST()

    with pytest.raises(TypeError):
        tree.insert(21)

    with pytest.raises(TypeError):
        tree.insert("Hello!")

########################################################

#the test cases for the retrieve function
def test_retrieve_empty_tree_returns_none():
    tree = BST()
    result = tree.retrieve("Hello!")
    #the function should return None since tree is empty
    assert result is None

def test_retrieve_not_found_tree_returns_none():
    tree = BST()
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 3, 2)
    
    tree.insert(obj1)
    tree.insert(obj2)
    #this should return none since hello is not in the tree
    result = tree.retrieve("Hello!")

    assert result is None


def test_retrieve_root_node_success():
    tree = BST()
    obj1 = SocialMedia("123456789", 3, 2)

    tree.insert(obj1)
    #we will retrieve the root
    result = tree.retrieve("123456789")

    assert result == obj1

def test_retrieve_left_subtree_success():
    tree = BST()
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)

    tree.insert(obj2)
    tree.insert(obj1)
    tree.insert(obj3)

    #we will retrieve the roots left node

    result = tree.retrieve("123456789")

    assert result == obj1


def test_retrieve_right_subtree_success():
    tree = BST()
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)

    tree.insert(obj2)
    tree.insert(obj1)
    tree.insert(obj3)

    #we will retrieve the roots right node

    result = tree.retrieve("999999999")

    assert result == obj3

def test_retrieve_deep_node_success():
    tree = BST()
    #will become the root
    obj_m = SocialMedia("muser12345", 3, 2)
    #will go the left of the root m
    obj_f = SocialMedia("fuser12345", 3, 2)
    #will go to the right of m
    obj_t = SocialMedia("tuser12345", 3, 2)
    #will go to the left of f
    obj_b = SocialMedia("buser12345", 3, 2)

    tree.insert(obj_m)
    tree.insert(obj_f)
    tree.insert(obj_t)
    tree.insert(obj_b)

    result = tree.retrieve("buser12345")

    assert result == obj_b

def test_retrieve_invalid_key_type_raises_typeerror():
    tree = BST()
    
    with pytest.raises(TypeError):
        tree.retrieve(5)

########################################################

#the test cases for my display function

#will display an empty tree 
def test_display_empty_tree(capsys):
    tree = BST()

    tree.display()
    #catches what is being displayed to the terminal
    catch = capsys.readouterr().out

    assert catch == ""

#will display a tree the has nodes
def test_display_non_empty_tree(capsys):
    tree = BST()

    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)

    tree.insert(obj2)
    tree.insert(obj1)
    tree.insert(obj3)

    tree.display()
    #catch contains what is being displayer
    catch = capsys.readouterr().out
    #checks to see that the right info was diplayed
    assert "123456789" in catch
    assert "555555555" in catch
    assert "999999999" in catch

def test_display_not_modify_tree():
    tree = BST()

    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)

    tree.insert(obj2)
    tree.insert(obj1)
    tree.insert(obj3)

    tree.display()

    assert tree.retrieve("123456789") == obj1
    assert tree.retrieve("555555555") == obj2
    assert tree.retrieve("999999999") == obj3

def test_display_check_if_displaying_in_order(capsys):
    tree = BST()

    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)

    #root
    tree.insert(obj2)
    #root->left
    tree.insert(obj1)
    #root->right
    tree.insert(obj3)
    #should display obj1 then obj2 then obj3
    tree.display()

    catch = capsys.readouterr().out
    #checks that all are present
    assert "123456789" in catch
    assert "555555555" in catch
    assert "999999999" in catch
    #Since catch is just one long string that contains what was displayed to terminal
    #catch.index will check at what index that object is found
    #So we can check the it was displayed in order
    index_obj1 = catch.index("123456789")
    index_obj2 = catch.index("555555555")
    index_obj3 = catch.index("999999999")
    
    assert index_obj1 < index_obj2 < index_obj3

########################################################

#this will test the remove function

def test_remove_from_empty_tree():
    tree = BST()
    #if tree is empty should return None
    result = tree.remove("Hello!")

    assert result is None


def test_remove_username_non_socialMedia_type():
    tree = BST()

    with pytest.raises(TypeError):
        tree.remove(5)

def test_remove_non_existing_username():
    #if username does not exist in tree should return None
    tree = BST()

    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)
    #root
    tree.insert(obj2)
    #root->left
    tree.insert(obj1)
    #root->right
    tree.insert(obj3)
    
    #we will attempt to delete using a username that doesn't exist
    result = tree.remove("378640283603845")

    assert result is None


def test_remove_leaf_node():
    tree = BST()

    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("555555555", 3, 2)
    obj3 = SocialMedia("999999999", 3 , 2)
    #root
    tree.insert(obj2)
    #root->left
    tree.insert(obj1)
    #root->right
    tree.insert(obj3)

    #we will delete obj1 which is a leaf
    tree.remove("123456789")

    #now we will see if it was removed in the tree

    assert tree.retrieve("123456789") is None
    #now we check that the other two were not changed
    assert tree.retrieve("555555555") == obj2
    assert tree.retrieve("999999999") == obj3



def test_remove_node_with_one_left_child():
    tree = BST()
    obj3 = SocialMedia("333333333", 3, 2)
    obj4 = SocialMedia("444444444", 3, 2)
    obj5 = SocialMedia("555555555", 3 , 2)
    obj7 = SocialMedia("777777777", 3, 2)
    obj6 = SocialMedia("666666666", 3, 2)
    
    tree.insert(obj5)
    tree.insert(obj3)
    tree.insert(obj7)
    tree.insert(obj4)
    tree.insert(obj6)

    #obj7 has only a left pointer so we will delete it
    tree.remove("777777777")

    assert tree.retrieve("777777777") is None


def test_remove_node_with_one_right_child():

    tree = BST()
    obj3 = SocialMedia("333333333", 3, 2)
    obj4 = SocialMedia("444444444", 3, 2)
    obj5 = SocialMedia("555555555", 3 , 2)
    obj7 = SocialMedia("777777777", 3, 2)
    obj6 = SocialMedia("666666666", 3, 2)
    
    tree.insert(obj5)
    tree.insert(obj3)
    tree.insert(obj7)
    tree.insert(obj4)
    tree.insert(obj6)

    #obj3 has only a left pointer so we will delete it
    tree.remove("333333333")

    assert tree.retrieve("333333333") is None

def test_remove_node_with_two_children():

    tree = BST()
    obj3 = SocialMedia("333333333", 3, 2)
    obj4 = SocialMedia("444444444", 3, 2)
    obj5 = SocialMedia("555555555", 3 , 2)
    obj7 = SocialMedia("777777777", 3, 2)
    obj6 = SocialMedia("666666666", 3, 2)
    obj8 = SocialMedia("888888888", 3, 2)
    
    tree.insert(obj5)
    tree.insert(obj3)
    tree.insert(obj7)
    tree.insert(obj4)
    tree.insert(obj6)
    tree.insert(obj8)

    #obj7 has both a left and right pointers now so we will remove it
    tree.remove("777777777")

    assert tree.retrieve("777777777") is None


def test_remove_keeps_other_nodes():
    tree = BST()
    obj3 = SocialMedia("333333333", 3, 2)
    obj4 = SocialMedia("444444444", 3, 2)
    obj5 = SocialMedia("555555555", 3 , 2)
    obj7 = SocialMedia("777777777", 3, 2)
    obj6 = SocialMedia("666666666", 3, 2)
    obj8 = SocialMedia("888888888", 3, 2)
    
    tree.insert(obj5)
    tree.insert(obj3)
    tree.insert(obj7)
    tree.insert(obj4)
    tree.insert(obj6)
    tree.insert(obj8)

    #obj7 has both a left and right pointers now so we will remove it
    tree.remove("777777777")

    assert tree.retrieve("777777777") is None
    #now we check to see if the other nodes are in the tree unaffected by the remove

    assert tree.retrieve("333333333") == obj3
    assert tree.retrieve("444444444") == obj4
    assert tree.retrieve("555555555") == obj5
    assert tree.retrieve("666666666") == obj6
    assert tree.retrieve("888888888") == obj8

