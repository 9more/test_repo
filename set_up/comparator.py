import pandas as pd

# --------------------------------------------------
# Time windows
# --------------------------------------------------

MORNING_START = "06:00"
MORNING_END = "23:59"

NIGHT_START = "00:00"
NIGHT_END = "10:00"


# --------------------------------------------------
# Filtering
# --------------------------------------------------


def is_excluded(row):
    """
    Completely remove Tennis + InFront events.
    """

    sport = str(row["Sport"]).strip().lower()

    data_source = str(row["DataSource"]).strip().lower()

    return sport == "tennis" and data_source.startswith("infront")


def filter_schedule(df):
    """
    Remove rows that are not relevant to the comparison.

    Currently excluded:
        Tennis + Infront

    All other rows remain.
    """

    return df[~df.apply(is_excluded, axis=1)].copy()


# --------------------------------------------------
# Date/time handling
# --------------------------------------------------


def add_sort_time(df):
    """
    Add a temporary datetime column based on StartTime.

    Example StartTime:

        08/09/2026 11:00:00

    dayfirst=True ensures this is interpreted correctly.
    """

    result = df.copy()

    result["_sort_time"] = pd.to_datetime(
        result["StartTime"], dayfirst=True, errors="coerce"
    )

    return result


def sort_by_start_time(df):
    """
    Sort the schedule chronologically.

    If two events have the same StartTime,
    their original CSV order is preserved.
    """

    result = add_sort_time(df)

    result["_original_order"] = range(len(result))

    result = result.sort_values(by=["_sort_time", "_original_order"], kind="stable")

    result = result.drop(columns=["_original_order"])

    return result


# --------------------------------------------------
# Time filtering
# --------------------------------------------------


def filter_time_window(df, start_time, end_time):
    """
    Return events within a specified daily time window.

    Start time is inclusive.
    End time is exclusive.

    Example:

        00:00 -> 10:00

    includes events from 00:00 through 09:59:59,
    but excludes 10:00.
    """

    result = add_sort_time(df)

    start = pd.to_datetime(start_time, format="%H:%M").time()

    end = pd.to_datetime(end_time, format="%H:%M").time()

    event_times = result["_sort_time"].dt.time

    result = result[(event_times >= start) & (event_times < end)].copy()

    return result


# --------------------------------------------------
# Morning comparison
# --------------------------------------------------


def compare_morning(df):
    """
    Compare today's schedule chronologically.

    Only events from 06:00 through 23:59 are returned.

    Rules:

        Tennis + InFront
            -> removed completely

        InFront / InFront Streaming / Modus
            -> retained but never marked switch

        Other datasources with a broadcaster change
            -> switch

        No broadcaster change
            -> blank
    """

    # -----------------------------------------
    # Remove excluded rows
    # -----------------------------------------

    result = filter_schedule(df)

    # -----------------------------------------
    # Sort chronologically
    # -----------------------------------------

    result = sort_by_start_time(result)

    # -----------------------------------------
    # Apply morning time window
    # -----------------------------------------

    result = filter_time_window(result, MORNING_START, MORNING_END)

    result = result.sort_values(by="_sort_time", kind="stable")

    # -----------------------------------------
    # Add Status column
    # -----------------------------------------

    result["Status"] = ""

    # -----------------------------------------
    # Track the latest broadcaster per server
    # -----------------------------------------

    last_broadcaster = {}

    for index, row in result.iterrows():

        server = str(row["Server"]).strip()

        broadcaster = str(row["Broadcaster"]).strip()

        data_source = str(row["DataSource"]).strip().lower()

        if not server or not broadcaster:
            continue

        # -------------------------------------
        # First event for this server
        # -------------------------------------

        if server not in last_broadcaster:

            last_broadcaster[server] = broadcaster

            continue

        # -------------------------------------
        # Broadcaster changed
        # -------------------------------------

        if broadcaster != last_broadcaster[server]:

            # InFront and Modus events are retained,
            # but they must never receive "switch".
            if not (
                data_source.startswith("infront") or data_source.startswith("modus")
            ):

                result.at[index, "Status"] = "switch"

            # Always update the latest broadcaster.
            last_broadcaster[server] = broadcaster

    # -----------------------------------------
    # Remove temporary column
    # -----------------------------------------

    result = result.drop(columns=["_sort_time"])

    return result


# --------------------------------------------------
# Night comparison
# --------------------------------------------------


def compare_night(today_df, tomorrow_df):
    """
    Compare tomorrow's schedule against the LAST
    broadcaster assigned to each server today.

    Only tomorrow's events from 00:00 through 09:59:59
    are returned.

    Rules:

        InFront / Modus
            -> no status

        Server not used today
            -> check channel

        Server used today + same broadcaster
            -> blank

        Server used today + different broadcaster
            -> switch

    Tennis + InFront rows are removed completely.
    """

    # -----------------------------------------
    # Filter both schedules
    # -----------------------------------------

    today = filter_schedule(today_df)
    tomorrow = filter_schedule(tomorrow_df)

    # -----------------------------------------
    # Sort chronologically
    # -----------------------------------------

    today = sort_by_start_time(today)
    tomorrow = sort_by_start_time(tomorrow)

    # -----------------------------------------
    # Find LAST broadcaster for each server today
    # -----------------------------------------

    last_broadcaster = {}

    for _, row in today.iterrows():

        server = str(row["Server"]).strip()

        broadcaster = str(row["Broadcaster"]).strip()

        if not server or not broadcaster:
            continue

        last_broadcaster[server] = broadcaster

    # -----------------------------------------
    # Restrict tomorrow to 00:00 -> 10:00
    # -----------------------------------------

    result = filter_time_window(tomorrow, NIGHT_START, NIGHT_END)

    result = result.sort_values(by="_sort_time", kind="stable")

    # -----------------------------------------
    # Add Status
    # -----------------------------------------

    result["Status"] = ""

    # -----------------------------------------
    # Compare tomorrow against today's
    # LAST broadcaster
    # -----------------------------------------

    for index, row in result.iterrows():

        server = str(row["Server"]).strip()

        broadcaster = str(row["Broadcaster"]).strip()

        data_source = str(row["DataSource"]).strip().lower()

        if not server or not broadcaster:
            continue

        # -------------------------------------
        # IMPORTANT:
        # InFront and Modus events should NEVER
        # receive switch OR check channel.
        # -------------------------------------

        if data_source.startswith("infront") or data_source.startswith("modus"):
            continue

        # -------------------------------------
        # Server does not exist today
        # -------------------------------------

        if server not in last_broadcaster:

            result.at[index, "Status"] = "check channel"

            continue

        # -------------------------------------
        # Server exists today.
        # Compare tomorrow's broadcaster with
        # the LAST broadcaster today.
        # -------------------------------------

        if broadcaster != last_broadcaster[server]:

            result.at[index, "Status"] = "switch"

    # -----------------------------------------
    # Remove temporary column
    # -----------------------------------------

    result = result.drop(columns=["_sort_time"])

    return result
