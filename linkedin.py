#Miguel Salvador
"""
LinkedIn profile class - derived from SocialMedia.
Tracks connections, profile views, and professional networking metrics.
"""
from social_media import SocialMedia

class LinkedIn(SocialMedia):
    def __init__(self, username: str, followers: int, posts: int, connections: int, profile_views: int):
        super().__init__(username, followers, posts)
        if profile_views < 0 or connections < 0:
            raise ValueError("Profile Views and Connections cannot be less than zero!")
        
        self._connections = connections
        self._profile_views = profile_views

    def connection_acceptance_rate(self, requests: int):
        if not isinstance(requests, int):
            raise TypeError("Request must be an integer!")
        if requests < 0:
            raise ValueError("Requests cannot be negative!")
        
        return self._connections / (self._connections + requests) * 100
    
    def profile_view_rate(self):
        
        return self._profile_views / 30
    
    def network_level(self, messages: int):
        if not isinstance(messages, int):
            raise TypeError("Messages must be an int!")
        if messages < 0:
            raise ValueError("Messages must be greater than or equal to zero!")
        
        if messages == 0:
            return "none"
        elif messages >= 1 and messages <= 5:
            return "low"
        elif messages >= 6 and messages <= 20:
            return "medium"
        else:
            return "high"

    def display(self):
        super().display()
        print(f"Connections: {self._connections}")
        print(f"Profile Views: {self._profile_views}")