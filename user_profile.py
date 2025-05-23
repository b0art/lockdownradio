from typing import List

class UserProfile:
    user_id: str
    first_name: str
    age: int
    bio: str
    interests: List[str]
    photo_urls: List[str]

    def __init__(self, user_id: str, first_name: str, age: int, bio: str, interests: List[str], photo_urls: List[str]):
        self.user_id = user_id
        self.first_name = first_name
        self.age = age
        self.bio = bio
        self.interests = interests
        self.photo_urls = photo_urls

if __name__ == "__main__":
    # Create an instance of UserProfile
    user_profile = UserProfile(
        user_id="user123",
        first_name="Alice",
        age=28,
        bio="Software engineer and avid hiker.",
        interests=["hiking", "photography", "reading", "traveling"],
        photo_urls=["http://example.com/photo1.jpg", "http://example.com/photo2.png"]
    )

    # Print each attribute
    print(f"User ID: {user_profile.user_id}")
    print(f"Name: {user_profile.first_name}")
    print(f"Age: {user_profile.age}")
    print(f"Bio: {user_profile.bio}")
    print(f"Interests: {user_profile.interests}")
    print(f"Photo URLs: {user_profile.photo_urls}")
