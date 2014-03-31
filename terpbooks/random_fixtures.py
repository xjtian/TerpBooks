import os

import itertools
import random
import string

from django.contrib.auth.models import User

from books.models import Textbook, Author, Semester, Professor
from transactions.models import Listing, TransactionRequest, TransactionRequestThread

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terpbooks.settings.staging')

# Set up data
first_names = ['Bob ', 'John ', 'Jane ', 'Sally ']
last_names = ['Doe', 'Grant', 'Gray', 'Brown']
author_names = map(lambda l: ''.join(l), itertools.product(first_names, last_names))

years = [2011, 2012, 2013, 2014]
semester_names = ['CFL', 'DWN', 'ASP', 'BSM']
semesters = itertools.product(semester_names, years)

class_subjects = ['CMSC', 'PHYS', 'MATH', 'ENGL']
class_numbers = ['101', '201', '301', '401']

class_codes = map(lambda l: ''.join(l), itertools.product(class_subjects, class_numbers))

isbns = [''.join(random.choice(string.digits) for i in xrange(0, 13)) for j in xrange(0, 16)]

title_prefixes = ['A History of ', 'General Background of ', "Beginner's Guide to ", 'Become an Expert in ']
title_suffixes = ['Physics', 'Technical Writing', 'Calculus', 'Algorithms']
titles = map(lambda l: ''.join(l), itertools.product(title_prefixes, title_suffixes))

professors = map(lambda s: Professor.objects.create(first_name=s.split()[0], last_name=s.split()[1]), author_names)
semesters = map(lambda x: Semester.objects.create(year=x[1], semester=x[0]), semesters)

u1 = User.objects.create_user('user1', password='Password1')
u2 = User.objects.create_user('user2', password='Password1')

users = [u1, u2]

for i in xrange(0, 16):
    b = Textbook.objects.create(title=titles[i], edition=random.randint(1, 3), isbn=isbns[i], course_code=class_codes[i], semester=semesters[i], professor=professors[i])
    num_authors = random.randint(1, 3)
    k = 0
    for _ in xrange(0, num_authors):
        f, l = author_names[k % 16].split()
        Author.objects.create(first_name=f, last_name=l, book=b)
        k += 1

    # Create a listing for this book
    status = random.choice(['AV', 'PN', 'SD'])
    asking_price = int(100 * (random.random() * 10.0) + 5.0) / 100.0

    owner = users[i % 2]
    comments = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

    l = Listing.objects.create(status=status, asking_price=asking_price,
                               owner=owner, book=b, comments=comments)

    # Create a transaction request for the listing
    sender = users[int(not i % 2)]
    thread = TransactionRequestThread.objects.create(sender=sender, listing=l)

    # Create some requests in the thread
    num_requests = random.randint(1, 4)
    for j in xrange(0, num_requests):
        created_by = users[(i % 2 + j + 1) % 2]
        price = int(100 * random.uniform(0.0, asking_price)) / 100.0

        text = 'Sed elementum est eget nibh venenatis vestibulum.'

        TransactionRequest.objects.create(created_by=created_by, price=price,
                                          text=text, thread=thread)
