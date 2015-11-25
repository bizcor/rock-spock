#!/usr/bin/env python

import cgi
from flask import Flask, request, redirect
import os
import subprocess
import twilio.twiml

APPDIR = '{}/twilio/rock-paper-scissors-spock-lizard-app.d'.format(
    os.environ['HOME'])
BINDIR = '{}/bin'.format(APPDIR)
PROGRAM = '{}/rock-paper-scissors-lizard-spock.py'.format(BINDIR)
LOGFILE = '{}/app.log'.format(APPDIR)

IMAGE_SERVER_URL = os.environ.get('ROCK_SPOCK_IMAGE_SERVER_URL')

HELP_MESSAGE = (
    'greetings!  i am your friendly rock-paper-scissors-lizard-spock app!'
    '  to play with me, text me one of the words'
    ''' ['rock', 'paper', 'scissors', 'lizard', 'spock'].'''
    '  i will then randomly choose one for myself'
    ' and let you know who won!'
    '  (see also: http://en.wikipedia.org/wiki/Rock-paper-scissors)'
)

image_for = {
    'rock': 'rock.jpg',
    'paper': 'paper.png',
    'scissors': 'scissors.png',
    'lizard': 'lizard.png',
    'spock': 'spock.jpg',
}

app = Flask(__name__)


def image_url(winner):
    return '{}/images/{}'.format(IMAGE_SERVER_URL, image_for[winner])


@app.route("/rock-spock", methods=['GET', 'POST'])
def get_results():
    '''call rock paper scissors lizard spock program if user gave a
       valid choice.  otherwise send help or error response as
       appropriate.
    '''

    print '--------------------------------------------------------'
    log_handle.write(
        "--------------------------------------------------------\n")

    from_number = request.values.get('From', None)
    body = request.values.get('Body', None).strip()

    print "from => '{}'".format(from_number)
    log_handle.write("from => '{}'\n".format(from_number))

    print "body => '{}'".format(body)
    log_handle.write("body => '{}'\n".format(body))

    choice = body.strip()
    lc_choice = choice.lower()

    you_sent = '[you sent "{}".]'.format(cgi.escape(choice))

    if lc_choice == "help" or lc_choice == "help me" \
            or lc_choice == "helpme" or lc_choice == "app help" \
            or lc_choice == "apphelp":
        message = '{}  {}'.format(you_sent, HELP_MESSAGE)
        image = IMAGE_SERVER_URL + '/images/roshambolizspo.png'

        response = (
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>'
            '{}</Body><Media>{}</Media></Message></Response>'.format(
                message, image)
        )
        return response

    if lc_choice not in image_for.keys():
        message = '{}  hmmm.  it looks like "{}" is not one of {}.'.format(
            you_sent, cgi.escape(lc_choice), image_for.keys())
        message = '{}  would you like to try again?'.format(message)
        print "message => '{}'".format(message)
        log_handle.write("message => '{}'\n".format(message))
        image = IMAGE_SERVER_URL + '/images/doh_l.gif'
        print "image => '{}'".format(image)
        log_handle.write("image => '{}'\n".format(image))
        response = (
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>'
            '{}</Body><Media>{}</Media></Message></Response>'.format(
                message, image)
        )
        return response

    p = subprocess.Popen([PROGRAM, choice],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()

    message = ''
    winner = ''

    if err != '':
        message = 'eeeeek:  {}'.format(err)
    else:
        lines = out.split('\n')
        for line in lines:
            if 'app.out.text::::' in line:
                fields = line.split('::::')
                message = "{}  {}".format(you_sent, fields[1])
            elif 'app.out.winner::::' in line:
                fields = line.split('::::')
                winner = fields[1]

    print "message => '{}'\nwinner => '{}'\nimage url => '{}'".format(
        message, winner, image_url(winner))
    log_handle.write("message => '{}'\nwinner => '{}'\nimage url => '{}'\n".
                     format(message, winner, image_url(winner)))

    response = (
        '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>'
        '{}</Body><Media>{}</Media></Message></Response>'.format(
            message, image_url(winner))
    )

    print "response => '{}'".format(response)
    log_handle.write("response => '{}'\n".format(response))

    log_handle.flush()

    return response


if __name__ == "__main__":
    log_handle = open(LOGFILE, 'a')
    app.run(debug=True, host='0.0.0.0', port=9898)
    log_handle.close()
    exit(0)
