SQLALCHEMY_DATABASE_URI='sqlite:///database.db'

ADMIN_USERNAME='admin'
ADMIN_PASSWORD='1234'
SECRET_KEY='dafghf5rtred52325erfdvc235df1@$&dw8defdgf'
PAYMENT_MERCHANT='sandbox'
PAYMENT_CALLBACK='http://localhost:5000/verify'
PAYMENT_FIRST_REQUEST_URL='https://sandbox.shepa.com/api/v1/token'
PAYMENT_VERIFY_REQUEST_URL = 'https://sandbox.shepa.com/api/v1/verify'
