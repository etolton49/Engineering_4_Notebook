from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
#declaring variables for controlling LEDS





app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def index():
        global red_led
        global blue_led
        global msg
        global msg2
        
        if request.method == "GET":
                GPIO.output(21, GPIO.LOW)
                msg = "Red: Off"
                msg2 = "Blue: Off"
                red_led = False
                blue_led = False
                
        elif request.method == "POST":
                #controlling red LED
                if request.form['Submit'] == 'redled':
                        if red_led:
                                msg = "Red: Off"
                                red_led = False
                                GPIO.output(21, GPIO.LOW)   
                        else:
                                msg = "Red: On"
                                red_led = True
                                GPIO.output(21, GPIO.HIGH)
                                
                #controlling blue LED
                if request.form['Submit'] == 'blueled':
                        if blue_led:
                                msg2 = "Blue: Off"
                                blue_led = False
                                GPIO.output(20, GPIO.LOW)   
                        else:
                                msg2 = "Blue: On"
                                blue_led = True
                                GPIO.output(20, GPIO.HIGH)


                        
        return render_template("index.html", msg=msg, msg2=msg2)

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 80)

GPIO.cleanup()
