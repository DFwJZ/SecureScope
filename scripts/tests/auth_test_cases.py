"""Test cases for authentication vulnerabilities"""
import requests

def test_weak_passwords():
    """Test for common weak passwords"""
    target_url = "http://localhost:5000/login"
    common_passwords = ["admin", "password", "123456", "qwerty"]
    
    for password in common_passwords:
        response = requests.post(target_url, 
            json={"username": "admin", "password": password})
        print(f"Testing {password}: {response.status_code}")

def test_username_enumeration():
    """Test for username enumeration via response timing"""
    target_url = "http://localhost:5000/login"
    usernames = ["admin", "root", "user", "test"]
    
    for username in usernames:
        response = requests.post(target_url, 
            json={"username": username, "password": "anything"})
        print(f"Username: {username}, Time: {response.elapsed.total_seconds()}")

# idor_test_cases.py
def test_horizontal_access():
    """Test for horizontal privilege escalation"""
    base_url = "http://localhost:5000/user/"
    session = requests.Session()
    # Login as user1
    session.post("http://localhost:5000/login", 
        json={"username": "user1", "password": "password1"})
    
    # Try accessing other users
    for user_id in range(1, 10):
        response = session.get(f"{base_url}{user_id}")
        print(f"Accessing user {user_id}: {response.status_code}")