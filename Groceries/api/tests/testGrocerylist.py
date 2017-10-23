from django.test import TestCase
from api.models import Grocerylist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):

    def setUp(self):
        self.list_name = "my list name"
        self.grocerylist = Grocerylist(name=self.list_name)

    def test_create_grocerylist(self):
        old_count = Grocerylist.objects.count()
        self.grocerylist.save()
        new_count = Grocerylist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.grocerylist_data = {'name': 'Andrew\'s List'}
        self.response = self.client.post(
            reverse('create_list'),
            self.grocerylist_data,
            format="json")

    def test_api_can_create_a_grocerylist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_grocerylist(self):
        grocerylist = Grocerylist.objects.get(id=1)
        response = self.client.get(
            reverse('details_list', kwargs={'pk': grocerylist.id}),
            kwargs={'pk': grocerylist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, grocerylist)

    def test_api_can_update_grocerylist(self):
        grocerylist = Grocerylist.objects.get(id=1)
        change_grocerylist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details_list', kwargs={'pk': grocerylist.id}),
            change_grocerylist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_grocerylist(self):
        grocerylist = Grocerylist.objects.get(id=1)
        response = self.client.delete(
            reverse('details_list', kwargs={'pk': grocerylist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
