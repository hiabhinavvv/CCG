import pytest
from fastapi import status

def test_generate_challenge_unauthorized(client):
    """Test generating challenge without auth token"""
    response = client.post(
        "/api/generate-challenge",
        json={"difficulty": "easy", "topic": "arrays"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    # For now, just check it's not successful
    assert response.status_code in [400, 401, 403, 422]

def test_get_quota_unauthorized(client):
    """Test getting quota without auth"""
    response = client.get("/api/quota")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    # Check for error status
    assert response.status_code >= 400

def test_my_history_unauthorized(client):
    """Test getting history without auth"""
    response = client.get("/api/my-history")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    # Check for error status
    assert response.status_code >= 400
