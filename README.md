TerpBooks
=========

TerpBooks is a textbook exchange website developed for UMD students as a capstone project for the Design, Cultures and Creativity honors program. Authentication is done through the UMD Central Authentication System (CAS), so users are limited to UMD students. Additionally, the app doesn't handle payment details, so users can buy, sell, trade, or barter without having to surrender any cut of the selling price.

Contributing (Installation)
---------------------------

Install [https://www.virtualbox.org](VirtualBox) and [http://www.vagrantup.com](Vagrant), and in a terminal prompt at the repository root,

```sh
$ vagrant up
```

This will provision the development VM for the project. To run the Django test server,

```sh
$ vagrant ssh
vagrant@geo:~$ source venvs/books/bin/activate
(books)vagrant@geo:~$ cd /vagrant/terpbooks
(books)vagrant@geo:/vagrant/terpbooks$ make runserver
```

Open up a browser on your host machine and go to http://localhost:8001 to see the app.
