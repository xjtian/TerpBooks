sudo apt-get update
sudo apt-get install -y apache2 python-dev git vim curl dos2unix make libapache2-mod-wsgi
sudo DEBIAN_FRONTEND=noninteractive apt-get install -q -y mysql-server
sudo apt-get install -y libmysqlclient-dev

cd /home/vagrant
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.tar.gz
tar xvzf virtualenv-1.11.tar.gz
cd virtualenv-1.11/
sudo python setup.py install

cd /home/vagrant
sudo rm -rf virtualenv-1.11/
rm virtualenv-1.11.tar.gz

mkdir venvs/
cd venvs/
virtualenv books
sudo chown vagrant:vagrant books/ -R

cd /vagrant
source /home/vagrant/venvs/books/bin/activate
pip install -r requirements.txt
mkdir -p /home/vagrant/www/public/ /home/vagrant/www/logs
sudo chown vagrant:vagrant /home/vagrant/www/ -R

cd /vagrant
#sudo cp httpd.conf /etc/apache2/httpd.conf

mysql -u root -e"create database terpbooks;"
#mysql -u root terpbooks < init_data.sql

sudo service apache2 restart
