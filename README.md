# Installation Guide
The project is compatible with Python 3.10

1. Install Django
```
sudo apt install python3-django
```
2. Create virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```
3. In the "backend" directory, install the dependencies
```
cd backend
pip install -r requirements.txt
```

4. To run the project, run the following command

```
python3 manage.py runserver
```
With this, the backend will start running on port 8000.

5. Now go to the Frontend directory and run file index.htm
