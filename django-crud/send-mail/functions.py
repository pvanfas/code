from django.conf import settings
from mailqueue.models import MailerMessage


def send_email(
    to_address,
    subject,
    content,
    html_content,
    bcc_address=None,
    attachment=None,
    attachment2=None,
    attachment3=None,
):
    new_message = MailerMessage()
    new_message.subject = subject
    new_message.to_address = to_address

    if bcc_address:
        new_message.bcc_address = bcc_address

    new_message.from_address = settings.DEFAULT_FROM_EMAIL
    new_message.content = content
    new_message.html_content = html_content
    new_message.cc_address = settings.DEFAULT_CC_EMAIL
    if attachment:
        new_message.add_attachment(attachment)
    if attachment2:
        new_message.add_attachment(attachment2)
    if attachment3:
        new_message.add_attachment(attachment3)
    new_message.app = "our app name"
    new_message.save()
