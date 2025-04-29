##############
# Functions
##############


BALL = False
STRIKE = True

def pitch(speed, pitch_type):
    if pitch_type not in ('fastball', 'curve', 'slider'):
        raise Exception('What type of pitch is that???')

    if pitch_type == 'curve':
        if speed > 90:
            return BALL
        else:
            return STRIKE
    # More code...


def do_pitch(strikes, balls, speed, pitch_type):
    if pitch(speed, pitch_type):
        strikes = strikes + 1
    else:
        balls = balls + 1
    print(strikes)
    print(balls)



strikes = 0
balls = 0
do_pitch(strikes, balls, 91, 'curve')
print(strikes)
print(balls)