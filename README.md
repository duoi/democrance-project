# democrance

1. Install the dependencies (`pip install -r requirements.txt`)
2. Migrate the database (`python3 manage.py migrate`)
3. Populate the dummy data for the policy types (`python3 manage.py populate_types`)
4. Create some admin user to access the admin panel (`python3 manage.py createsuperuser`)

Notes:

You need to pass in a user PK as part of your POST data to create a policy to be able to bind the policy to a particular user.
