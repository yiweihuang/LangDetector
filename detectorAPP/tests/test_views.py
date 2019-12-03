import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import DetectorAppSerializer


# initialize the APIClient app
client = Client()

class CreateNewDetectorTest(TestCase):
    """ Test module for inserting a new detector """

    def setUp(self):
        self.valid_payload = {
            'sentence': "Tous mes meilleurs voeux pour l'année 2020!",
        }
        self.invalid_payload = {
            'sentence': '',
        }

    def test_create_valid_detector(self):
        response = client.post(
            reverse('detectorAPP:detector-app-lang'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_detector(self):
        response = client.post(
            reverse('detectorAPP:detector-app-lang'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
