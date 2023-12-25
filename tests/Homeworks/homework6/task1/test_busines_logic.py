import src.Homeworks.homework6.task1.AVLtree as AVLtree
import src.Homeworks.homework6.task1.business_logic as business_logic
import pytest
import os.path


def test_file_validation(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "wrong_name1.txt wrong_name2.txt wrong_name3.txt",
    )
    with pytest.raises(ValueError):
        business_logic.main()


@pytest.mark.parametrize(
    "command, args, res_file",
    (
        ("ADD", "result.txt", (1, 2, 3)),
        ("ADD", "result.txt", ()),
        ("GET", "result.txt", ()),
        ("GET", "result.txt", (1, 2)),
        ("SELECT", "result.txt", ()),
        ("SELECT", "result.txt", (1, 2)),
    ),
)
def test_command_selection_exceptions(command, args, res_file):
    test_tree = AVLtree.create_tree_map()
    with pytest.raises(ValueError):
        business_logic.command_selection(test_tree, command, res_file, *args)


def test_main_scenario_runner(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "tests/Homeworks/homework6/task1/input.txt results.txt balance.txt",
    )
    business_logic.main()
    assert os.path.exists(f"results.txt")
    assert os.path.exists(f"balance.txt")


def test_main_scenario():
    expected_results, expected_balance, actual_results, actual_balance = [], [], [], []
    with open("tests/Homeworks/homework6/task1/shop_balance_expected.txt") as file:
        for line in file.readlines():
            expected_balance.append(line)
    with open("tests/Homeworks/homework6/task1/shop_results_expected.txt") as file:
        for line in file.readlines():
            expected_results.append(line)
    with open("balance.txt") as file:
        for line in file.readlines():
            actual_balance.append(line)
    with open("results.txt") as file:
        for line in file.readlines():
            actual_results.append(line)
    assert expected_balance == actual_balance and expected_results == actual_results
