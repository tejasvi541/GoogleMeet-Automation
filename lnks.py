dict = {'subject name': 'meeting_code',
        'subject name': 'meeting_code',
        'subject name': 'meeting_code',
        'subject name': 'meeting_code'
        }


def getLnk(csub):

    for keys, value in dict.items():
        if csub == keys:
            clink = value
    return clink
