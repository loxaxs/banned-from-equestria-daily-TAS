from fast import sleep, skip
from info import center
from model import State
from util import logboth


@logboth
def encounter_trixie(st: State, action):
    if action == 'twilight':
        if 'trixie2' not in st.encounter:
            st.encounter['trixie2'] = 'twilight'
        else: pass
    elif action == 'trixie':
        if 'trixie1' not in st.encounter:
            sleep(.2)
            skip(7)
            st.encounter['trixie1'] = True
        elif 'trixie2' not in st.encounter: pass
        elif st.encounter['trixie2'] == 'trixie': pass
        else:
            st.encounter['trixie2'] = 'trixie'
            sleep(0.8)
            skip(2)
            sleep(3.5)
            skip()


@logboth
def break_shield_trixie(st: State):
    if 'trixie_shield' not in st.encounter:
        center.click()
        sleep(.8)
        skip(1)
        st.encounter['trixie_shield'] = True