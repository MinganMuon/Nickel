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
wins/losses against different AIs recorded in a database. It 
will have support for multiple AIs.

Nickel was developed for AI research, particularly in the field
of neural networks. As such, the AI section will be the most
expansive and complex of the three sections. Not only will
the web interface be able to access the latest AI generation,
the AI section will have several desktop windows for evolving the
neural networks and other AI related tasks.

## Roadmap to 0.3

* Implement a minimax module.

* Improve the minimax module (depth sensing, optimization, etc.)

* Implement a simple evaluation function to test minimax.

* Test the new AI against humans and the random AI.
