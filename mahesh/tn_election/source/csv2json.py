# csv2json.py

import csv
import json
import sys


def clean_int(value):
    try:
        return int(str(value).replace(",", "").strip())
    except:
        return 0


def main():

    if len(sys.argv) != 3:
        print("Usage: python csv2json.py source.csv 2021")
        sys.exit(1)

    csv_file = sys.argv[1]
    target_year = str(sys.argv[2]).strip()

    constituency_map = {}

    with open(csv_file, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row_year = row.get("YEAR", "").strip()

            # Filter by year
            if row_year != target_year:
                continue

            constituency_name = row.get("AC_NAME", "").strip()

            key = constituency_name

            if key not in constituency_map:

                constituency_map[key] = {
                    "constituency_name": constituency_name,
                    "district": row.get("District", "").strip(),
                    "constituency_type": row.get("AC_TYPE", "").strip(),
                    "polled_votes": clean_int(row.get("polled_votes", 0)),
                    "candidates": []
                }

            candidate = {
                "party": row.get("PARTY", "").strip(),
                "name": row.get("NAME", "").strip(),
                "votes_received": clean_int(row.get("VOTES", 0)),
                "rank": clean_int(row.get("rank", 0))
            }

            constituency_map[key]["candidates"].append(candidate)

    # Sort candidates by rank
    for constituency in constituency_map.values():
        constituency["candidates"].sort(key=lambda x: x["rank"])

    output = {
        "year": clean_int(target_year),
        "constituencies": list(constituency_map.values())
    }

    output_file = f"./../output/tn_election_{target_year}.json"

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(output, json_file, indent=4, ensure_ascii=False)

    print(f"JSON file created: {output_file}")


if __name__ == "__main__":
    main()