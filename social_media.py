class SocialMedia:
    #constructor
    def __init__(self, username: str, followers: int, posts: int):

        if len(username) < 8:
            raise ValueError("Username must be 8 characters long!")

        if followers < 0:
            raise ValueError("Followers cannot be negative!")
        
        if posts < 0:
            raise ValueError("Posts cannot be negative!")
        

        self._username = username
        self._followers = followers
        self._posts = posts

    def update_stats(self, new_followers: int, new_posts: int):
        if new_posts < 0:
            raise ValueError("You cannot add negative posts to total posts count!")
        
        if new_followers < 0:
            raise ValueError("You cannot add negative followers to the total follower count!")
        
        if new_followers <= 0 and new_posts <= 0:
            raise ValueError("Nothing to update!")
        #if new_followers or new_posts is not type int, python will automatically raise a TypeError!
        self._followers += new_followers
        self._posts += new_posts


    def display(self):
        print(f"Username: {self._username}")
        print(f"Followers: {self._followers}")
        print(f"Posts: {self._posts}")

    def __add__(self, other: "SocialMedia"):

        if not isinstance(other, SocialMedia):
            raise TypeError("Invalid you must add to objects of same type together!")
        
        temp = SocialMedia("0000000000", 0, 0)
        if self._followers >= other._followers:
            temp._username = self._username
        else:
            temp._username = other._username
        
        temp._followers = self._followers + other._followers
        temp._posts = self._posts + other._posts

        return temp

    def __le__(self, other: "SocialMedia"):

        if not isinstance(other, SocialMedia):
            raise TypeError("You must compare objects of same class!")

        if self._username <= other._username:
            return True
        else:
            return False
    
    

