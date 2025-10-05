import csv
import json
import pandas as pd

# Part 1 - Task 1: Create the Tabular CSV Data (Requires Cleaning)

print("Begin Part 1: Acquisition and Flexible Formatting")
print()

print("Begin Task 1: Create the Tabular CSV Data")

rows = [
    {"student_id": 1, "major": "Computer Science", "GPA": 3.9, "is_cs_major": "Yes", "credits_taken": "15.0"},
    {"student_id": 2, "major": "Mathematics", "GPA": 3, "is_cs_major": "No", "credits_taken": "12.0"},
    {"student_id": 3, "major": "Computer Science", "GPA": 3.75, "is_cs_major": "Yes", "credits_taken": "32"},
    {"student_id": 4, "major": "Economics", "GPA": 3.2, "is_cs_major": "No", "credits_taken": "77.0"},
    {"student_id": 5, "major": "Statistics", "GPA": 2, "is_cs_major": "No", "credits_taken": "45.0"}
]

headers = ["student_id", "major", "GPA", "is_cs_major", "credits_taken"]

print("    Writing to raw_survey_data.csv")

with open("raw_survey_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print("    Wrote to raw_survey_data.csv")
print()


# Part 1 - Task 2: Create the Hierarchical JSON Data (Requires Normalization)

print("Begin Task 2: Create the Hierarchical JSON Data")

courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "CS3240",
        "section": "002",
        "title": "Software Engineering",
        "level": 300,
        "instructors": [
            {"name": "Derick Stone", "role": "Primary"},
            {"name": "Ryan Leyhe", "role": "TA"}
        ]
    },
    {
        "course_id": "CS4640",
        "section": "001",
        "title": "Defense Against the Dark Arts",
        "level": 400,
        "instructors": [
            {"name": "Jack Davidson", "role": "Primary"},
            {"name": "Andrew Dovan", "role": "TA"}
        ]
    },
    {
        "course_id": "APMA3150",
        "section": "003",
        "title": "From Data to Knowledge",
        "level": 300,
        "instructors": [
            {"name": "Meiqin Li", "role": "Primary"},
            {"name": "Logan Toth", "role": "TA"}
        ]
    },
    {
        "course_id": "CS3130",
        "section": "002",
        "title": "Computer Systems and Organization II",
        "level": 300,
        "instructors": [
            {"name": "Kevin Skadron", "role": "Primary"},
            {"name": "Dominic Tran", "role": "TA"}
        ]
    }
]

print("    Writing to raw_course_catalog.json")

with open("raw_course_catalog.json", "w", encoding="utf-8") as f:
    json.dump(courses, f)

print("    Wrote to raw_course_catalog.json")
print()

# Part 2 - Task 3: Clean and Validate the CSV Data

print("Begin Part 2: Data Validation and Type Casting")
print()
print("Begin Task 3: Clean and Validate the CSV Data")
print("    Reading raw_survey_data.csv")

csv_df = pd.read_csv("raw_survey_data.csv")

csv_df["is_cs_major"] = (
    csv_df["is_cs_major"].map({"Yes": True, "No": False})
)

csv_df = csv_df.astype({
    "GPA": "float64",
    "credits_taken": "float64"
})

print("    Writing to clean_survey_data.csv")

csv_df.to_csv("clean_survey_data.csv")

print("    Wrote to clean_survey_data.csv")
print()

# Part 2 - Task 4: Normalize the JSON Data

print("Begin Task 4: Normalize the JSON Data")

with open("raw_course_catalog.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

print("    Normalizing JSON data")

json_df = pd.json_normalize(json_data, record_path=["instructors"], meta=["course_id", "title", "level"])

print("    Writing to clean_course_catalog.csv")

json_df.to_csv("clean_course_catalog.csv")

print("    Wrote to clean_course_catalog.csv")