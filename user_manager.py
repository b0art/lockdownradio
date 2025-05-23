from typing import List
from user_profile import UserProfile

class UserManager:
    def __init__(self):
        self.users: List[UserProfile] = []

    def add_user(self, user: UserProfile):
        self.users.append(user)

    def get_all_users(self) -> List[UserProfile]:
        return self.users

if __name__ == "__main__":
    # Create UserManager instance
    manager = UserManager()

    # Create UserProfile instances
    profile1 = UserProfile(
        user_id="user001",
        first_name="Alice",
        age=30,
        bio="Loves hiking and books.",
        interests=["hiking", "reading"],
        photo_urls=["photo_alice.jpg"]
    )
    profile2 = UserProfile(
        user_id="user002",
        first_name="Bob",
        age=28,
        bio="Enjoys coding and cooking.",
        interests=["coding", "cooking", "music"],
        photo_urls=["photo_bob.jpg"]
    )
    profile3 = UserProfile(
        user_id="user003",
        first_name="Charlie",
        age=35,
        bio="Passionate about photography and travel.",
        interests=["photography", "travel", "art"],
        photo_urls=["photo_charlie.jpg", "photo_charlie_travel.jpg"]
    )

    # Add users to the manager
    manager.add_user(profile1)
    manager.add_user(profile2)
    manager.add_user(profile3)

    # Retrieve and print user information
    all_profiles = manager.get_all_users()
    print("\n--- All Users in Manager ---")
    for profile in all_profiles:
        print(f"Name: {profile.first_name}, Age: {profile.age}, Interests: {profile.interests}, Bio: {profile.bio}, Photos: {profile.photo_urls}")
