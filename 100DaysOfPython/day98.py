import multiprocessing
import requests
import os

def download_files(url, name):
    print(f'Started: {name}')
    response = requests.get(url)
    # Ensure directory exists
    os.makedirs('files', exist_ok=True)
    open(f'files/{name}.jpg', 'wb').write(response.content)
    print(f'Finished: {name}')

if __name__ == "__main__":  # ✅ REQUIRED for multiprocessing
    url = 'https://picsum.photos/2000/3000'
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=download_files, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
