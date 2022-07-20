import pytest
import difflib
import mock
import builtins
from pomodoro.omar import *
from tests.flo import diff

"""
This test will mock print the main menu
"""
def test_print_main_menu():
    ls = ListOfOptions()
    diffs =diff(ls.main_menu,"tests/text_sims/main_menu.txt")
    assert not diffs, diffs

def test_settings_input(list_of_options):
    with mock.patch.object(builtins, 'input', lambda _: '10', '5', '25'):
        assert list_of_options.settings('10','5','25') == '''
           L ) Long Break : 10 m every 4 running Pomodoro's
           SH ) Short Break : 5 m
           P ) Pomodoro's:  25 m
           R ) To return to main menu

           Enter the settings symbol that you want to change .'''

def test_settings_selected(list_of_options):
    # with mock.patch.object(builtins, 'input', lambda _: 'short break'):
        assert list_of_options.settings_selected('short break') == '''
        Enter the new time for the short breaksection time in minutes
        press Enter to confirm your choice
        R) To return to main menu'''

"""
This test will mock print the add task menu
"""
def test_print_add_task():
    ls = ListOfOptions()
    diffs =diff(ls.task_add,"tests/text_sims/add_task.txt")
    assert not diffs, diffs

# def test_task_after_added(list_of_options):
#     assert list_of_options.task_after_added() == '''
#  Task Added Successfully
#
#             V) View all the Tasks
#             R) To return to starting menu'''

"""
This test will mock print the view list of tasks menu
"""
def test_view_list_of_tasks():
    ls = ListOfOptions()
    diffs = diff(ls.view_list_of_tasks, "tests/text_sims/view_list_of_tasks.txt")
    assert not diffs, diffs

"""
This test will mock print the select existing menu
"""
def test_print_select_existing_task():
    ls = ListOfOptions()
    diffs = diff(ls.select_existing_task, "tests/text_sims/select_existing_task.txt")
    assert not diffs, diffs

# def test_print_start_pomodoro(list_of_options):
#     default = '''
#         Time: 25 minutes / long break 10 minutes /short break 5 minutes'''
#     assert list_of_options.start_pomodoro(default) == '''
#
#         To start Pomodoro:
#         Time: 25 minutes / long break 10 minutes /short break 5 minutes
#               A) add task to work on
#               S) select existing task
#               R) return to main menu
#
#     '''

def test_print_show_default_value(list_of_options):
    assert list_of_options.show_default_value('25','10','5') == '''
        Time: 25 minutes / long break 10 minutes /short break 5 minutes'''

"""
This test will mock print no tasks found menu
"""
def test_print_no_tasks_found():
    ls = ListOfOptions()
    diffs = diff(ls.no_tasks_founded, "tests/text_sims/no_tasks_found.txt")
    assert not diffs, diffs

"""
This test will mock print task in progress menu
"""
def test_print_task_in_progress():
    ls = ListOfOptions()
    diffs = diff(ls.task_in_progress, "tests/text_sims/task_in_progress.txt")
    assert not diffs, diffs

def test_print_settings(list_of_options):
    assert list_of_options.settings('10','5','25') == '''
           L ) Long Break : 10 m every 4 running Pomodoro's
           SH ) Short Break : 5 m
           P ) Pomodoro's:  25 m
           R ) To return to main menu

           Enter the settings symbol that you want to change .'''

"""
This test will mock input of the task description
"""
def test_input_task_desc(in_handler):
    with mock.patch.object(builtins, 'input', lambda _: 'task 1'):
        assert in_handler.input_task_desc() == 'task 1'

def test_input_messenger(body):
    with mock.patch.object(builtins, 'input', lambda _: 'task 1'):
        assert body.input_messenger('msg') == 'task 1'

def test_quit_pomodoro(body):
    with mock.patch('sys.exit') as exit_mock:
        body.quit_pomodoro()
        assert exit_mock.called





@pytest.fixture
def list_of_options():
    ls = ListOfOptions()
    return ls

@pytest.fixture
def body():
    bd = Body()
    return bd

@pytest.fixture
def in_handler():
    user_in = InputHandler()
    return user_in

# if __name__ == '__main__':
#     pytest.main()
