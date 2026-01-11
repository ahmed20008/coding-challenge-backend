import httpx
import os
from config import settings

def get_github_profile_image(github_username: str) -> str:
    """Fetch GitHub profile image and save locally"""
    try:
        url = f"https://api.github.com/users/{github_username}"
        headers = {}
        
        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"token {settings.GITHUB_TOKEN}"
        
        with httpx.Client() as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            avatar_url = data.get("avatar_url")
            
            if avatar_url:
                img_response = client.get(avatar_url)
                img_response.raise_for_status()
                
                os.makedirs("temp_images", exist_ok=True)
                image_path = f"temp_images/{github_username}.png"
                
                with open(image_path, "wb") as f:
                    f.write(img_response.content)
                
                return image_path
        
        return None
    except Exception as e:
        print(f"Error fetching GitHub profile image: {e}")
        return None
