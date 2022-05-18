import pytz
from account.hooks import AccountDefaultHookSet
from account.callbacks import account_delete_mark, account_delete_expunge
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_LOGIN_URL = "account_login"
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
ACCOUNT_LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "account:account_password"
ACCOUNT_PASSWORD_RESET_REDIRECT_URL = "account:account_login"
ACCOUNT_PASSWORD_EXPIRY = 0
ACCOUNT_PASSWORD_USE_HISTORY = False
ACCOUNT_REMEMBER_ME_EXPIRY = 60 * 60 * 24 * 365 * 10
ACCOUNT_USER_DISPLAY = lambda user: user.username
ACCOUNT_CREATE_ON_SAVE = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account:account_login"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_URL = "account:account_confirm_email"
ACCOUNT_SETTINGS_REDIRECT_URL = "account:account_settings"
ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE = True
ACCOUNT_DELETION_MARK_CALLBACK = account_delete_mark
ACCOUNT_DELETION_EXPUNGE_CALLBACK = account_delete_expunge
ACCOUNT_DELETION_EXPUNGE_HOURS = 48
ACCOUNT_HOOKSET = AccountDefaultHookSet
ACCOUNT_TIMEZONES = list(zip(pytz.all_timezones, pytz.all_timezones))
ACCOUNT_LANGUAGES = []