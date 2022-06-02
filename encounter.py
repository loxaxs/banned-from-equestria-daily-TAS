from fast import sleep, skip
from info import center
from model import State
from util import logboth


@logboth
def encounter_trixie(st: State, action):
    if action == 'twilight':
        if 'trixie2' not in st.status:
            st.status['trixie2'] = 'twilight'
        else: pass
    elif action == 'trixie':
        if 'trixie1' not in st.status:
            skip(8)
            st.status['trixie1'] = True
        elif 'trixie2' not in st.status: pass
        elif st.status['trixie2'] == 'trixie': pass
        else:
            st.status['trixie2'] = 'trixie'
            sleep(2)
            skip(6)
            sleep(4)
            skip()


@logboth
def break_shield_trixie(st: State):
    if 'trixie_shield' not in st.status:
        center.click()
        sleep(.8)
        skip(1)
        st.status['trixie_shield'] = True


@logboth
def break_second_shield_trixie(st: State):
    if 'second_trixie_shield' not in st.status:
        center.click()
        sleep(.8)
        skip(1)
        st.status['second_trixie_shield'] = True