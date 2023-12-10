
import time
from pygoogle_image import image as pi

def download_images(query, limit=3):
    try:
        pi.download(keywords=query, limit=limit)
        print(f"Машины загвар {query} амжилттай даталаа")
    except Exception as e:
        print(f"Алдаа заавал {query}-д амжилтгүй боллоо: {e}")

cars = ['mercedes', 'toyota', 'ferrari', 'tesla', 'volkswagen', 'bugatti', 'rolls royce', 'maserati']

for car in cars:
    download_images(car)
    time.sleep(1)  # Add a delay to avoid rate limits

