<p align="center">
  <img src="https://github.com/user-attachments/assets/2ff01561-62f0-45cd-b986-f2af760cbba9" alt="2025 Day 1 Visualization" width="600">
</p>



## Key Points for Advent of Code 2025

### Day 1: Secret Entrance

**Story Summary**

* Elves finally adopted project management and realized they have no time left to decorate the North Pole.
* You must help finish the decorations by solving puzzles to collect stars.
* You reach a secret entrance, but the password has changed and is stored in a safe.
* The attached document gives a sequence of safe dial rotations.

**Dial Mechanics**

* Dial has values from 0 to 99 in a circle.
* L means rotate left toward lower numbers.
* R means rotate right toward higher numbers.
* Rotations wrap around (0 goes to 99 when turning left; 99 goes to 0 when turning right).
* Dial starts at 50.

**Part One Logic**

* Perform each rotation.
* Count how many times the dial ends a rotation pointing at 0.
* The total number of end-at-zero events is the password.
* Example shows 3 occurrences.
* Your final answer for Part One was **1066**.

**Part Two Logic**

* New rule: count every time the dial points at 0, including all intermediate clicks during rotation.
* Each click matters, not just the final position.
* Large rotations can pass 0 multiple times.
* Example total becomes 6 because intermediate steps add extra zero hits.
* Your final answer for Part Two was **6223**.

