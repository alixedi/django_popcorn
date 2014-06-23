from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Very important - sexy css selectors to test template output
# All we have here is templaets so this was a life-saver!
# Please star: https://github.com/johnpaulett/django-with-asserts
from with_asserts.case import TestCase

from bookstore.models import Publisher, Author, Book


class PopcornTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_superuser('admin', 'admin@popcorn.com', 'admin')

    def test_books_no_login(self):
        """
        Test the Book create view. We should not get 'add another' links 
        until we login as admin of course.
        """
        response = self.client.get(reverse("bookstore_book_create"))
        self.assertEqual(response.status_code, 200)

        # so the number of links should be 1 - cancel
        with self.assertHTML(response, 'a') as adds:
            self.assertEqual(1, len(adds))


    def test_books_login(self):
        """
        Test the book create view after logging in. We should now get three
        links in the HTML - one for cancel and 2 for add-anothers
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse("bookstore_book_create"))
        self.assertEqual(response.status_code, 200)

        # so the number of links should be 3 - cancel and 2 add-anothers
        with self.assertHTML(response, 'a') as adds:
            self.assertEqual(3, len(adds))

    def test_add_author(self):
        """
        Test the author create PopcornView. Submitting a valid form should
        result in an Author being added to the DB.
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse("bookstore_author_popcorn"))
        self.assertEqual(response.status_code, 200)

        # add an author and check if it gets added
        form_data = {'first_name': 'Robert',
                     'last_name': 'Lafore',
                     'email': 'robert@lafore.com'}
        response = self.client.post(reverse("bookstore_author_popcorn"), form_data)
        self.assertEqual(response.status_code, 200)

        # author should be in select box
        response = self.client.get(reverse("bookstore_book_create"))
        self.assertEqual(response.status_code, 200)
        with self.assertHTML(response, '#id_authors > option') as option:
            self.assertEqual(1, len(option))
            self.assertEqual("Robert Lafore", option[0].text)

    def test_add_publisher(self):
        """
        Test the publisher create PopcornView. Submitting a valid form should
        result in an Publisher being added to the DB.
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse("bookstore_publisher_popcorn"))
        self.assertEqual(response.status_code, 200)

        # add an publisher and check if it gets added
        form_data = {'name': 'Penguin',
                     'address': 'ABC',
                     'city': 'NY',
                     'state_province': 'NY/NJ',
                     'country': 'USA',
                     'website': 'www.penguin.com'}
        response = self.client.post(reverse("bookstore_publisher_popcorn"), form_data)
        self.assertEqual(response.status_code, 200)

        # publisher should be in select box
        response = self.client.get(reverse("bookstore_book_create"))
        self.assertEqual(response.status_code, 200)
        with self.assertHTML(response, '#id_publisher > option') as option:
            self.assertEqual(2, len(option))
            self.assertEqual("Penguin", option[1].text)
