import pytesseract
import time
start = time.time()
string = pytesseract.image_to_string('./figure-65.png')
end = time.time()
time_elapsed = end - start
print(string)
print("time elapsed: {0} seconds".format(time_elapsed))
