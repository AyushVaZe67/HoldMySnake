import asyncio
import time

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name} after {delay} seconds!")
    return f"Done with {name}"

async def main():
    start = time.time()

    # Create tasks to run concurrently
    results = await asyncio.gather(
        say_hello("Ayush", 2),
        say_hello("Mia", 3),
        say_hello("Leo", 1)
    )

    print("\nResults:", results)
    print("Time taken:", time.time() - start)

# Run the event loop
asyncio.run(main())
