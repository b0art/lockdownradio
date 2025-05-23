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

def have_shared_interest(profile1: 'UserProfile', profile2: 'UserProfile') -> bool:
    """
    Checks if two user profiles have at least one common interest.
    """
    for interest1 in profile1.interests:
        if interest1 in profile2.interests:
            return True
    return False

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

    # --- Shared Interest Test ---
    print("\n--- Shared Interest Test ---")

    # Create User Profiles for testing shared interests
    profile1 = UserProfile(
        user_id="user1_interests",
        first_name="TestUser1",
        age=30,
        bio="Bio for TestUser1",
        interests=["coding", "music", "hiking"],
        photo_urls=[]
    )

    profile2_match = UserProfile(
        user_id="user2_match",
        first_name="TestUser2Match",
        age=32,
        bio="Bio for TestUser2Match",
        interests=["traveling", "music", "food"],
        photo_urls=[]
    )

    profile3_no_match = UserProfile(
        user_id="user3_no_match",
        first_name="TestUser3NoMatch",
        age=25,
        bio="Bio for TestUser3NoMatch",
        interests=["sports", "movies", "art"],
        photo_urls=[]
    )

    # Test have_shared_interest function
    shared_match_result = have_shared_interest(profile1, profile2_match)
    shared_no_match_result = have_shared_interest(profile1, profile3_no_match)

    # Print results clearly
    print(f"Profile A ({profile1.user_id}) Interests: {profile1.interests}")
    print(f"Profile B ({profile2_match.user_id}) Interests: {profile2_match.interests}")
    print(f"Do Profile A and Profile B share an interest? -> {shared_match_result}")

    print(f"\nProfile A ({profile1.user_id}) Interests: {profile1.interests}")
    print(f"Profile C ({profile3_no_match.user_id}) Interests: {profile3_no_match.interests}")
    print(f"Do Profile A and Profile C share an interest? -> {shared_no_match_result}")
