from fastapi import FastAPI
import asyncio

app = FastAPI(title="Overbooking Demo")

TOTAL_SEATS = 10
available_seats = TOTAL_SEATS

seat_lock = asyncio.Lock()


@app.get("/reset")
async def reset():
    global available_seats
    available_seats = TOTAL_SEATS
    return {"message": "reset done", "available_seats": available_seats}


@app.get("/status")
async def status():
    return {"available_seats": available_seats}


@app.post("/book/unprotected")
async def book_unprotected():
    """
    NO protection:
    - read seats
    - delay (makes race obvious)
    - write seats
    """
    global available_seats

    if available_seats <= 0:
        return {"success": False, "message": "no seats left", "available_seats": available_seats}

    current = available_seats
    await asyncio.sleep(0.05)
    available_seats = current - 1

    return {"success": True, "message": "booked (UNPROTECTED)", "available_seats": available_seats}


@app.post("/book/protected")
async def book_protected():
    """
    WITH protection (async lock):
    the entire read-check-write is one protected critical section
    """
    global available_seats

    async with seat_lock:
        if available_seats <= 0:
            return {"success": False, "message": "no seats left", "available_seats": available_seats}

        current = available_seats
        await asyncio.sleep(0.05)
        available_seats = current - 1

    return {"success": True, "message": "booked (PROTECTED)", "available_seats": available_seats}
