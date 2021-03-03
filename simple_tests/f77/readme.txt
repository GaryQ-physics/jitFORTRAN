benchmark 2 and 3 take ~3.04 seconds for 1000000000 points, while
benchmark 1 only takes ~2.58 seconds

this indicates that compiling sub.f seperately into sub.o and linking later
doesnt affect performance, but inline SUB into the loop in SUBV does.
