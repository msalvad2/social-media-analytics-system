from linkedin import LinkedIn
import pytest


def test_linkedin_constructor_valid():
    #makes sure the constructor correctly creates the instance of the class
    obj = LinkedIn("123456789", 10, 5, 10, 20)

    assert obj._username == "123456789"
    assert obj._followers == 10
    assert obj._posts == 5
    assert obj._connections == 10
    assert obj._profile_views == 20


def test_linkedin_constructor_negative_connections_invalid():
    #cannot have negative connections
    with pytest.raises(ValueError):
        LinkedIn("123456789", 10, 5, -1, 20)


def test_linkedin_constructor_negative_profile_views_invalid():
    #cannot have negative profile views
    with pytest.raises(ValueError):
        LinkedIn("123456789", 10, 5, 10, -10)


def test_linkedin_constructor_zero_connections_valid():
    #cann have zero connections- boundary case
    obj = LinkedIn("123456789", 10, 5, 0, 20)

    assert obj._connections == 0
    assert obj._profile_views == 20


def test_linkedin_constructor_zero_profile_views_valid():
    #can have zero profile views - boundary case
    obj = LinkedIn("123456789", 10, 5, 10, 0)

    assert obj._connections == 10
    assert obj._profile_views == 0

########################################################################

#connection_acceptance_rate test functions


def test_connection_acceptance_rate_valid():
    #this will test to make sure the function works as expected
    obj = LinkedIn("123456789", 10, 5, 10, 20)
    result = obj.connection_acceptance_rate(20)  # connections = 10
    #this is what the function will do
    expected = 10/(10 + 20)*100
    assert result == expected


def test_connection_acceptance_rate_zero_requests_valid():
    #you can call the function with zero request, it just means you have a 100 percent acceptance rate
    obj = LinkedIn("123456789", 10, 5, 10, 20)
    result = obj.connection_acceptance_rate(0)

    expected = 10/(10+0) * 100
    assert result == expected


def test_connection_acceptance_rate_zero_connections_valid():
    #you can have zero connections and requests, it means you have 0 percent acceptance rate
    obj = LinkedIn("123456789", 10, 5, 0, 20)
    result = obj.connection_acceptance_rate(20)
    #this is what he function called should be doing
    expected = 0/(0+20)* 100
    assert result == expected


def test_connection_acceptance_rate_invalid_negative_requests():
    #You cannot have negative request
    obj = LinkedIn("123456789", 10, 5, 10, 20)

    with pytest.raises(ValueError):
        obj.connection_acceptance_rate(-1)


def test_connection_acceptance_rate_invalid_non_int_requests():
    #requests must be an integer!
    obj = LinkedIn("123456789", 10, 5, 10, 20)

    with pytest.raises(TypeError):
        obj.connection_acceptance_rate("yayihed")

########################################################################

#Profile_view_rate test functions
def test_profile_view_rate_valid():
    #makes sure the code works as expected
    obj = LinkedIn("123456789", 10, 5, 100, 60) 
    result = obj.profile_view_rate()
    #functin will divide profile views / month
    expected = 60 / 30 
    assert result == expected


def test_profile_view_rate_zero_views_valid():
    #it is valid to have zero views just means your view rate will be zero
    obj = LinkedIn("123456789", 10, 5, 100, 0)
    result = obj.profile_view_rate()

    expected = 0 / 30
    assert result == expected


def test_profile_view_rate_does_not_modify_object():
    
    obj = LinkedIn("123456789", 10, 5, 100, 60)

    #Save original object data members before calling function to make sure it doesnt modify object
    username = obj._username
    followers = obj._followers
    posts = obj._posts
    connections = obj._connections
    profile_views = obj._profile_views

    obj.profile_view_rate()

    assert obj._username == username
    assert obj._followers == followers
    assert obj._posts == posts
    assert obj._connections == connections
    assert obj._profile_views == profile_views
########################################################################

#Network_level test functions

def test_network_level_zero_messages_none():
    #this should return none, will check based on messages
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(0)
    assert result == "none"


def test_network_level_one_message_low():
    #this should return low- lower bound of low
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(1)
    assert result == "low"


def test_network_level_five_messages_low():
    #this should return low- upperbound of low
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(5)
    assert result == "low"


def test_network_level_six_messages_medium():
    #this should return medium - lowerbound of medium
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(6)
    assert result == "medium"


def test_network_level_twenty_messages_medium():
    #this should return medium - upperbound of medium
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(20)
    assert result == "medium"


def test_network_level_twentyone_messages_high():
    #this should return high -  lowerbound high
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    result = obj.network_level(21)
    assert result == "high"


def test_network_level_negative_messages_invalid():
    #messages count cannot be negative will throw a ValueError
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    with pytest.raises(ValueError):
        obj.network_level(-1)


def test_network_level_non_integer_messages_invalid():
    #messages argument must be an int
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    with pytest.raises(TypeError):
        obj.network_level("ten")


def test_network_level_does_not_modify_object():
    #The function should not modify the members
    obj = LinkedIn("123456789", 10, 5, 100, 200)

    # Save original state
    
    username = obj._username
    followers = obj._followers
    posts = obj._posts
    connections = obj._connections
    profile_views = obj._profile_views

    obj.network_level(10)

    assert obj._username == username
    assert obj._followers == followers
    assert obj._posts == posts
    assert obj._connections == connections
    assert obj._profile_views == profile_views

########################################################################

#display function test

def test_display_valid_case(capsys):
    obj = LinkedIn("123456789", 10, 5, 100, 200)
    obj.display()
    ##this will catch what is being displayed
    catch = capsys.readouterr().out

    assert "Connections: 100" in catch
    assert "Profile Views: 200" in catch


