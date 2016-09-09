# Development Overview

This document is a overview of the structure of Nickel and a
roadmap for various large goals. See devnotes.md for quick notes
about certain developmental items/questions to be addressed.

## Nickel Overview

Nickel is a python-based checkers program developed for AI
research. It consists of three sections:

* CheckerGame, the checker board/game logic.
* A web interface
* The AI(s)

The web interface will give a easy UI for users to play checkers
from. It may have support for multiple users, with their
wins/losses against different AIs recorded in a database It 
will have support for multiple AIs.

Nickel was developed for AI research, particularly in the field
of neural networks. As such, the AI section will be the most
expansive and complex of the three sections. Not only will
the web interface be able to access the latest AI generation,
the AI section will have several desktop windows for evolving the
neural networks and other AI related tasks.

## Roadmap to 0.1

A ? means that said goal may be pushed to a later release.
A ~ means that said goal will be worked on but not completed
until a later release.

### CheckerGame

* Add support for man/king jumps
* Add support for detecting wins by immobilization?
* Optimize the functions?

### Web Interface

* Develop the basic UI
* Interface the client-side code with the CheckerGame and AI
libraries
* Add the basic game logic
* Add nice graphics and make the UI user-friendly~
* Add support for selecting different AIs~
* Test/evaluate the UI via different browsers and users~

### AI

* Develop a random AI that gets the possible moves and selects
one at random.
