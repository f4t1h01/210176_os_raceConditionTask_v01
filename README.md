4) README.md (how to run)
# Booking Overbooking Demo (Critical Section)

## What this shows
This project demonstrates how overbooking happens due to a race condition
and how it can be prevented using synchronization.

## Setupe
```bash
cd backend
pip install -r requirements.txt

# Run the server
# IMPORTANT: use ONE worker so the shared variable is truly shared.
uvicorn main:app --host 127.0.0.1 --port 8000

# Run the simulation (new terminal)
cd backend
python simulation.py
```
