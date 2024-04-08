from pathlib import Path
from typing import Any, Dict

import emails
from emails.template import JinjaTemplate

from app.config.settings import settings
from app.schemas import EmailContent, EmailValidation
from app.utils.logger import logger_system

EMAIL_TEMPLATES_DIR = settings.email_platform.EMAIL_TEMPLATES_DIR


def read_template(template_name: str) -> str:
    with open(Path(EMAIL_TEMPLATES_DIR) / template_name) as f:
        return f.read()


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
    template_name: str = None,
) -> None:
    assert settings.email_platform.EMAILS_ENABLED, "no provided configuration for email variables"
    if template_name:
        html_template = read_template(template_name)

    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings.email_platform.EMAILS_FROM_NAME, settings.email_platform.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.smtp.SMTP_HOST, "port": settings.smtp.SMTP_PORT}
    if settings.email_platform.SMTP_TLS:
        smtp_options["ssl"] = True
    if settings.email_platform.SMTP_USER:
        smtp_options["user"] = settings.smtp.SMTP_USER
    if settings.email_platform.SMTP_PASSWORD:
        smtp_options["password"] = settings.smtp.SMTP_PASSWORD

    environment.update({
        "server_host": settings.general.SERVER_HOST,
        "server_name": settings.general.SERVER_NAME,
        "server_bot": settings.general.SERVER_BOT,
    })

    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logger_system.info(f"send email result: {response}")


def send_email_validation_email(data: EmailValidation) -> None:
    subject = f"{settings.general.PROJECT_NAME} - {data.subject}"
    link = f"{settings.general.SERVER_HOST}?token={data.token}"
    template_name = "confirm_email.html"
    send_email(
        email_to=data.email,
        subject_template = subject,
        template_name = template_name,
        environment = {'link': link}
    )

def send_web_contact_email(data: EmailContent) -> None:
    subject = f"{settings.general.PROJECT_NAME} - {data.subject}"
    template_name = "web_contact_email.html"
    send_email(
        email_to=settings.email_platform.EMAILS_TO_EMAIL,
        subject_template=subject,
        template_name=template_name,
        environment={"content": data.content, "email": data.email},
    )

def send_test_email(email_to: str) -> None:
    subject = f"{settings.general.PROJECT_NAME} - Test email"
    template_name = "test_email.html"
    send_email(
        email_to=email_to,
        subject_template=subject,
        template_name=template_name,
        environment={"project_name": settings.general.PROJECT_NAME, "email": email_to},
    )

def send_magic_login_email(email_to: str, token: str) -> None:
    subject = f"Your {settings.general.PROJECT_NAME} magic login"
    template_name = "magic_login.html"
    link = f"{settings.general.SERVER_HOST}?magic={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        template_name=template_name,
        environment={
            "project_name": settings.general.PROJECT_NAME,
            "valid_minutes": int(settings.jwt.ACCESS_TOKEN_EXPIRE_SECONDS / 60),
            "link": link,
        },
    )

def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    subject = f"{settings.general.PROJECT_NAME} - Password recovery for user {email}"
    template_name = "reset_password.html"
    link = f"{settings.general.SERVER_HOST}/reset-password?token={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        template_name=template_name,
        environment={
            "project_name": settings.general.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": int(settings.jwt.ACCESS_TOKEN_EXPIRE_SECONDS / 60),
            "link": link,
        },
    )

def send_new_account_email(email_to: str, username: str, password: str) -> None:
    subject = f"{settings.general.PROJECT_NAME} - New account for user {username}"
    template_name = "new_account.html"
    link = settings.general.SERVER_HOST
    send_email(
        email_to=email_to,
        subject_template=subject,
        template_name=template_name,
        environment={
            "project_name": settings.general.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": link,
        },
    )