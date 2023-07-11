def calculate_minimum_classes(students):
    classes = max(2, students // 30 + 1)
    students_per_class = students // classes
    remainder = students % classes

    allocated = {}
    for i in range(1, classes + 1):
        if i <= remainder:
            allocated[f"Class {i}"] = students_per_class + 1
        else:
            allocated[f"Class {i}"] = students_per_class

    print(f"Proposed Allocation: {classes} classes")
    print(allocated)


calculate_minimum_classes(31)
calculate_minimum_classes(59)
calculate_minimum_classes(86)
