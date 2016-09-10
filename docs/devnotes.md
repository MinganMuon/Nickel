# Development Notes

* What amount of unit tests should there be for the various
different subsections of Nickel?
* Sometimes the CheckerBoard code repeats itself and does not
follow the DRY principle. Should it be more DRY? For example,
the get(left/right)(up/down) functions repeat most of their code
between themselves with minor changes.
* If there are two paths that a tile can take in a jump, the ui
would not allow the user to select between them. Is this easily
fixable?