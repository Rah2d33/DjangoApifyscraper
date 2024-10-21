import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# Step 1: Scraping Instagram Profile Using BeautifulSoup
def scrape_instagram_profile(username):
    # URL encode the username to handle special characters
    encoded_username = quote(username)
    url = f"https://www.instagram.com/{encoded_username}/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to retrieve Instagram profile. {str(e)}"}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract display name from the meta tag with property 'og:title'
    title_tag = soup.find('meta', attrs={'property': 'og:title'})
    display_name = title_tag['content'].split('(')[0].strip() if title_tag else 'No display name found'

    # Extract bio content
    bio_description = None

    # Try to locate bio content in the <div> with class '-vDIg'
    bio_div = soup.find('div', attrs={'class': '-vDIg'})
    if bio_div:
        bio_span = bio_div.find('span')
        if bio_span:
            bio_text = bio_span.text
            
            # Check for bullet points (•) and split to avoid follower/following counts
            bio_parts = bio_text.split('•')
            bio_description = bio_parts[0].strip() if bio_parts else 'No bio found'

    # If bio is still not found, check the alternative meta description
    if not bio_description or bio_description == 'No bio found':
        alternative_bio = soup.find('meta', attrs={'name': 'description'})
        if alternative_bio:
            content = alternative_bio.get('content', '')
            bio_parts = content.split('•')
            bio_description = bio_parts[0].strip() if bio_parts else 'No bio found'

    return {
        'username': f"@{username}",  # Prefixing username with @
        'display_name': display_name,
        'bio': bio_description if bio_description else 'No bio found',  # Now called 'bio'
        'profile_url': url
    }

# Step 3: Merging Scraped Data with Instagram Graph API Data
def get_combined_instagram_data(username):
    # Scrape basic profile details
    scraped_data = scrape_instagram_profile(username)

    # Combine both sets of data
    combined_data = {
        'scraped_data': scraped_data,
    }

    return combined_data

# Step 4: Example Usage
if __name__ == "__main__":
    username = input("Enter the Instagram username to search: ").strip()
    combined_data = get_combined_instagram_data(username)

    # Output the combined data
    if combined_data:
        scraped_data = combined_data['scraped_data']
        print("Scraped Data:")
        print(f"Username: {scraped_data.get('username')}")  # Username will now show as @username
        print(f"Display Name: {scraped_data.get('display_name')}")
        print(f"Bio: {scraped_data.get('bio')}")  # Now called 'bio' instead of 'bio_description'
        print(f"Profile URL: {scraped_data.get('profile_url')}\n")
    else:
        print("No data found or an error occurred.")

