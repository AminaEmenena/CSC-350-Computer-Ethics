import matplotlib.pyplot as plt
import csv

def fetch_data_with_consent(user_profiles):
    return [profile for profile in user_profiles if profile['consent_given']]

def anonymize_data(data):
    return [{'interests': profile['interests']} for profile in data]

def analyze_data(data):
    interests_count = {}
    for profile in data:
        for interest in profile['interests']:
            if interest in interests_count:
                interests_count[interest] += 1
            else:
                interests_count[interest] = 1
    return interests_count

def plot_interests(interests_count):
    interests = list(interests_count.keys())
    counts = list(interests_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(interests, counts, color='skyblue')
    plt.xlabel('Interests')
    plt.ylabel('Count')
    plt.title('Most Common Interests Among Users')
    plt.xticks(rotation=45)
    plt.show()

def read_user_profiles(filename):
    user_profiles = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Ensure v is a string before calling strip(), replace None with an empty string
            row = {k: v.strip() if v is not None else '' for k, v in row.items()}
            row['interests'] = row['interests'].split('|') if row['interests'] else []
            row['consent_given'] = row['consent_given'].upper() == 'TRUE' if row['consent_given'] else False
            user_profiles.append(row)
    return user_profiles

"""def main(filename):
    user_profiles = read_user_profiles(filename)
    data_with_consent = fetch_data_with_consent(user_profiles)
    anonymized_data = anonymize_data(data_with_consent)
    analysis_results = analyze_data(anonymized_data)
    plot_interests(analysis_results)

    print("Most Common Interests Among Users (Anonymized Data):")
    for interest, count in analysis_results.items():
        print(f"{interest}: {count}")"""

def main(filename):
    # Read user profiles from the CSV file
    user_profiles = read_user_profiles(filename)
    print("Read User Profiles:")
    for profile in user_profiles:
        print(profile)
    print("\n")

    # Fetch data for users who have given consent
    data_with_consent = fetch_data_with_consent(user_profiles)
    print("Data with Consent:")
    for profile in data_with_consent:
        print(profile)
    print("\n")

    # Anonymize the data
    anonymized_data = anonymize_data(data_with_consent)
    print("Anonymized Data:")
    for profile in anonymized_data:
        print(profile)
    print("\n")


if __name__ == "__main__":
    filename = "/workspaces/CSC-350-Computer-Ethics/user_profiles.csv"  # Adjust as needed
    main(filename)