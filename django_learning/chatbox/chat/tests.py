from django.test import TestCase

from .models import Message


class MessageModelTests(TestCase):
    
    def test___str___with_short_message_text(self):
        """
        __str__ returns complete message if message_text is shorter than
        21 characters
        """
        text = "I'm a short message."
        message = Message(message_text = text)
        result_text = message.__str__
        expected_text = "{} sent {}".format(message.message_text, message.send_date)

        self.assertIs(
            expected_text,
            result_text
            )


    def test___str___with_long_message_text(self):
            """
            __str__ returns complete message if message_text is longer than
            21 characters
            """
            text = "I'm a looong message."
            message = Message(message_text = text)
            result_text = message.__str__
            expected_text = "{}... sent {}".format(message.message_text[:20], message.send_date)

            self.assertIs(
                expected_text,
                result_text
                )