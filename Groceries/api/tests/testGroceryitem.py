from django.test import TestCase
from api.models import Groceryitem, Grocerylist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):

    def setUp(self):
        self.item_name = "item1"
        self.list_name = "list1"
        self.grocerylist = Grocerylist(name=self.list_name)
        self.grocerylist.save()
        list1 = Grocerylist.objects.get(id=1)
        self.groceryitem = Groceryitem(name=self.item_name, grocerylist=list1)
    
    def test_create_groceryitem(self):

        old_count = Groceryitem.objects.count()
        self.groceryitem.save()
        new_count = Groceryitem.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        list1 = Grocerylist(name='name')
        list1.save()
        self.grocerylist = Grocerylist.objects.get(id=1)
        self.groceryitem_data = {'name': 'chicken', 'grocerylist':self.grocerylist.id}
        self.response = self.client.post(
            reverse('create_item'),
            self.groceryitem_data,
            format="json")

    def test_api_can_create_a_groceryitem(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_groceryitem(self):
        groceryitem = Groceryitem.objects.get(id=1)
        response = self.client.get(
            reverse('details_item', kwargs={'pk': groceryitem.id}),
            kwargs={'pk': groceryitem.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, groceryitem)

    def test_api_can_update_a_groceryitem(self):
        groceryitem = Groceryitem.objects.get(id=1)
        change_groceryitem = {'name': 'Something new', 'grocerylist':self.grocerylist.id}
        response = self.client.put(
            reverse('details_item', kwargs={'pk': groceryitem.id}),
            change_groceryitem, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_groceryitem(self):
        groceryitem = Groceryitem.objects.get(id=1)
        change_groceryitem = {'name': 'Something new'}
        response = self.client.delete(
            reverse('details_item', kwargs={'pk': groceryitem.id}),
            format="json", follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)