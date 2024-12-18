import pyfirmata2
from time import sleep
# Establish a connection to the Arduino board
PORT = pyfirmata2.Arduino.AUTODETECT
arduino = pyfirmata2.Arduino(PORT)

# Define the SysEx command for printing a string on the LCD
LCD_PRINT = 0x01
LCD_CLEAR = 0x02
LCD_SET_CURSOR = 0x03

# Define the string to print
message = "Hello, World!"

# Convert the string to bytes
message_bytes = [ord(char) for char in message]

# Set the cursor to the first row position [x, y]
arduino.send_sysex(LCD_SET_CURSOR, [0, 0])

# Set the cursor to the second row position [x, y]
arduino.send_sysex(LCD_SET_CURSOR, [0, 1])

# Send the command and the string to the Arduino
arduino.send_sysex(LCD_PRINT, message_bytes)

# Clear the LCD
# arduino.send_sysex(LCD_CLEAR, [])

# Close the connection to the board
arduino.exit()