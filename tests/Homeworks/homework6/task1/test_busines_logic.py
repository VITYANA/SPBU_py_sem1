import src.Homeworks.homework6.task1.AVLtree as AVLtree
import src.Homeworks.homework6.task1.busines_logic as busines_logic
import pytest
import os.path


def test_file_validation(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "wrong_name.txt",
    )
    with pytest.raises(ValueError):
        busines_logic.main()


@pytest.mark.parametrize(
    "command, args",
    (
        ("ADD", (1, 2, 3)),
        ("ADD", ()),
        ("GET", ()),
        ("GET", (1, 2)),
        ("SELECT", ()),
        ("SELECT", (1, 2)),
    ),
)
def test_command_selection_exceptions(command, args):
    test_tree = AVLtree.create_tree_map()
    with pytest.raises(ValueError):
        busines_logic.command_selection(test_tree, command, *args)


def test_main_scenario_runner(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "input",
    )
    busines_logic.main()
    assert os.path.exists(f"results.txt")
    assert os.path.exists(f"balance.txt")


def test_main_scenario():
    expected_results, expected_balance, actual_results, actual_balance = [], [], [], []
    with open("shop_balance_expected") as file:
        for line in file.readlines():
            expected_balance.append(line)
    with open("shop_results_expected") as file:
        for line in file.readlines():
            expected_results.append(line)
    with open("balance.txt") as file:
        for line in file.readlines():
            actual_balance.append(line)
    with open("results.txt") as file:
        for line in file.readlines():
            actual_results.append(line)
    assert expected_balance == actual_balance and expected_results == actual_results
