import pytest
from mock import Mock

from ROVMessaging.MessageChannel import MessageChannel
from ROVMessaging.MessageType import MessageType
from ROVMessaging.Message import Message
from ROVMessaging.Subscriber import Subscriber

@pytest.fixture
def mockSubscriber():
    return Mock(spec=Subscriber)

@pytest.fixture
def messageChannel():
    return MessageChannel()

def test_can_create_a_message_channel(messageChannel):
    assert isinstance(messageChannel, MessageChannel)

def test_a_subscriber_can_subscribe_to_a_message_channel(messageChannel, mockSubscriber):
    status = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)

    assert status == True

def test_a_subscriber_can_not_be_added_to_the_same_channel_twice(messageChannel, mockSubscriber):
    status1 = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)

    assert status1 == True

    status2 = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)

    assert status2 == False

def test_a_subscriber_can_subscribe_to_multiple_message_types(messageChannel, mockSubscriber):
    status = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)
    status2 = messageChannel.subscribe(MessageType.SYSTEM_STATUS, mockSubscriber)

    assert status == True
    assert status2 == True

def test_different_subscribers_can_subscribe_to_the_same_message_type(messageChannel):
    status = messageChannel.subscribe(MessageType.SYSTEM_STATUS, mockSubscriber)
    status2 = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)

    assert status == True
    assert status2 == True

def test_a_subscriber_can_unsubscribe_from_a_message_channel_that_it_is_subscribed_to(messageChannel, mockSubscriber):
    messageChannel.subscribe(MessageType.SYSTEM_STATUS, mockSubscriber)
    status = messageChannel.unsubscribe(MessageType.SYSTEM_STATUS, mockSubscriber)

    assert status == True

def test_a_subscriber_can_only_unsubsubribe_if_it_belongs_to_the_message_channel(messageChannel, mockSubscriber):
    status = messageChannel.unsubscribe(MessageType.SYSTEM_STATUS, mockSubscriber)

    assert status == False

def test_unsubscribing_a_subscriber_only_unsubscribes_them_from_the_specified_message_type(messageChannel, mockSubscriber):
    messageChannel.subscribe(MessageType.SYSTEM_STATUS, mockSubscriber)
    messageChannel.subscribe(MessageType.ACTION, mockSubscriber)

    status1 = messageChannel.unsubscribe(MessageType.SYSTEM_STATUS, mockSubscriber)
    status2 = messageChannel.unsubscribe(MessageType.ACTION, mockSubscriber)

    assert status1 == True
    assert status2 == True

def test_a_non_subsubscribed_subscriber_does_not_recieve_broadcasted_messages(messageChannel, mockSubscriber):
    message = Message(MessageType.ACTION, "Do Something")
    messageChannel.broadcast(message)

    mockSubscriber.recieveMessage.assert_not_called()

def test_a_message_channel_can_broadcast_a_message_to_all_of_its_subscribers(messageChannel):
    subscriber = Mock(spec=Subscriber)
    subscriber2 = Mock(spec=Subscriber)

    messageChannel.subscribe(MessageType.ACTION, subscriber)
    messageChannel.subscribe(MessageType.ACTION, subscriber2)

    message = Message(MessageType.ACTION, "Move!")
    messageChannel.broadcast(message)

    subscriber.recieveMessage.assert_called_once_with(message)
    subscriber2.recieveMessage.assert_called_once_with(message)

def test_a_susbscriber_only_recieves_messages_from_the_channels_that_it_is_subscribed_to(messageChannel):
    subscriber = Mock(spec=Subscriber)
    subscriber2 = Mock(spec=Subscriber)

    messageChannel.subscribe(MessageType.ACTION, subscriber)
    messageChannel.subscribe(MessageType.SYSTEM_STATUS, subscriber2)

    message = Message(MessageType.ACTION, "Move!")
    messageChannel.broadcast(message)

    subscriber.recieveMessage.assert_called_once_with(message)
    subscriber2.recieveMessage.assert_not_called()

def test_is_processing_in_parallel_is_false_by_default(messageChannel):
    assert messageChannel.isProcessingInParallel() == False

def test_a_message_channel_can_be_set_to_process_messages_in_parallel(messageChannel):
    assert messageChannel.isProcessingInParallel() == False

    messageChannel.setProcessInParallel(True)

    assert messageChannel.isProcessingInParallel() == True

# def test_if_not_is_processing_in_parallel_messages_should_be_sent_sequentially():
#     assert False

# def test_if_is_processing_in_parallel_messages_should_be_sent_in_seperate_threads():
#     assert False
#
