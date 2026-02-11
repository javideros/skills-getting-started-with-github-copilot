"""
Pytest configuration and fixtures for tests
"""

import pytest
from copy import deepcopy
import src.app

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and games",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn tennis skills and participate in friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["sophia@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu"]
    },
    "Music Band": {
        "description": "Join the school band and perform at events",
        "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop argumentation and public speaking skills",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["lucas@mergington.edu"]
    },
    "Science Club": {
        "description": "Explore physics, chemistry, and biology through experiments",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 22,
        "participants": ["mia@mergington.edu", "ethan@mergington.edu"]
    }
}


@pytest.fixture(autouse=True)
def reset_app_state():
    """Reset app state before each test"""
    # Reset the module-level activities variable in src.app
    src.app.activities = deepcopy(INITIAL_ACTIVITIES)
    yield


