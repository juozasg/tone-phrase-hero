

## Linux virtual MIDI device setup

create a file in `/etc/modules-load.d` called `snd-virmidi.conf`
```
# enable virtual midi at boot
snd-virmidi
```

create `/etc/modprobe.d/snd-virmidi.conf`
```
options snd-virmidi enable=1 midi_devs=1
```