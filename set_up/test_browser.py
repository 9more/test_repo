import pandas as pd

from reporter import create_report


def main():

    test_data = [
        {
            "FixtureId": "1",
            "StartTime": "09:00",
            "Server": "Euro201",
            "Broadcaster": "Sky Sports",
            "Status": "",
        },
        {
            "FixtureId": "2",
            "StartTime": "10:00",
            "Server": "Euro201",
            "Broadcaster": "Sky Sports",
            "Status": "",
        },
        {
            "FixtureId": "3",
            "StartTime": "11:00",
            "Server": "Euro201",
            "Broadcaster": "Al Jazeera",
            "Status": "switch",
        },
        {
            "FixtureId": "4",
            "StartTime": "12:00",
            "Server": "Euro201",
            "Broadcaster": "Al Jazeera",
            "Status": "",
        },
        {
            "FixtureId": "5",
            "StartTime": "13:00",
            "Server": "Euro201",
            "Broadcaster": "BBC Sport",
            "Status": "switch",
        },
        {
            "FixtureId": "6",
            "StartTime": "14:00",
            "Server": "Euro202",
            "Broadcaster": "ESPN",
            "Status": "check channel",
        },
    ]

    df = pd.DataFrame(test_data)

    report = create_report(df)

    print("\nGenerated report:\n")
    print(report.to_string(index=False))

    # --------------------------------------------------
    # Tests
    # --------------------------------------------------

    assert len(report) == 3

    assert list(report["FixtureId"]) == [
        "3",
        "5",
        "6",
    ]

    assert list(report["Status"]) == [
        "switch",
        "switch",
        "check channel",
    ]

    assert list(report.columns) == [
        "FixtureId",
        "StartTime",
        "Server",
        "Broadcaster",
        "Status",
    ]

    print("\nAll reporter tests passed.")


if __name__ == "__main__":
    main()
