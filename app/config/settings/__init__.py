from app.config.settings.email.main import Email
from app.config.settings.general.main import General
from app.config.settings.jwt.main import JWT
from app.config.settings.main import get_settings
# from app.config.settings.services.main import Service
from app.config.settings.smtp.main import SMTP
from app.config.settings.totp.main import TOTP

settings = get_settings()