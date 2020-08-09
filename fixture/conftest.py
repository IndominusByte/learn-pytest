import pytest
import smtplib

# Parametrizing fixtures
@pytest.fixture(scope="module",params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection  # provide the fixture value
    print(" finalizing {}".format(smtp_connection))
    print(" teardown smtp")
    smtp_connection.close()
