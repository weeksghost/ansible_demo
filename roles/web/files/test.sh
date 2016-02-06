export DISPLAY=:99

cd pytest && python setup.py install && cd ..

py.test --driver=chrome --baseurl='http://reddit.com'  pytest/tests.py
