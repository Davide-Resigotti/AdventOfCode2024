safe = 0


def is_safe(report):
    """Check if a report is safe by the original rules."""
    is_ascending = True
    is_descending = True
    valid_distance = True

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        # Check for ascending or descending order
        if diff > 0:
            is_descending = False
        elif diff < 0:
            is_ascending = False

        # Check for valid distance
        if abs(diff) < 1 or abs(diff) > 3:
            valid_distance = False
            break

    return valid_distance and (is_ascending or is_descending)


with open("day2/input.txt") as file:
    for row in file:
        # Convert the row into a list of integers
        row = list(map(int, row.split()))
        print("element: " + str(row))

        # First, check if the row is safe as-is
        if is_safe(row):
            print("distance ok")
            safe += 1
        else:
            # If not safe, apply the Problem Dampener
            for i in range(len(row)):
                # Create a new list with the current level removed
                modified_row = row[:i] + row[i + 1 :]
                if is_safe(modified_row):
                    print(f"Safe after removing level {row[i]}: {modified_row}")
                    safe += 1
                    break  # Count the report as safe and stop checking further removals

print("safe: " + str(safe))
