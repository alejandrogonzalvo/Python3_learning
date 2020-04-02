from django.test import TestCase
from django.db import utils

from .models import Message, Conversation


class MessageModelTests(TestCase):
    def test___str___with_short_message_text(self):
        """
        __str__ returns complete message if message_text is shorter than
        21 characters
        """
        text = "I'm a short message."
        message = Message(message_text=text)
        result_text = message.__str__()
        expected_text = "\n{} // sent {}\n".format(
            message.message_text, message.send_date
            )

        self.assertAlmostEqual(
            expected_text,
            result_text
            )

    def test___str___with_long_message_text(self):
        """
        __str__ returns complete message if message_text is longer than
        21 characters
        """
        text = "I'm a looong message."
        message = Message(message_text=text)
        result_text = message.__str__()
        expected_text = "\n{}... // sent {}\n".format(
            message.message_text[:20], message.send_date
            )

        self.assertAlmostEqual(
            expected_text,
            result_text
            )

    def test_conversation_name_that_surpasses_max_length(self):
        """
        A name longer than the max length should raise a DataError exception.
        """
        self.assertRaises(
            utils.DataError,
            conversation=Conversation(
                conversation_name="""This name Actually surpases the maximum
                characters available to put on a conversation_name""")
        )


class ConversationModelTests(TestCase):
    def test_conversation_name_that_surpasses_max_length(self):
        """
        A name longer than the max length should raise a DataError exception.
        """
        self.assertRaises(
            utils.DataError,
            conversation=Conversation(
                conversation_name="""This name Actually surpases the maximum
                characters available to put on a conversation_name""")
        )
