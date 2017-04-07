from pyslideshare import pyslideshare

api_key = '' # Your api key secret_key = '' # Your secret key

obj = pyslideshare.pyslideshare(locals(), verbose=True)
print(obj.get_slideshow(slideshow_id=436333))