import Jetson.GPIO as GPIO
import time
def fun():
	# Configuración de los pines GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	
	try:
	    
	        # Enciende el relé
	        GPIO.output(7, GPIO.LOW)
        	print("Relay ON")
	        time.sleep(5)
	
	        # Apaga el relé
	        GPIO.output(7, GPIO.HIGH)
	        print("Relay OFF")
	        time.sleep(1)
	
	except KeyboardInterrupt:
	    GPIO.cleanup()

if __name__ == '__main__':
    GPIO.setwarnings(False)
    fun()
