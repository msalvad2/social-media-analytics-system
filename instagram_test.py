#Miguel Salvador 
"""
PyTest test suite for Instagram class.
Tests Instagram-specific methods and data validation.
"""
from instagram import Instagram
import pytest

#constructor test
def test_instagram_constructor_valid():
    #checks for valid imput
    obj = Instagram("123456789", 10, 5, 3, 2)

    assert obj._username == "123456789"
    assert obj._followers == 10
    assert obj._posts == 5
    assert obj._total_reels == 3
    assert obj._stories_per_day == 2


def test_instagram_constructor_negative_total_reels_invalid():
    #Negative total reels is invalid
    with pytest.raises(ValueError):
        Instagram("123456789", 10, 5, -1, 2)


def test_instagram_constructor_negative_stories_invalid():
    #cannot have negative stories per day
    with pytest.raises(ValueError):
        Instagram("123456789", 10, 5, 3, -1)


def test_instagram_constructor_zero_values_valid():
    #you can have zero stories and zero posts per day
    obj = Instagram("123456789", 10, 5, 0, 0)

    assert obj._total_reels == 0
    assert obj._stories_per_day == 0


def test_instagram_constructor_non_integer_reels_invalid():
    #testing if user uses non int type for total reels
    with pytest.raises(TypeError):
        Instagram("123456789", 10, 5, "hello", 2)


def test_instagram_constructor_non_integer_stories_invalid():
    #testing if user puts non int type for stories per day
    with pytest.raises(TypeError):
        Instagram("123456789", 10, 5, 3, "hello")
##############################################################

#engagement test

def test_instagram_engagement_valid():
    #this is the valid case
    obj = Instagram("123456789", 10, 5, 3, 2) 
    result = obj.engagement(10, 5) 
    assert result == 5.5


def test_instagram_engagement_zero_likes_valid():
    #having zero likes is valid 
    obj = Instagram("123456789", 10, 5, 3, 2)
    result = obj.engagement(0, 5)  
    assert result == 2.5


def test_instagram_engagement_zero_comments_valid():
    #having zero comments is valid
    obj = Instagram("123456789", 10, 5, 3, 2)
    result = obj.engagement(10, 0) 
    assert result == 3


def test_instagram_engagement_negative_likes_invalid():
    #cannot have negative likes
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(ValueError):
        obj.engagement(-1, 5)


def test_instagram_engagement_negative_comments_invalid():
    #cannot have negative comments
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(ValueError):
        obj.engagement(10, -1)


def test_instagram_engagement_posts_zero_invalid():
    #cannot divide by zero aka post be zero
    # posts = 0 here
    obj = Instagram("123456789", 10, 0, 3, 2)
    with pytest.raises(ValueError):
        obj.engagement(10, 5)


def test_instagram_engagement_non_integer_likes_invalid():
    #likes has to be an integer
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(TypeError):
        obj.engagement("ten", 5)


def test_instagram_engagement_non_integer_comments_invalid():
    #comments has to be integer
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(TypeError):
        obj.engagement(10, "Whats good G")

##############################################################

# Story_Activity tests


def test_story_activity_zero_stories_returns_low():
    #will check the stories is zero and should return low
    obj = Instagram("123456789", 10, 5, 3, stories_per_day=0)

    result = obj.story_activity()

    assert result == "low"


def test_story_activity_one_story_returns_medium():
    #should return medium
    obj = Instagram("123456789", 10, 5, 3, stories_per_day=1)

    result = obj.story_activity()

    assert result == "medium"


def test_story_activity_three_stories_returns_medium():
    #shoudl return medium since it is upperbound
    obj = Instagram("123456789", 10, 5, 3, stories_per_day=3)

    result = obj.story_activity()

    assert result == "medium"


def test_story_activity_four_stories_returns_high():
   #should return high
    obj = Instagram("123456789", 10, 5, 3, stories_per_day=4)

    result = obj.story_activity()

    assert result == "high"


def test_story_activity_large_stories_returns_high():
    #should return too much
    obj = Instagram("123456789", 10, 5, 3, stories_per_day=6)

    result = obj.story_activity()

    assert result == "too much"
##############################################################

#Average likes per Post test functions


def test_average_like_per_post_valid():
    #this is the valid case what its suppose to do likes/ posts
    obj = Instagram("123456789", 10, 5, 3, 2)  
    result = obj.average_like_per_post(20)     
    assert result == 4


def test_average_like_per_post_zero_likes_valid():
    #works when likes are zero
    obj = Instagram("123456789", 10, 5, 3, 2)
    result = obj.average_like_per_post(0)       # 0 / 5 = 0
    assert result == 0


def test_average_like_per_post_negative_likes_invalid():
    #cannot have negative likes
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(ValueError):
        obj.average_like_per_post(-1)


def test_average_like_per_post_non_integer_likes_invalid():
    #likes must be an int
    obj = Instagram("123456789", 10, 5, 3, 2)
    with pytest.raises(TypeError):
        obj.average_like_per_post("mi casa es su casa")


def test_average_like_per_post_posts_zero_invalid():
    #cannot divide by zero aka post be zero
    obj = Instagram("123456789", 10, 0, 3, 2) 
    with pytest.raises(ValueError):
        obj.average_like_per_post(10)

##############################################################

#display test case
def test_display_valid_case(capsys):
    obj = Instagram("123456789", 10, 5, 3, 2) 
    obj.display()

    catch = capsys.readouterr().out
    assert "Total Reels: 3" in catch
    assert "Stories Per Day: 2" in catch