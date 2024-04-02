from raven import Client

from app.config.settings.main import Settings

client_sentry = Client(Settings.general.SENTRY_DSN)
