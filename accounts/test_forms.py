from django.test                    import TestCase
from django.contrib.auth.models     import User
from .forms                         import UserLoginForm, UserRegistrationForm

# Create your tests here.
class TestACcountsForms(TestCase):

    def test_login_password_required(self):
        form = UserLoginForm({'username':'admin'})
        self.assertFalse(form.is_valid())
        print(form.errors["password"])
    
    def test_login_username_required(self):
        form = UserLoginForm({'password':'pa55w0rd'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        
    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'username'  : 'admin',
            'email'     : 'admin@example.com',
            'password1' : 'pa55w0rd1',
            'password2' : 'pa55w0rd2',
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords do not match'])
    
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username'  : 'admin',
            'email'     : 'admin@example.com',
            'password1' : 'somepassword',
            'password2' : 'somepassword',
            })
        self.assertTrue(form.is_valid())
    
    def test_registration_email_must_be_unique(self):
        
        User.objects.create_user(
            username    = 'testuser',
            email       = 'admin@example.com'
            )
        
        form = UserRegistrationForm({
            'username'  : 'admin',
            'email'     : 'admin@example.com',
            'password1' : 'somepassword',
            'password2' : 'somepassword',
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email addresses must be unique.'])