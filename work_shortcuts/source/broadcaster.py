def get_broadcasts(participant, sport):

    event = find_event(participant, sport)

    if not event:
        return None

    broadcasts = []

    broadcasts += sporteventz.find(event)
    broadcasts += sportmonks.find(event)

    return merge_results(event, broadcasts)
