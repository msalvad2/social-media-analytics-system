#Miguel Salvador
"""
PyTest test suite for Binary Search Tree.
Tests insert, retrieve, display, and remove functionality.
"""
from social_media import SocialMedia
from tiktok import TikTok
from linkedin import LinkedIn
from instagram import Instagram

class Node:

    def __init__(self, data: "SocialMedia"):
        self._data = data
        self._left = None
        self._right = None

    def get_right(self):
       
       return self._right

    def get_left(self):

        return self._left

    def set_left(self, node):
        
        self._left = node

    def set_right(self, node):
        
        self._right = node

    def get_data(self):
        
        return self._data
    


class BST:

    def __init__(self):
        self._root = None
        

    def insert(self, data: "SocialMedia"):
        #list is empty
        if not isinstance(data, SocialMedia):
            raise TypeError("You must insert an object of type Social Media!")
        self._root = self._insert_recursively(self._root, data)

    def _insert_recursively(self, root: Node, data: "SocialMedia"):
        #you reach a leaf
        if(root is None):
            root = Node(data)
            return root
        
        #we do not allow dupliicate usernames
        if(root.get_data() == data):
            #you won't duplicate names so just return
            raise ValueError("Cannot enter Duplicates Usernames!")
        
        #Goes right
        elif(root.get_data() < data):

            root.set_right(self._insert_recursively(root.get_right(), data))
            
        #Goes left
        else:

            root.set_left(self._insert_recursively(root.get_left(), data))
            

        return root
            

    def retrieve(self, username: str):
        if not isinstance(username, str):
            raise TypeError("Must use a string to retrieve!")
        
        return self._retrieve_recursively(self._root, username)

    def _retrieve_recursively(self, root: Node, username: str):

        #means empty tree or Not Found
        if root is None:
            return None
        #if match is found we return the object
        if root.get_data()._username == username:
            return root.get_data()
        
        elif root.get_data()._username < username:
            result = self._retrieve_recursively(root.get_right(), username)

        else:
            result = self._retrieve_recursively(root.get_left(), username)
        
        return result


    def display(self):
        if self._root is None:
            return None
        
        else:
            self._display_recursively(self._root)
        
    def _display_recursively(self, root: Node):

        if root is None:
            return 
        
        #in order traversal
        self._display_recursively(root.get_left())
        print("--------------------------------------------")

        root.get_data().display()
        print("--------------------------------------------")

        self._display_recursively(root.get_right())



    def remove(self, username: str):

        if not isinstance(username, str):
            raise TypeError("Username must be a string type!")
        self._root = self._remove_recursively(self._root, username)

    
    def _remove_recursively(self, root: Node, username: str):
        
        if root is None:
            return
        
        if root.get_data()._username == username:
            
            #case 1: Node has no pointers
            if root.get_left() is None and root.get_right() is None :

                return None
            #case 2.a: Node has a left pointer and no right pointer
            elif root.get_left() is not None and root.get_right() is None :
                return root.get_left()
            #case 2.b: Node has no left pointer and it has a right pointer
            elif root.get_left() is None and root.get_right() is not None:
                return root.get_right()
            #case 3: Node has two pointers
            else:
                #this will return in order successor's data that will replace the nodes data that we are pointing to
                ios_data = self._IOS(root.get_right())
                #now you delete the node, you also need to update as you come back
                root.set_right(self._remove_recursively(root, ios_data._username))
                #update the current nodes data to IOS
                root._data = ios_data

                return root

                
        
        elif(root.get_data()._username < username):

            root.set_right(self._remove_recursively(root.get_right(), username))
        
        else:
            root.set_left(self._remove_recursively(root.get_left(), username))

        return root
    #function will return the In order successor: right subtree's smallest node
    def _IOS(self, root: Node):
        if root.get_left() is None:
            return root.get_data()
        
        return self._IOS(root.get_left())
    

#this class will be used to manage the social media analytics
class SocialMediaAnalytics:

    def __init__(self):
        #initialize the tree
        self._tree = BST()

    def run(self):

        print("WELCOME to the Social Media Analytics Tool!")
        print("------------------------------------------------")
        self._load_sample_data()
