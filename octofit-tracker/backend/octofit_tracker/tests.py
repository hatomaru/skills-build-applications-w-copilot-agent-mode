from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctofitTrackerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password')

    def test_user_creation(self):
        response = self.client.post('/api/users/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_creation(self):
        response = self.client.post('/api/teams/', {
            'name': 'Test Team',
            'members': [self.user.id]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_activity_creation(self):
        response = self.client.post('/api/activities/', {
            'user': self.user.id,
            'activity_type': 'Running',
            'duration': '01:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_leaderboard_creation(self):
        response = self.client.post('/api/leaderboard/', {
            'user': self.user.id,
            'score': 100
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_workout_creation(self):
        response = self.client.post('/api/workouts/', {
            'name': 'Test Workout',
            'description': 'This is a test workout.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
