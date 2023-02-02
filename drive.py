#All non-power I/O is 3.3V output and 5V tolerant on input,
# links
# https://docs.odriverobotics.com/v/0.5.5/encoders.html#encoders-hall-effect
# to check hall sensor/encoder is good https://docs.odriverobotics.com/v/0.5.5/hoverboard.html#hoverboard-doc
# maxon https://www.maxongroup.com/maxon/view/product/motor/ecmotor/ecflat/ecflat60/642221

### MOTOR
#sets M0 current limit to 75 amps. Should be careful, because the stall current of our motor
#is 83 amps
odrv0.axis0.motor.config.requested_current_range = 80 #increases the range, must reboot to execute this
odrv0.axis0.motor.config.current_lim = 75
#velocity limit turn/s. 54 is the max our motor should ever go
odrv0.axis0.controller.config.vel_limit = 54
#calibration current, should be less than the max continuous current
odrv0.axis0.motor.config.calibration_current = 9
#brake resistor
odrv0.config.enable_brake_resistor = True
odrv0.config.brake_resistance = 2 #this is in ohms
#negative current sent back to the power supply. defaults to 10mA
# if getting DC_BUS_OVER_REGEN_CURRENT error, make this value more negative
#odrv0.config.dc_max_negative_current = -0.01
#pole pairs
odrv0.axis0.motor.config.pole_pairs = 7
#torque constant
odrv0.axis0.motor.config.torque_constant = 52.5 # TODO: ensure this is correct
#motor type
odrv0.axis0.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT #DEBUG: this line might be missing a [0] parameter
# should be less than 0.5 * DC bus voltage. 
odrv0.axis0.motor.config.resistance_calib_max_voltage = 10.0 
odrv0.axis0.motor.config.current_control_bandwidth = 100 #TODO: figure this out







###Hall sensor feedback control. Alternatively, use encoder configuration
# pinout https://docs.odriverobotics.com/v/0.5.5/encoders.html#encoders-hall-effect
odrv0.axis0.encoder.config.mode = ENCODER_MODE_HALL
# cpr is pole pairs * 6 (6 is the number of hall states) = 42
odrv0.axis0.encoder.config.cpr = 42
#this is basically the distance the motor can turn while calibrating
odrv0.axis0.encoder.config.calib_scan_distance = 150.1 
#specify the hall pins as digital pins
odrv0.config.gpio9_mode = GPIO_MODE_DIGITAL
odrv0.config.gpio10_mode = GPIO_MODE_DIGITAL
odrv0.config.gpio11_mode = GPIO_MODE_DIGITAL
odrv0.axis0.encoder.config.bandwidth = 100 #TODO: figure out this line and the three above
###

###encoder configuration -- once we have these 
#Connect the encoder(s) to J4. The A,B phases are required, and the 
# Z (index pulse) is optional. The A,B and Z lines have 3.3k pull up resistors, 
# for use with open-drain encoder outputs.
#odrv0.axis0.encoder.config.mode = ENCODER_MODE_ABSOLUTE

#encoder count per revolution value
#odrv0.axis0.encoder.config.cpr = 
###


#CONTROL
odrv0.axis0.controller.config.pos_gain = 1
odrv0.axis0.controller.config.vel_gain = 0.02 * odrv0.axis0.motor.config.torque_constant * odrv0.axis0.encoder.config.cpr
odrv0.axis0.controller.config.vel_integrator_gain = 0.1 * odrv0.axis0.motor.config.torque_constant * odrv0.axis0.encoder.config.cpr
odrv0.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
#this will reboot the board and permanently save these configuration settings
odrv0.save_configuration()




#activate calibration process 
odrv0.axis0.requested_state = AXIS_STATE_MOTOR_CALIBRATION

#read the data about the motor
odrv0.axis0.motor
odrv0.axis0.motor.config.phase_inductance
odrv0.axis0.motor.config.phase_resistance

#only execute this if everything looks good.. it saves calibration to persistent memory
#odrv0.axis0.motor.config.pre_calibrated = True
