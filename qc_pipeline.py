import pandas as pd
import argparse

def load_data(path):
    return pd.read_csv(path)

def check_missing(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_ranges(df):
    issues = {}
    for col in df.select_dtypes(include="number").columns:
        if (df[col] < 0).any():
            issues[col] = "Contains negative values"
    return issues

def generate_report(missing, duplicates, ranges):
    print("\n=== QC REPORT ===")
    print("Missing Values:")
    print(missing)
    print("\nDuplicate Rows:", duplicates)
    print("\nRange Issues:")
    for col, issue in ranges.items():
        print(f"- {col}: {issue}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    df = load_data(args.input)
    missing = check_missing(df)
    duplicates = check_duplicates(df)
    ranges = check_ranges(df)

    generate_report(missing, duplicates, ranges)

if __name__ == "__main__":
    main()
