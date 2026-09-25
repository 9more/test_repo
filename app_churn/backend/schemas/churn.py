NUMERIC_FEATURES = [
    "eqpdays",
    "months",
    "change_mou",
    "totmrc_Mean",
    "mou_Mean",
    "avgqty",
    "change_rev",
    "hnd_price",
    "mou_cvce_Mean",
    "avg3mou",
    "uniqsubs",
    "totcalls",
]

CATEGORICAL_FEATURES = [
    "asl_flag",
    "crclscod",
    "refurb_new",
]

REQUIRED_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
