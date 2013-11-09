sudo apt-get install python-pip python-dev build-essential 
sudo apt-get install git
sudo apt-get install nginx

sudo apt-get install fish
sudo chsh -s (which fish)

sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

sudo pip install tornado
sudo pip install nltk
sudo pip install supervisor 

rm /etc/nginx/nginx.conf
ln -s ~/moji.fi/server-setup/tornado-ec2/conf/nginx.conf /etc/nginx/nginx.conf 
ln -s ~/moji.fi/server-setup/tornado-ec2/conf/supervisord.conf /etc/supervisord.conf 

adduser --system --no-create-home --disabled-login --disabled-password --group nginx 
mkdir ~/logs 

# mkdir moji.fi
# git clone https://github.com/OmerShapira/Mojifi moji.fi	