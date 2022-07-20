import pytest
import difflib

# from pomodoro.pomodoro_gui import *
# from pomodoro.pomodoro_gui import PomodoroTimer
# from pomodoro.omar import ListOfOptions
from pomodoro.omar import *
from tests.flo import diff


def test_print_main_menu():
    ls = ListOfOptions()
    diffs =diff(ls.main_menu,"tests/text_sims/main_menu.txt")
    assert not diffs, diffs

# def test_print_settings():
#     ls = ListOfOptions()
#     diffs =diff(ls.settings,"tests/text_sims/settings.txt")
#     assert not diffs, diffs

def test_print_add_task():
    ls = ListOfOptions()
    diffs =diff(ls.task_add,"tests/text_sims/add_task.txt")
    assert not diffs, diffs

def test_view_list_of_tasks():
    ls = ListOfOptions()
    diffs = diff(ls.view_list_of_tasks, "tests/text_sims/view_list_of_tasks.txt")
    assert not diffs, diffs


# def test_input_add_task():


# def test_body_weloming():
#     mm = Body()
#     ls = ListOfOptions()
#     actual = mm.welcoming_main_menu()
#     expected = ls.main_menu()


# def test_print_main_menu():
#     ls = ListOfOptions()
#     actual = ls.main_menu()
#     print(actual)
#     expected ='''
#            Welcome to Pomodoro
#            Please chose from the following:
#            S) To start Pomodoro
#            A) To add a task
#            V) View all tasks
#            ST) Settings
#            Q) Quit Pomodoro
#            '''
#     assert actual == expected


# @pytest.fixture
# def list_of_options():
#     ls = ListOfOptions()
#     return ls


# if __name__ == '__main__':
#     pytest.main()