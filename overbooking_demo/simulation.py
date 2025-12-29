import asyncio
import httpx

BASE = "http://127.0.0.1:8000"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

async def run_test(endpoint: str, n_requests: int):
    async with httpx.AsyncClient(timeout=10) as client:
        await client.get(f"{BASE}/reset")

        tasks = [client.post(f"{BASE}{endpoint}") for _ in range(n_requests)]
        results = await asyncio.gather(*tasks)

        data = [r.json() for r in results]
        success_count = sum(1 for x in data if x.get("success") is True)
        status = (await client.get(f"{BASE}/status")).json()

        print(BOLD + CYAN + "\n===================================" + RESET)
        print(BOLD + f"Endpoint: {endpoint}" + RESET)
        print(f"Total requests sent: {n_requests}")
        print(f"Successful bookings: {success_count}")
        print(f"Final available seats: {status['available_seats']}")

        if endpoint == "/book/unprotected":
            print(RED + "⚠ Overbooking occurred (race condition)" + RESET)
        else:
            print(GREEN + "✔ Overbooking prevented (critical section protected)" + RESET)

        print(CYAN + "Sample responses:" + RESET)
        for r in data[:5]:
            print(" ", r)

async def main():
    print(BOLD + RED + "\nUNPROTECTED CASE (NO LOCK)" + RESET)
    await run_test("/book/unprotected", 80)

    print(BOLD + GREEN + "\nPROTECTED CASE (WITH LOCK)" + RESET)
    await run_test("/book/protected", 80)

if __name__ == "__main__":
    asyncio.run(main())
