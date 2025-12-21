from colorama import Fore, init
from glob import glob
import importlib.util
import time
import sys
import os

init()


def run_solution(year, day):
    day_str = f"{day:02d}"
    solution_path = os.path.join(str(year), day_str, "solution.py")

    if not os.path.exists(solution_path):
        raise FileNotFoundError(f"Solution file not found: {solution_path}")

    original_cwd = os.getcwd()
    solution_dir = os.path.dirname(solution_path)
    os.chdir(solution_dir)

    import_time = 0
    parts = []
    try:
        spec = importlib.util.spec_from_file_location("solution", "solution.py")
        solution_module = importlib.util.module_from_spec(spec)
        sys.modules["solution"] = solution_module

        start_time = time.time()
        spec.loader.exec_module(solution_module)
        end_time = time.time()
        import_time = end_time - start_time

        # Run part1
        if hasattr(solution_module, "part1"):
            start_time = time.time()
            result1 = solution_module.part1()
            end_time = time.time()
            time1 = end_time - start_time
            parts.append((result1, time1))

        # Run part2
        if hasattr(solution_module, "part2"):
            start_time = time.time()
            result2 = solution_module.part2()
            end_time = time.time()
            time2 = end_time - start_time
            parts.append((result2, time2))

    except Exception as e:
        raise e
    finally:
        os.chdir(original_cwd)

    return parts, import_time


def fmt_time(seconds):
    if seconds < 1e-3:
        return f"{seconds * 1e6:5.1f} µs"
    if seconds < 1:
        return f"{seconds * 1e3:5.1f} ms"
    if seconds < 60:
        return f"{seconds:5.2f} s "
    m, s = divmod(seconds, 60)
    return f"{int(m):2d}m {s:5.1f}s "


def resolve_values(value, min_value=None, max_value=None):
    if value == "*":
        if min_value is None or max_value is None:
            raise ValueError("'*' requires min_value and max_value")
        return list(range(min_value, max_value + 1))

    result = set()

    for part in value.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            result.update(range(start, end + 1))
        else:
            result.add(int(part))

    return sorted(result)


def print_solution(year, day):
    if not os.path.exists(os.path.join(str(year), f"{day:02d}")):
        return

    try:
        parts, import_time = run_solution(year, day)
    except Exception as e:
        print(f"[{year}/{day:02d}] {Fore.RED}{e}{Fore.RESET}")
        return

    part_str = " | ".join(
        [f"p{i} {fmt_time(t)}" for i, (_, t) in enumerate(parts, start=1)]
    )
    total = sum(part[1] for part in parts) + import_time

    print(
        f"{year}/{day:02d} | {part_str} | import {fmt_time(import_time)} | total {fmt_time(total)}"
    )


if __name__ == "__main__":
    import sys

    years_arg, days_arg = sys.argv[1:]

    # resolve years and days into lists
    years = resolve_values(years_arg, min_value=2015, max_value=2025)
    days = resolve_values(days_arg, min_value=1, max_value=25)

    for year in years:
        for day in days:
            print_solution(year, day)
