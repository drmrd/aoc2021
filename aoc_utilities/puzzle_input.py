from pathlib import Path

import git


REPO_ROOT = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
PUZZLE_INPUTS_DIRECTORY = REPO_ROOT / 'puzzle_inputs'


def as_text(day: int) -> str:
    puzzle_input = PUZZLE_INPUTS_DIRECTORY / f'Day {day}.txt'
    try:
        return puzzle_input.read_text()
    except FileNotFoundError as error:
        raise ValueError(
            f'No puzzle input file found for Day {day}. '
            'You may still need to download it from '
            f'https://adventofcode.com/2021/day/{day}/input (after '
            'logging in).'
        )