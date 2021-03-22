import nimlib
from time import time
import requests


if __name__ == '__main__':

    url = 'https://yandex.ru'

    start = time()
    py_result = requests.get(url)
    py_elapsed = time() - start

    start = time()
    nim_result = nimlib.get(url)
    nim_elapsed = time() - start

    assert py_result.text[:1000] == nim_result[:1000]
    print(f'{py_elapsed=:.2f}, {nim_elapsed=:.2f}')  # py_elapsed=0.55, nim_elapsed=0.60
