from tiktok import TikTok
import pytest


def test_tiktok_constructor_total_views_zero_valid():
    
    obj = TikTok("123456789", 3, 2, 0, 5)
    #check to see if constructor worked for total views being zero
    assert obj._total_views == 0
    assert obj._total_reposts == 5

def test_tiktok_constructor_total_reposts_zero_valid():
      
    obj = TikTok("123456789", 3, 2, 5, 0)
    #check to see if constructor worked for total reposts being zero
    assert obj._total_views == 5
    assert obj._total_reposts == 0

def test_tiktok_constructor_both_zero_valid():
    
    obj = TikTok("123456789", 3, 2, 0, 0)
    #check to see if constructor worked for total reposts being zero
    assert obj._total_views == 0
    assert obj._total_reposts == 0


def test_tiktok_constructor_negative_total_views_invalid():
    with pytest.raises(ValueError):
        obj = TikTok("123456789", 3, 2, -5, 5)


def test_tiktok_constructor_negative_total_reposts_invalid():
    with pytest.raises(ValueError):
        obj = TikTok("123456789", 3, 2, 5, -5)


def test_tiktok_constructor_non_int_total_views_invalid():
    with pytest.raises(TypeError):
        obj = TikTok("123456789", 3, 2, "Hello", 5)


def test_tiktok_constructor_non_int_total_reposts_invalid():
    with pytest.raises(TypeError):
        obj = TikTok("123456789", 3, 2, 5, "Hello")

def test_tiktok_constructor_valid():
        obj = TikTok("123456789", 3, 2, 5, 5)

        assert obj._total_views == 5
        assert obj._total_reposts == 5

def test_tiktok_inheritance_base_members_case():
    obj = TikTok("123456789", 3, 2, 5, 5)
    #will test the tiktok calls the base class constructor
    assert obj._username == "123456789"
    assert obj._followers == 3
    assert obj._posts == 2
########################################################################

#repost rate

def test_repost_rate_zero_reposts_valid():
    obj = TikTok("123456789", 3, 2, 5, 0)
    rate = obj.repost_rate()

    assert rate == 0
    

def test_repost_rate_posts_zero_invalid():
    obj = TikTok("123456789", 3, 0, 5, 5)
    with pytest.raises(ValueError):
        rate = obj.repost_rate()
        
    

def test_repost_rate_does_not_modify_members():
    obj = TikTok("123456789", 3, 2, 5, 5)
    rate = obj.repost_rate()

    assert obj._username == "123456789"
    assert obj._followers == 3
    assert obj._posts == 2
    assert obj._total_views == 5
    assert obj._total_reposts == 5

def test_repost_rate_posts_one_boundary_valid():
    obj = TikTok("123456789", 3, 1, 5, 5)
    #boundary case is post being 1
    rate = obj.repost_rate()
    
    assert rate == 5 


def test_repost_rate_valid():
    obj = TikTok("123456789", 3, 20, 5, 10)
    #boundary case is post being 1
    rate = obj.repost_rate()
    
    assert rate == .5


########################################################################

#is_viral

def test_is_viral_true_when_above_threshold():
    obj = TikTok("123456789", 10, 2, 5, 5)
    viral = obj.is_viral(101)

    assert viral == True

    

def test_is_viral_false_when_below_threshold():
    obj = TikTok("123456789", 10, 2, 5, 5)
    viral = obj.is_viral(1)

    assert viral == False

def test_is_viral_true_at_exact_threshold_boundary():
    obj = TikTok("123456789", 10, 2, 5, 5)
    viral = obj.is_viral(100)

    assert viral == True

def test_is_viral_negative_latest_view_invalid():
    obj = TikTok("123456789", 10, 2, 5, 5)

    with pytest.raises(ValueError):
        viral = obj.is_viral(-5)
        


def test_is_viral_non_int_latest_view_invalid():
    obj = TikTok("123456789", 10, 2, 5, 5)

    with pytest.raises(TypeError):
        obj.is_viral("Hello")

def test_is_viral_does_not_modify_members():
    obj = TikTok("123456789", 15, 2, 5, 5)
    viral = obj.is_viral(300)

    assert obj._username == "123456789"
    assert obj._followers == 15
    assert obj._posts == 2
    assert obj._total_views == 5
    assert obj._total_reposts == 5

########################################################################

#engagement


def test_engagement_all_zero_valid():
    obj = TikTok("123456789", 10, 2, 5, 5)
    engagement = obj.engagement(0, 0, 0)
    assert engagement == 0


def test_engagement_negative_likes_invalid():
    obj = TikTok("123456789", 10, 2, 5, 5)
    with pytest.raises(ValueError):
        engagement = obj.engagement(-1, 1, 1)
    

def test_engagement_negative_comments_invalid():
    obj = TikTok("123456789", 10, 2, 5, 5)
    with pytest.raises(ValueError):
        engagement = obj.engagement(1, -1, 1)

def test_engagement_negative_shares_invalid():
   obj = TikTok("123456789", 10, 2, 5, 5)
   with pytest.raises(ValueError):
        engagement = obj.engagement(1, 1, -1)

def test_engagement_non_int_likes_invalid():
    obj = TikTok("123456789", 3, 2, 5, 5)
    with pytest.raises(TypeError):
        obj.engagement("hello", 1, 1)

def test_engagement_followers_zero_invalid():
    obj = TikTok("123456789", 0, 2, 5, 5)
    with pytest.raises(ValueError):
        obj.engagement(1,1,1)
    

def test_engagement_does_not_modify_members():
    obj = TikTok("123456789", 10, 2, 5, 5)
    obj.engagement(1,1,1)

    assert obj._username == "123456789"
    assert obj._followers == 10
    assert obj._posts == 2
    assert obj._total_views == 5
    assert obj._total_reposts == 5


def test_engagement_valid():
    obj = TikTok("123456789", 10, 2, 5, 5)
    absorbed = obj.engagement(1,1,1)

    assert absorbed == .3

########################################################################

#display

def test_display_case_valid(capsys):
    obj = TikTok("123456789", 10, 2, 5, 5)
    obj.display()

    catch = capsys.readouterr().out
    assert "Total Views: 5" in catch
    assert "Total Reposts: 5" in catch
