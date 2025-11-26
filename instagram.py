from social_media import SocialMedia

class Instagram(SocialMedia):

    def __init__(self, username: str, followers: int, posts: int, total_reels: int, stories_per_day: int):
        super().__init__(username, followers, posts)

        if total_reels < 0 or stories_per_day < 0:
            raise ValueError("Total reels and Stories must both be greater than or equal to zero")
        
        self._total_reels = total_reels
        self._stories_per_day = stories_per_day

    def engagement(self, likes: int, comments: int):

        if likes < 0 or comments < 0:
            raise ValueError("Comments and Likes both have to be greater than or equal to zero!")
        if self._posts == 0:
            raise ValueError("Cannot Divide by Zero!")
        
        return (likes*3 + comments*5)/self._followers
    
    def story_activity(self):
        if self._stories_per_day == 0:
            return "low"
        elif self._stories_per_day >= 1 and self._stories_per_day <= 3:
            return "medium"
        elif self._stories_per_day >=4 and self._stories_per_day <= 5:
            return "high"
        else:
            return "too much"
        
    def average_like_per_post(self, likes: int):
        if not isinstance(likes, int):
            raise TypeError("Likes must be an integer!")
        if likes < 0:
            raise ValueError("Likes must be greater than or equal to zero!")
        if self._posts == 0:
            raise ValueError("Cannot divide by zero!")
        
        return likes/ self._posts
    
    def display(self):
        super().display()
        print(f"Total Reels: {self._total_reels}")
        print(f"Stories Per Day: {self._stories_per_day}")

