
from social_media import SocialMedia

class TikTok(SocialMedia):

    def __init__(self, username: str, followers: int, posts: int, total_views: int, total_resposts: int):
        #will call the bases constructor and that will handle its own test cases
        super().__init__(username, followers, posts)
        if total_views < 0:
            raise ValueError("Total views cannot be negative!")
        
        if total_resposts < 0:
            raise ValueError("Total reposts cannot be negative!")
        
        #then we do the test cases for Tiktoks unique members
        self._total_views = total_views
        self._total_reposts = total_resposts

        

    def repost_rate(self):
        if self._posts <= 0:
            raise ValueError("Cannot divide be zero!)")
        
        return self._total_reposts / self._posts
    
    def is_viral(self, latest_views: int):
        if not isinstance(latest_views, int):
            raise TypeError("Latest views must be an int!")
        
        if latest_views <= 0:
            raise ValueError("Latest views must be greater than or equal to zero")
        
        return latest_views >= 10 * self._followers
    
    def engagement(self, likes: int, comments: int, shares: int):
        if likes < 0:
            raise ValueError("Likes cannot be negative")
        if comments < 0:
            raise ValueError("Comments cannot be negative")
        if shares < 0:
            raise ValueError("Shares cannot be negative")
        
        if self._followers <= 0:
            raise ValueError("Cannot divide by zero!")
        
        return (likes + comments + shares) / self._followers
    
    def display(self):
        super().display()
        print(f"Total Views: {self._total_views}")
        print(f"Total Reposts: {self._total_reposts}")

