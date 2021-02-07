import pytest
from mock import Mock

from MessageChannel import MessageChannel
from MessageType import MessageType
from Subscriber import Subscriber

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

# def test_a_subscriber_can_not_be_added_to_the_same_channel_twice(messageChannel, mockSubscriber):
#     status1 = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)
#
#     assert status1 == True
#
#     status2 = messageChannel.subscribe(MessageType.ACTION, mockSubscriber)
#
#     assert status2 == False


# def test_a_subscriber_can_unsubscribe_from_a_message_channel():
#     assert False
#
# def test_a_subscriber_can_only_unsubsubribe_if_it_belongs_to_the_message_channel():
#     assert False
#
# def test_a_message_channel_can_broadcast_a_message_to_all_of_its_subscribers():
#     assert False
#
# def test_a_susbscriber_only_recieves_messages_from_the_channels_that_it_is_subsribed_to():
#     assert False
    # mock_susbscriber.recieveMessage()
    # mock_susbscriber.recieveMessage.assert_called_once()
#
# def test_a_message_channel_can_be_set_to_process_messages_in_parallel():
#     assert False

# def test_if_not_is_processing_in_parallel_messages_should_be_sent_sequentially():
#     assert False
#
# def test_if_is_processing_in_parallel_messages_should_be_sent_in_seperate_threads():
#     assert False
