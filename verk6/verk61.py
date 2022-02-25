from Adafruit_IO import *

aio = Client('thorhallurt', 'aio_ybgq74X7UVstaUk6LfZO7r0bMar7')

aio.send('hello', 'Hello, World')
