#Miguel Salvador
"""
PyTest test suite for SocialMedia base class.
Tests constructor, update_stats, operators, and engagement tracking.
"""
import pytest
from social_media import SocialMedia

#constructor test cases
def test_constructor_short_username():
    #invalid case: string is not atleast 8 characters long
    with pytest.raises(ValueError):
        obj1 = SocialMedia("Mike",2, 2)

def test_constructor_boundary_length_8():
    #Username minimum length is 8
    obj1 = SocialMedia("12345678", 2, 2)
    assert len(obj1._username) == 8

def test_constructor_negative_followers_invalid():
    #Followers must not be negative
    with pytest.raises(ValueError):
        obj1 = SocialMedia("Salvo12345", -1, 2)

def test_constructor_boundary_zero_followers():
    #Followers can be zero
    obj1 = SocialMedia("123456789", 0, 2)
    assert obj1._followers == 0

def test_constructor_negative_posts_invalid():
    #Posts cannot be negative
    with pytest.raises(ValueError):
        obj1 = SocialMedia("Salvo12345", 1, -1)

def test_constructor_zero_posts():
    #You can have zero posts
    obj1 = SocialMedia("123456789", 2, 0)
    assert obj1._posts == 0


def test_constructor_valid():
    #this will create a valid constructor
    obj1 = SocialMedia("123456789", 2, 2)
    assert len(obj1._username) == 9
    assert obj1._followers == 2
    assert obj1._posts == 2

############################################

#Update_stats Test
def test_update_stats_followers_non_int_invalid():
    obj1 = SocialMedia("123456789", 2, 2)
    #new followers has to be an int type
    with pytest.raises(TypeError):
        obj1.update_stats("Two", 2)

def test_update_stats_posts_non_int_invalid():
    obj1 = SocialMedia("123456789", 2, 2)
    #new posts must be an int type
    with pytest.raises(TypeError):
        obj1.update_stats(2, "Two")

def test_update_stats_followers_boundary_zero_valid():

    obj1 = SocialMedia("123456789", 2, 2)
    #new follower argument can be zero if posts is not
    obj1.update_stats(0, 2)
    #expected output
    assert obj1._followers == 2
    assert obj1._posts == 4

def test_update_stats_negative_followers_invalid():
    obj1 = SocialMedia("123456789", 2, 2)
    #invalid to pass a negative number as a new follower argument
    with pytest.raises(ValueError):
        obj1.update_stats(-1, 1)

def test_update_stats_posts_boundary_zero_followers_valid():
     obj1 = SocialMedia("123456789", 2, 2)
     #new posts argument can be zero if new followers argument is not
     obj1.update_stats(2, 0)

     assert obj1._followers == 4
     assert obj1._posts == 2
 
def test_update_stats_negative_posts_invalid():
    obj1 = SocialMedia("123456789", 2, 2)
    #invalid to pass negative # for new posts (argument)
    with pytest.raises(ValueError):
        obj1.update_stats(1, -1)

def test_update_stats_both_zero_invalid():
    obj1 = SocialMedia("123456789", 2, 2)
    #Invalid to call function when both new posts/followers is zero
    with pytest.raises(ValueError):
        obj1.update_stats(0,0)

def test_update_stats_followers_only_valid():
    obj1 = SocialMedia("123456789", 2, 2)
    #Valid to only followers
    obj1.update_stats(1,0)

    assert obj1._followers == 3
    assert obj1._posts == 2

def test_update_stats_posts_only_valid():
    obj1 = SocialMedia("123456789", 2, 2)
    #Valid to only change posts
    obj1.update_stats(0,1)
    assert obj1._followers == 2
    assert obj1._posts == 3

def test_update_stats_both_arguments_positive_valid():
    obj1 = SocialMedia("123456789", 2, 2)
    #valid to change both posts and new posts
    obj1.update_stats(2,2,)

    assert obj1._followers == 4
    assert obj1._posts == 4
############################################

#display test

def test_display_case_valid(capsys):
    obj1 = SocialMedia("123456789", 2, 2)
    obj1.display()
    #built in python function that intercepts what is printed in the terminal
    #capsys - build in python class which captures anything printed to the console during testing
    #readouterr - Method that retrieves anything that was printed so far (output & error streams)
    #.out -string containing everything the functin printed using print()
    output = capsys.readouterr().out
    #output now holds ""Username: 123456789\nFollowers: 2\nPosts: 2\n
    assert "Username: 12345678" in output
    assert "Followers: 2" in output
    assert "Posts: 2" in output
