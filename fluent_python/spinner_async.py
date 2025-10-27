import asyncio
import itertools
import time
from multiprocessing import synchronize

def main() -> None:
  result = asyncio.run(supervisor())
  print(f'Answer: {result}')

async def spin(msg: str) -> None:
  for char in itertools.cycle(r'\|/-'):
    status = f'\r{char} {msg}'
    print(status, end='', flush=True)
    try:
      await asyncio.sleep(.1)
    except asyncio.CancelledError:
      break

  blanks = ' ' * len(status)
  print(f'\r{blanks}\r', end='')

async def slow() -> int:
  await asyncio.sleep(3)
  # Don't use time.sleep in asyncio coroutines
  # unless you want to pause your whole program.
  # time.sleep(3)
  return 42

async def supervisor() -> int:
  spinner = asyncio.create_task(spin('thinking!'))
  print(f'spinner object: {spinner}')
  # Yields control explicitly with the await keyword
  result = await slow()
  spinner.cancel()
  return result

if __name__ == '__main__':
  main()
