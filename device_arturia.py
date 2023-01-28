# name=arturia

# imports
# location C:\Users\**username**\Documents\Image-Line\FL Studio\Settings\Hardware\yyCustom

import mixer
import ui
import transport
import channels
import mixer

# Control song variables
play_song = 36
reset_song = 37
rewind = 38
fast_forward = 39

# Show windows variables
show_mx = 40
show_pl = 41
show_ch = 42
show_pr = 43


def OnMidiMsg(event):

    event.handled = False
    channel_index = channels.selectedChannel()
    print(event.midiId, event.data1, event.data2)
    if event.data1 > 0:

        # Push Button
        if event.midiId == 144:
            
            # Control Transport
            
            # Toggle song play/pause            
            if event.data1 == play_song:
                transport.start()
                event.handled = True

            # Reset song           
            if event.data1 == reset_song:
                transport.stop()
                event.handled = True

            # Rewind song position          
            if event.data1 == rewind:
                if event.data2 > 0:
                    transport.rewind(2)
                else:
                    transport.start(0)

                event.handled = True

            # Forward song position          
            if event.data1 == fast_forward:
                if event.data2 > 0:
                    transport.fastForward(2)
                else:
                    transport.start(0)
                event.handled = True
            
            # Show mixer pannel
            if event.data1 == show_mx:
                if ui.getVisible(0) == 0:  # if window is not visible
                    ui.showWindow(0)  # make it visible
                    ui.setFocused(0)
                    event.handled = True
                else:
                    ui.hideWindow(0)  # if it is visible hide it
                    event.handled = True
            # Show channel pannel
            if event.data1 == show_ch:
                if ui.getVisible(1) == 0:
                    ui.showWindow(1)
                    event.handled = True
                else:
                    ui.hideWindow(1)
                    event.handled = True
                                        
            # Show playlist pannel
            if event.data1 == show_pl:
                if ui.getVisible(2) == 0:
                    ui.showWindow(2)
                    event.handled = True
                else:
                    ui.hideWindow(2)
                    event.handled = True
    
                # Show playlist pannel
            if event.data1 == show_pr:
                if ui.getVisible(3) == 0:
                    ui.showWindow(3)
                    event.handled = True
                else:
                    ui.hideWindow(3)
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
                    
                # Toggle mixer track slot 1
                if event.data1 == 20:
                    mixer.enableTrack(1)
                    event.handled = True
                # Toggle mixer track slot 2
                if event.data1 == 21:
                    mixer.enableTrack(2)
                    event.handled = True
                # Toggle mixer track slot 3
                if event.data1 == 22:
                    mixer.enableTrack(3)
                    event.handled = True
                # Toggle mixer track slot 4
                if event.data1 == 23:
                    mixer.enableTrack(4)
                    event.handled = True
                # Toggle mixer track slot 5
                if event.data1 == 24:
                    mixer.enableTrack(5)
                    event.handled = True
                # Toggle mixer track slot 6
                if event.data1 == 25:
                    mixer.enableTrack(6)
                    event.handled = True
                # Toggle mixer track slot 7
                if event.data1 == 26:
                    mixer.enableTrack(7)
                    event.handled = True
                # Toggle mixer track slot 8
                if event.data1 == 27:
                    mixer.enableTrack(8)
                    event.handled = True
                # Toggle mixer track slot 9
                if event.data1 == 28:
                    mixer.enableTrack(9)
                    event.handled = True
                # Toggle mixer track slot 10
                if event.data1 == 29:
                    mixer.enableTrack(10)
                    event.handled = True
                # Toggle mixer track slot 11
                if event.data1 == 30:
                    mixer.enableTrack(11)
                    event.handled = True
                # Toggle mixer track slot 12
                if event.data1 == 31:
                    mixer.enableTrack(12)
                    event.handled = True
                # Toggle mixer track slot 13
                if event.data1 == 41:
                    mixer.enableTrack(13)
                    event.handled = True
                # Toggle mixer track slot 14
                if event.data1 == 46:
                    mixer.enableTrack(14)
                    event.handled = True
                # Toggle mixer track slot 15
                if event.data1 == 47:
                    mixer.enableTrack(15)
                    event.handled = True
                # Toggle mixer track slot 16
                if event.data1 == 52:
                    mixer.enableTrack(16)
                    event.handled = True


def OnControlChange(event):
        # I have 5 faders. You can edit fader channels or use this block to use every single fader.
    if 1 <= event.data1 <= 5:
        mixer.setTrackVolume((event.data1 - 1), (event.data2 / 127) * 0.8)
        event.handled = True
