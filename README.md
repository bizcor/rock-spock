# rock-spock

A python flask application that uses Twilio and multimedia messaging to play the game rock-paper-scissors-lizard-spock.  Rock-paper-scissors-lizard-spock is described at <https://en.wikipedia.org/wiki/Rock-paper-scissors#Additional_weapons>.

## How to play

Send a text message to the app's Twilio phone number:  **+1 415 801 0700**.  Go ahead.  Do it!

| If you send this text | Here's what will happen |
| :-------------------- |:------------------------|
| any of ['app help', 'apphelp', 'help me', 'helpme'] | you'll get a help message |
| any of ['rock', 'paper', 'scissors', 'lizard', 'spock']  | you'll play the game |
| anything else | you'll get a message indicating your response was not understood |

Note that if you send the word 'help' you'll get the help message as long as whatever delivers the text to my Twilio phone number above doesn't intercept it and show you *their* help message.  That is, if my app gets 'help' it will send you a help message.  But my experience has been that 'help' doesn't get to my app.
