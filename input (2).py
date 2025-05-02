import serial
import time
import matplotlib.pyplot as plt

# Serial port configuration
SERIAL_PORT = 'COM6'       # Change this to your actual port
BAUD_RATE = 115200         # Match this with your device
OUTPUT_FILE = 'serial_output.txt'

def read_and_save_serial_data():
    try:
        Start = input()
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser, open(OUTPUT_FILE, 'w') as file:
            print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
            
            
            start_time = time.time()  # Start the timer
            
            while time.time() - start_time < 3.5:  # Run for 3 seconds
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    value = float(line)  # Convert to float
                    
                    # If the value is less than 100, set it to 0
                    if value < 100:
                        value = 0
                    
                    print(f"Received: {value}")
                    file.write(f"{value}\n")
                    file.flush()  # Ensure immediate writing to file

                #time.sleep(1)  # Wait 1 second before checking again
                
            print("3 seconds have passed. Data collection stopped.")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("\nData collection stopped by user.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")



def get_peak_value(peak_value):
        if peak_value is not None:
            print(f"The peak value from the data is: {peak_value}")
            if 700 < peak_value < 1200:
                print("Distance: 10cm, Height: 10cm")
            elif peak_value >= 1200:
                print("Distance: 10cm, Height: 30cm")
            elif 50 < peak_value < 300:
                print("Distance: 30cm, Height: 10cm")
            elif 300 < peak_value <= 700:
                print("Distance: 30cm, Height: 30cm")
            else:
                print("Peak value is out of the specified range.")

if __name__ == '__main__':
    #settling_time = input("Enter samples value")
    peak_value = input("Enter Peak value")
    #material = get_settling_time()  # Get material from the settling time function
    get_peak_value(peak_value)  # Pass the detected material to get_peak_value
    #plot_serial_data()
