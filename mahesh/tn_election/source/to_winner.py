# summary_generator.py

import csv
import json
import sys


def clean_int(value):
    try:
        return int(str(value).replace(",", "").strip())
    except:
        return 0


def get_best_candidate(rows, target_rank):

    filtered = []

    for row in rows:
        if clean_int(row.get("rank", 0)) == target_rank:
            filtered.append(row)

    if not filtered:
        return None

    filtered.sort(
        key=lambda x: clean_int(x.get("VOTES", 0)),
        reverse=True
    )

    return filtered[0]


def main():

    if len(sys.argv) != 3:
        print("Usage: python summary_generator.py source.csv 2021")
        sys.exit(1)

    csv_file = sys.argv[1]
    target_year = str(sys.argv[2]).strip()

    constituency_map = {}

    with open(csv_file, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row_year = row.get("YEAR", "").strip()

            # Filter only target year
            if row_year != target_year:
                continue

            constituency = row.get("AC_NAME", "").strip()

            if constituency not in constituency_map:
                constituency_map[constituency] = []

            constituency_map[constituency].append(row)

    final_output = []

    for constituency, rows in constituency_map.items():

        # Get row having highest polled_votes
        best_polled_row = max(
            rows,
            key=lambda x: clean_int(x.get("polled_votes", 0))
        )

        votes_polled = clean_int(
            best_polled_row.get("polled_votes", 0)
        )

        winner = get_best_candidate(rows, 1)
        runner = get_best_candidate(rows, 2)
        second_runner = get_best_candidate(rows, 3)
        third_runner = get_best_candidate(rows, 4)

        winner_votes = clean_int(
            winner.get("VOTES", 0)
        ) if winner else 0

        runner_votes = clean_int(
            runner.get("VOTES", 0)
        ) if runner else 0

        second_runner_votes = clean_int(
            second_runner.get("VOTES", 0)
        ) if second_runner else 0

        third_runner_votes = clean_int(
            third_runner.get("VOTES", 0)
        ) if third_runner else 0

        item = {

            "constituency": constituency,

            "district": best_polled_row.get(
                "District",
                ""
            ).strip(),

            "votes_polled": votes_polled,

            "winner_candidate": winner.get(
                "NAME",
                ""
            ).strip() if winner else "",

            "winner_party": winner.get(
                "PARTY",
                ""
            ).strip() if winner else "",

            "winner_votes": winner_votes,

            "winner_votes_diff_from_runner":
                winner_votes - runner_votes,

            "runner_candidate": runner.get(
                "NAME",
                ""
            ).strip() if runner else "",

            "runner_party": runner.get(
                "PARTY",
                ""
            ).strip() if runner else "",

            "runner_votes": runner_votes,

            "runner_votes_diff_from_winner":
                runner_votes - winner_votes,

            "second_runner": second_runner.get(
                "NAME",
                ""
            ).strip() if second_runner else "",

            "second_runner_party": second_runner.get(
                "PARTY",
                ""
            ).strip() if second_runner else "",

            "second_runner_votes": second_runner_votes,

            "second_runner_diff_from_winner":
                second_runner_votes - winner_votes,

            "third_runner": third_runner.get(
                "NAME",
                ""
            ).strip() if third_runner else "",

            "third_runner_party": third_runner.get(
                "PARTY",
                ""
            ).strip() if third_runner else "",

            "third_runner_votes": third_runner_votes,

            "third_runner_diff_from_winner":
                third_runner_votes - winner_votes
        }

        final_output.append(item)

    # Sort by constituency
    final_output.sort(
        key=lambda x: x["constituency"]
    )

    # -----------------------------
    # JSON OUTPUT
    # -----------------------------

    json_output_file = (
        f"./../output/tn_election_summary_{target_year}.json"
    )

    with open(
        json_output_file,
        "w",
        encoding="utf-8"
    ) as json_file:

        json.dump(
            final_output,
            json_file,
            indent=4,
            ensure_ascii=False
        )

    # -----------------------------
    # CSV OUTPUT
    # -----------------------------

    csv_output_file = (
        f"./../output/tn_election_summary_{target_year}.csv"
    )

    if final_output:

        headers = final_output[0].keys()

        with open(
            csv_output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file_out:

            writer = csv.DictWriter(
                csv_file_out,
                fieldnames=headers
            )

            writer.writeheader()
            writer.writerows(final_output)

    print(f"JSON file created: {json_output_file}")
    print(f"CSV file created: {csv_output_file}")


if __name__ == "__main__":
    main()