###############################################

#addition operator function

def test_add_other_more_followers_case():
    #if the other has more followers it keeps that username
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 5, 3)
    #should keep the 
    obj3 = obj1 + obj2

    assert obj3._username == "987654321"
    assert obj3._followers == 8
    assert obj3._posts == 5

def test_add_self_more_followers_case():
    #if the self has more followers it keeps that username
    obj1 = SocialMedia("123456789", 5, 3)
    obj2 = SocialMedia("987654321", 3, 2)
    #should keep the 
    obj3 = obj1 + obj2

    assert obj3._username == "123456789"
    assert obj3._followers == 8
    assert obj3._posts == 5

def test_add_self_other_equal_followers_case():
    #if the other and self have same followers it keeps the self username
    obj1 = SocialMedia("123456789", 5, 3)
    obj2 = SocialMedia("987654321", 5, 2)
    #should keep the 
    obj3 = obj1 + obj2

    assert obj3._username == "123456789"
    assert obj3._followers == 10
    assert obj3._posts == 5

def test_add_check_original_followers_posts_unchanged():
    
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 5, 3)
    #should keep the same values for the originals 
    obj3 = obj1 + obj2
    #checks to see that original objects have not changed
    assert obj1._username == "123456789"
    assert obj1._followers == 3
    assert obj1._posts == 2

    assert obj2._username == "987654321"
    assert obj2._followers == 5
    assert obj2._posts == 3

def test_add_non_SocialMedia_type():
    obj1 = SocialMedia("123456789", 3, 2)
    
    with pytest.raises(TypeError):
        obj3 = obj1 + 5

def test_add_followers_posts_valid():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 5, 3)
    #should keep the 
    obj3 = obj1 + obj2

    assert obj3._username == "987654321"
    assert obj3._followers == 8
    assert obj3._posts == 5
############################################

#less than or equal to operation overload function

def test_le_other_greater_return_true():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 5, 3)
    # "123456789" <= "987654321" → True
    flag = obj1 <= obj2

    assert flag == True

def test_le_self_greater_return_false():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 5, 3)
   # "987654321" <= "123456789" → False
    flag = obj2 <= obj1

    assert flag == False

def test_le_self_other_equal_return_true():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("123456789", 5, 3)
    # "987654321" <= "123456789" → False
    flag = obj2 <= obj1

    assert flag == True

def test_le_other_non_SocialMedia_type_invalid():
    obj1 = SocialMedia("123456789", 3, 2)
    with pytest.raises(TypeError):
        flag = obj1 <= 5

############################################

#testing the less than function

def test_lt_other_return_false():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 3, 2)

    result = obj2 < obj1

    assert result == False
    
def test_lt_other_return_true():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 3, 2)

    result = obj1 < obj2

    assert result == True
    
def test_lt_other_non_social_media_invalid():
    obj1 = SocialMedia("123456789", 3, 2)
    
    with pytest.raises(TypeError):
        result = obj1 < 5

############################################

#testing the equal to function

def test_eq_other_return_true():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("123456789", 3, 2)

    result = obj1 == obj2

    assert result == True
    

def test_equal_other_return_false():
    obj1 = SocialMedia("123456789", 3, 2)
    obj2 = SocialMedia("987654321", 3, 2)

    result = obj1 == obj2
    
    assert result == False


def test_equal_other_non_socialMedia_invalid():
    obj1 = SocialMedia("123456789", 3, 2)
    
    with pytest.raises(TypeError):
        result = obj1 == 5

############################################

def test_average_ratio_zero_engagement_ratios():
    obj1 = SocialMedia("123456789", 3, 2)
    with pytest.raises(ValueError):
        obj1.average_engagement_ratio()

def test_average_ratio_one_engagement_ratios():
    obj1 = SocialMedia("123456789", 10, 10)
    
    obj1.update_stats(10,10)

    result = obj1.average_engagement_ratio()

    assert result == 1

def test_average_ratio_multiple_engagement_ratios():
    obj1 = SocialMedia("123456789", 10, 10)
    obj1.update_stats(0,10)
    obj1.update_stats(20, 10)
    result = obj1.average_engagement_ratio()
    assert result == pytest.approx(1.5)


    































