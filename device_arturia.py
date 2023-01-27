# name=arturia

# imports
# location C:\Users\**username**\Documents\Image-Line\FL Studio\Settings\Hardware\yyCustom

import mixer
import ui
import transport
import channels
import mixer

# define variables
play_this_song = 36
show_mx = 48
show_pl = 53


def OnMidiMsg(event):

    event.handled = False
    channel_index = channels.selectedChannel()
    print(event.midiId, event.data1, event.data2)
    if event.data1 > 0:

        # Push Button
        if event.midiId == 144:
            if event.data1 == play_this_song:
                transport.start()
                event.handled = True
            if event.data1 == show_mx:
                if ui.getVisible(0) == 0:  # if window is not visible
                    ui.showWindow(0)  # make it visible
                    ui.setFocused(0)
                    event.handled = True
                else:
                    ui.hideWindow(0)  # if it is visible hide it
                    event.handled = True
            if event.data1 == show_pl:
                if ui.getVisible(2) == 0:
                    ui.showWindow(2)
                    event.handled = True
                else:
                    ui.hideWindow(2)
                    event.handled = True
            # Toggle mixer track slot 1
            if event.data1 == 37:
                mixer.enableTrack(1)
                event.handled = True
            # Toggle mixer track slot 2
            if event.data1 == 38:
                mixer.enableTrack(2)
                event.handled = True
            # Toggle mixer track slot 3
            if event.data1 == 39:
                mixer.enableTrack(3)
                event.handled = True
            # Toggle mixer track slot 4
            if event.data1 == 40:
                mixer.enableTrack(4)
                event.handled = True
            # Toggle mixer track slot 5
            if event.data1 == 41:
                mixer.enableTrack(5)
                event.handled = True
            # Toggle mixer track slot 6
            if event.data1 == 42:
                mixer.enableTrack(6)
                event.handled = True
            # Toggle mixer track slot 7
            if event.data1 == 43:
                mixer.enableTrack(7)
                event.handled = True
                
        # Control Button
        if event.midiId == 176:
            if event.data1 > 0:
                if event.data1 == 112 and event.data2 == 65:  # increase the channel index
                    print(channel_index)
                if event.data1 == 112 and event.data2 == 63:  # increase the channel index
                    print(channel_index)
                    
                # Mixer volume 1
                if event.data1 == 74:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(1,vol/100)
                # Mixer volume 2
                if event.data1 == 71:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(2,vol/100)
                # Mixer volume 3
                if event.data1 == 76:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(3,vol/100)
                # Mixer volume 4
                if event.data1 == 77:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(4,vol/100)
                # Mixer volume 5
                if event.data1 == 93:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(5,vol/100)
                # Mixer volume 6
                if event.data1 == 73:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(6,vol/100)
                # Mixer volume 7
                if event.data1 == 75:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(7,vol/100)
                # Mixer volume 8
                if event.data1 == 18:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(8,vol/100)
                # Mixer volume 9
                if event.data1 == 19:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(9,vol/100)
                # Mixer volume 10
                if event.data1 == 16:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(10,vol/100)
                # Mixer volume 11
                if event.data1 == 17:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(11,vol/100)
                # Mixer volume 12
                if event.data1 == 91:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(12,vol/100)
                # Mixer volume 13
                if event.data1 == 79:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(13,vol/100)
                # Mixer volume 14
                if event.data1 == 72:
                    vol = event.data2
                    if vol >= 100:
                        vol = 100
                    mixer.setTrackVolume(14,vol/100)
def OnControlChange(event):
        # I have 5 faders. You can edit fader channels or use this block to use every single fader.
    if 1 <= event.data1 <= 5:
        mixer.setTrackVolume((event.data1 - 1), (event.data2 / 127) * 0.8)
        event.handled = True
