from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType

def test_can_create_a_message():
    message = Message(MessageType.ACTION, "Move Forward")

    assert isinstance(message, Message)

def test_can_get_the_contents_of_a_message():
    contents = "Move Forward"
    message = Message(MessageType.ACTION, contents)

    assert message.getContents() == contents

def test_can_get_the_type_of_the_message():
    type = MessageType.SYSTEM_STATUS
    message = Message(type, "This statement is false!")

    assert message.getType() == type