#display menu 
        
        while True:
            self._display_menu()
        
            #user response
            choice = input("Enter choice:")

            
            if choice == '1':
                self._add_instagram()
            elif choice == '2':
                self._add_tiktok()
            elif choice == '3':
                self._add_linkedin()
            elif choice == '4':
                self._search_profile()
            elif choice == '5':
                self._display_all_profiles()
            elif choice == '6':
                self._update_profile_stats()
            elif choice == '7':
                self._remove_profile()
            elif choice == '8':
                self._view_analytics()
            elif choice == '9':
                print("Thank you for using Social Media Analytics Tool!")
                print("------------------------------------------------")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 9.")



    def _load_sample_data(self):
        
        #asks the user if they want to load samples
        choice = input("Load sample profiles? (yes/no)").strip().lower()

        if choice == 'yes' or choice == 'y':
            print("Loading samples!")

            try:
                # Instagram profiles
                self._tree.insert(Instagram("fitness_mike", 5000, 120, 45, 3))
                self._tree.insert(Instagram("sarah_cook", 8200, 89, 30, 2))

                
                # TikTok profiles
                self._tree.insert(TikTok("dance_pro", 15000, 67, 450000, 120))
                self._tree.insert(TikTok("comedy_joe", 22000, 134, 890000, 340))
                
                # LinkedIn profiles
                self._tree.insert(LinkedIn("alex_techie", 2500, 45, 850, 3200))
                self._tree.insert(LinkedIn("emma_sales", 1800, 38, 620, 2100))

            except Exception as e:
                print("Error loading sample data")


    def _display_menu(self):
        print("--------------------------------------------")
        print("Main Menu:")
        print("1.Add Instagram Profile")
        print("2. Add TikTok Profile")
        print("3. Add LinkedIn Profile")
        print("4. Search for Profile")
        print("5. Display All Profiles")
        print("6. Update Profile Stats")
        print("7. Remove Profile")
        print("8. View Profile Analytics")
        print("9. Exit")
        print("--------------------------------------------")


    def _add_instagram(self):
        print("Add Instagram Profile: ")

        try:
            username = input("Username(8+ characters):")
            followers = int(input("Followers:"))
            posts = int(input("Posts:"))
            total_reels = int(input("Total Reels: "))
            stories_per_day = int(input("Stories Per Day:"))
            #create an object with the users input
            instagram_profile = Instagram(username, followers, posts, total_reels, stories_per_day)

            self._tree.insert(instagram_profile)
            print("Succesfully Added Account")

        except ValueError as e:
            print(f"Type Error: {e}")
        
        except TypeError as e:
            print(f"Type Error: {e}")
        #general exception handling
        except Exception as e:
            print(f"An error has occured: {e}")

    def _add_tiktok(self):
        print("Adding Tiktok profile: ")

        try:
            username = input("Username (8+ characters):")
            followers = int(input("Followers:"))
            posts = int(input("Posts:"))
            total_views = int(input("Total Views:"))
            total_reposts = int(input("Total Reposts:"))
            # Create the TikTok object
            tiktok_profile = TikTok(username, followers, posts, total_views, total_reposts)
            
            # Insert into tree
            self._tree.insert(tiktok_profile)
            print("Succesfully Added Account")


        except TypeError as e:
            print(f"Type Error: {e}")

        except ValueError as e:
            print(f"Value Error: {e}")

        except Exception as e:
            print(f"Error Occured: {e}")


    def _add_linkedin(self):

        print("ADD LINKEDIN PROFILE:")
        
        try:
            username = input("Username (8+ characters): ").strip()
            followers = int(input("Followers: "))
            posts = int(input("Posts: "))
            connections = int(input("Connections: "))
            profile_views = int(input("Monthly Profile Views: "))
            
            profile = LinkedIn(username, followers, posts, connections, profile_views)
            self._tree.insert(profile)
            print("Succesfully Added Account")


        except TypeError as e:
            print(f"Type Error: {e}")
        except ValueError as e:
            print(f"Value Error: {e}")
        except Exception as e:
            print(f"An Error has occured: {e}")


    def _search_profile(self):
        print("Searching Profile:")

        username = input("Username: ")
        #means profile was not found
        if not username:
            print("Username Cannot be empty!")
            return
        
        try:
            profile = self._tree.retrieve(username)
            #means profile was not found
            

            if profile is None:
                print("No Profile Found!")
            else:
                profile.display()
            
        except Exception as e:
            print(f"An Error has occured: {e}")

    def _display_all_profiles(self):
         
        try:
            if self._tree._root is None:
                print("Nothing to Display!")
            else:
                self._tree.display()
        except Exception as e:
            print(f"An Error has Occured: {e}")
    

    def _update_profile_stats(self):
        print("Updating Profile Stats")

        username = input("Enter Username:").strip()

        if not username:
            print("Username cannot be empty!")
            return
        try:
            #returns the user account
            profile = self._tree.retrieve(username)
            if profile is None:
                print("No Profile was found!")
                return
            print("Profile Information:")
            profile.display()
            print("--------------------------------------------")

            new_followers = int(input("New Followers: "))
            new_posts = int(input("New Posts:"))

            profile.update_stats(new_followers, new_posts)

            print("Stats Updated Succesfully!")

        except ValueError as e:
            print(f"Value Error: {e}")

        except TypeError as e:
            print(f"Type Error: {e}")

        except Exception as e:
            print(f"An Error has occured: {e}")


    def _remove_profile(self):
        print("Removing Profile!")
        
        username = input("Username!")
        if not username:
            print("Username cannot be empty!")
            return
        try:
            if self._tree is None:
                print("No Profiles!")
                return
            
            found = self._tree.retrieve(username) 
            if found is None:
                print("Profile was not found!")
                return
            
            
            
            self._tree.remove(username)
            #now we check to see if removal was succesful
            if self._tree.retrieve(username) is None:
                print("Username deleted succesfully")
            

        except TypeError as e:
            print(f"Type Error: {e}")

        except Exception as e:
            print(f"An error has occured: {e}")

    def _view_analytics(self):
        print("Viewing Profile Analytics")

        username = input("Username: ")

        #empty string
        if not username:
            print("Username cannot be empty")
            return
        try:
            profile = self._tree.retrieve(username)

            if profile is None:
                print("Username Not Found!")
                return
            print("Profile Information")
            profile.display()

            #if it is an instagram account
            if isinstance(profile, Instagram):
                print("Instagram Account:")
                #gets story activities
                activity = profile.story_activity()
                print(f"Story Activity: {activity}")

                #Engagement activites
                if len(profile._engagement_ratios) > 0:
                    average = profile.average_engagement_ratio()
                    print(f"Average Engagement Ratio History: {average}")
                else:
                    print("No Engagement History!")

                option = input("Calculate Engagement Score(yes or no):").strip().lower()
                #display score based on likes/comments  and current followers
                if option == 'yes' or option == 'y':
                    likes = int(input("Enter likes: "))
                    comments = int(input("Enter comments: "))
                    score = profile.engagement(likes, comments)
                    print(f"Engagement Score: {score:.2f}")

                #calculates average likes per post
                option2 = input("Calculate average likes per post?")
                if option2 == 'yes' or option2 == 'y':
                    likes = int(input("Enter total likes: "))
                    average_likes_post = profile.average_like_per_post(likes)
                    print(f"Average likes per post: {average_likes_post:.2f}")
            #if it is a TikTok Account
            elif isinstance(profile, TikTok):
                print("TikTok Account: ")

                rate = profile.repost_rate()
                print(f"Repost Rate: {rate:.2f}")
            # Checks if video is viral
                check_viral = input("\nCheck if latest video is viral? (yes/no): ").strip().lower()
                if check_viral == 'yes' or check_viral == 'y':
                    views = int(input("Enter latest video views: "))
                    is_viral = profile.is_viral(views)
                    if is_viral:
                        print("Video is VIRAL!")
                    else:
                        print("Video is not viral (needs 10x followers in views)")
                # Calculate engagement
                option = input("\nCalculate engagement? (yes/no): ").strip().lower()
                if option == 'yes' or option == 'y':
                    likes = int(input("Enter likes: "))
                    comments = int(input("Enter comments: "))
                    shares = int(input("Enter shares: "))
                    score = profile.engagement(likes, comments, shares)
                    print(f"Engagement Score: {score:.2f}")

            elif isinstance(profile, LinkedIn):
                print("LinkedIn Account: ")
                #calculates views recieved within last 30 days
                rate = profile.profile_view_rate()
                print(f"Daily Profile View Rate: {rate:.2f}")
                #calculates acceptance rate
                calc_rate = input("\nCalculate connection acceptance rate? (yes/no): ").strip().lower()
                if calc_rate == 'yes' or calc_rate == 'y':
                    requests = int(input("Enter pending connection requests: "))
                    rate = profile.connection_acceptance_rate(requests)
                    print(f"Connection Acceptance Rate: {rate:.2f}%")

                 #calculates the network level activites
                check_level = input("\nCheck network activity level? (yes/no): ").strip().lower()
                if check_level == 'yes' or check_level == 'y':
                    messages = int(input("Enter messages sent this month: "))
                    level = profile.network_level(messages)
                    print(f"Network Activity Level: {level}")
        except ValueError as e:
            print(f" Validation Error: {e}")
        except Exception as e:
            print(f" Error: {e}")

