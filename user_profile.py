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

def are_ages_compatible(profile1: 'UserProfile', profile2: 'UserProfile', max_age_difference: int) -> bool:
    """
    Checks if the age difference between two user profiles is within a specified limit.
    """
    age_diff = abs(profile1.age - profile2.age)
    return age_diff <= max_age_difference

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

    # --- Age Compatibility Test ---
    print("\n--- Age Compatibility Test ---")
    sample_max_age_difference = 5

    # Create User Profiles for testing age compatibility
    profile_age_test1 = UserProfile(
        user_id="age_test_user1",
        first_name="AgeTest1",
        age=30,
        bio="Bio for AgeTest1",
        interests=["cinema", "board games"],
        photo_urls=[]
    )

    profile_age_test2_compatible = UserProfile(
        user_id="age_test_user2_compatible",
        first_name="AgeTest2Compatible",
        age=33,
        bio="Bio for AgeTest2Compatible",
        interests=["reading"],
        photo_urls=[]
    )

    profile_age_test3_incompatible = UserProfile(
        user_id="age_test_user3_incompatible",
        first_name="AgeTest3Incompatible",
        age=40,
        bio="Bio for AgeTest3Incompatible",
        interests=["gardening"],
        photo_urls=[]
    )

    # Test are_ages_compatible function
    compatible_result = are_ages_compatible(profile_age_test1, profile_age_test2_compatible, sample_max_age_difference)
    incompatible_result = are_ages_compatible(profile_age_test1, profile_age_test3_incompatible, sample_max_age_difference)

    # Print results clearly
    print(f"Profile X ({profile_age_test1.user_id}) Age: {profile_age_test1.age}")
    print(f"Profile Y ({profile_age_test2_compatible.user_id}) Age: {profile_age_test2_compatible.age}")
    print(f"Max Allowed Age Difference: {sample_max_age_difference}")
    print(f"Are Profile X and Y ages compatible? -> {compatible_result}")

    print(f"\nProfile X ({profile_age_test1.user_id}) Age: {profile_age_test1.age}")
    print(f"Profile Z ({profile_age_test3_incompatible.user_id}) Age: {profile_age_test3_incompatible.age}")
    print(f"Max Allowed Age Difference: {sample_max_age_difference}")
    print(f"Are Profile X and Z ages compatible? -> {incompatible_result}")
