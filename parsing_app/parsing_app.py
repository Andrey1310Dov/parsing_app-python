import re
import os
from parsing_app.function import search_id, search_login, search_sender,\
     search_recipient, search_sent, remove_id

def start():
    print('Input name of a file: ',end='')
    path = input()
    path = os.getcwd() + '\parsing_app\logs\\' + path
    
    with open(path, 'r') as file:
        file = list(file)
        # the dictionary of active id
        dict_id = {}
        # the dictionary of id sent anything
        dict_a_id = {}
        # the dictionary sender's mails contain statistics sent messages and not recieved messages
        dict_senders = {}
        # the dictionary of recipients
        dict_recipients = []
        # a loop for parsing
        for line in file:
            id_ = search_id(line)
            # search a client has been logined
            client = search_login(line)
            if client:
                if id_ not in dict_id:
                    dict_id[id_] = ''
           # search sender's mails and add it in dictionaries
            sender = search_sender(line)
            if sender and id_ in dict_id:
                dict_a_id[id_] = sender
                if sender not in dict_senders:
                    dict_senders[sender] = {'sent': 0, 'failed': 0}
            # search count sent messages from one mail
            sent = search_sent(line)
            if sent and id_ in dict_a_id:
                recipient = search_recipient(line)
                dict_recipients.append((recipient ,id_))
                if sent == 'sent':
                    dict_senders[dict_a_id[id_]]['sent'] += 1
                    dict_recipients.remove((recipient ,id_))
         # remove id together mail after using
            rm_id = remove_id(line)
            if rm_id and rm_id in dict_a_id:
                for elem in dict_recipients:
                    if elem[1] == rm_id:
                        dict_senders[dict_a_id[rm_id]]['sent'] += 1
                        dict_senders[dict_a_id[rm_id]]['failed'] += 1
                        dict_recipients.remove(elem)
                dict_a_id.pop(rm_id)


    for key, value in dict_senders.items():
        print('Mailbox "{}" sent "{}" messages. "{}" of them were with errors.'.format(key,value["sent"],value["failed"]))

