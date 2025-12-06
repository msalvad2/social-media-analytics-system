#Miguel Salvador
"""
Social Media Analytics Tool - Main application with menu interface.
Provides menu-driven access to BST operations and analytics features.
"""
from social_media import SocialMedia
from  instagram import Instagram
from tiktok import TikTok
from linkedin import LinkedIn
from bst import SocialMediaAnalytics


def main():

   app = SocialMediaAnalytics()
   app.run()


if __name__ == "__main__":
   main()