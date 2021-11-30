import pytest

from commands.Command import Command
from commands.CommandProcessor import CommandProcessor

@pytest.fixture
def mockCommand():
    return Mock(spec=Command)

@pytest.fixture
def commandProcessor():
    return CommandProcessor()

def test_is_running_is_false_by_default():
    assert False

def test_a_command_can_be_added_to_the_queue():
    assert False

def test_a_command_can_be_removed_from_the_queue():
    assert False

def test_process_commands_executes_all_queued_commands():
    assert False
