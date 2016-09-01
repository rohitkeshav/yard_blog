This is a simple blog with REST API endpoints. Currently only backend has been created.

Clone the project using  - git clone https://github.com/rohittk/yard_blog.git


##### To run project on your system- 
  1. **Create virtual environment** - 
      virtualenv *virtual_environment_name*
  2. **Activate using** - 
      source *virtual_environment_name*/bin/activate
  3. **Enter project directory**
  4. **Install requirements** - 
      pip install requirements.txt
  5. **Create Superuser** - 
      python manage.py createsuperuser


To access the API endpoints use the urls below - 
* blogs - localhost/api/v1/blog_endpoint/
* comments - localhost/api/v1/comment_endpoint/
* users - localhost/api/v1/user_endpoint/

To access admin panel - localhost/admin

Future commits to include frontend using AngularJS to handle our REST API.
