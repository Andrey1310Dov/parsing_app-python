import re

def search_id(line):
    id_ = re.search( r'[A-Z0-9]{11}\: ', line)
    if id_ is not None:
        id_ = id_.group()[:-2]
        return id_
    else:
        return False


def search_login(line):
    feature_1 = re.search( r'sasl_method=', line)
    feature_2 = re.search( r'sasl_username=', line)
    if feature_1 and feature_2:
        id_ = re.search( r'[A-Z0-9]{11}\: ', line)
        if id_ is not None:
            id_ = id_.group()[:-2]
            return id_
        else:
            return False


def search_sender(line):
    feature_1 = re.search( r'from=', line)
    feature_2 = re.search( r'size=', line)
    feature_3 = re.search( r'nrcpt=', line)
    if feature_1 and feature_2 and feature_3:
        sender = re.search( r'<[\w].+@[\w].+\.[\w]+>', line)
        if sender is not None:
            sender = sender.group()[1:-1]
            return sender
        else:
            return False
    else:
        return False


def search_recipient(line):
    recipient = re.search( r'<[\w].+@[\w].+\.[\w]+>', line)
    if recipient is not None:
        recipient = recipient.group()[1:-1]
        return recipient
    else:
        return False


def search_sent(line):
    feature_1 = re.search( r'to=', line)
    feature_2 = re.search( r'relay=', line)
    feature_3 = re.search( r'dsn=', line)
    feature_4 = re.search( r'status=', line)
    if feature_1 and feature_2 and feature_3 and feature_4:
        sent = re.search( r'status=[\w]+\ \(', line)
        if sent is not None:
            sent = sent.group()[7:-2]
            return sent
        else:
            return False
    else:
        return False


def remove_id(line):
    feature_1 = re.search( r'removed', line)
    if feature_1:
        remove_id = re.search( r'[A-Z0-9]{11}\: ', line)
        if remove_id is not None:
            remove_id = remove_id.group()[:-2]
            return remove_id
        else:
            return False
    else:
        return False

