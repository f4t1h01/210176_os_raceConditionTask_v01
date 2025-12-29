# Booking System Overbooking – Critical Section Report

## Centrum Air overbooking case
The Centrum Air overbooking case is a real example of what happens when more
tickets are sold than the number of available seats. Passengers with valid
tickets were unable to board the flight, which caused delays and complaints.
This situation is similar to a software system allowing more bookings than
its capacity.

## Critical section
A critical section is a part of a program where a shared resource is accessed.
If multiple requests enter this section at the same time without control,
the program can produce incorrect results.

- In this project, the critical section is the code that checks and updates
the number of available seats.


## Read/Write conflict (race condition)
When two booking requests arrive at the same time, both can read the same
number of available seats before either one updates it. As a result, both
requests succeed even though only one seat was available. This causes
overbooking and is called a race condition.


## Producer–Consumer analogy
Available seats can be compared to a limited container. Booking requests act
as consumers that try to take a seat. Without synchronization, multiple
consumers can take the same last seat at the same time.


## Solution and why it works
To prevent overbooking, a lock is used around the critical section. The lock
ensures that only one booking request can read and update the seat count at
a time. This guarantees that once seats reach zero, no further bookings are
allowed.


## Conclusion
This project demonstrates:
- Overbooking without protection (race condition)
- Safe booking with synchronization (lock)
- How critical sections must be protected in concurrent systems
