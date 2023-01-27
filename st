aplay -l

echo which one do you think ?
read device 


fluidsynth --audio-driver=alsa -o audio.alsa.device=hw:$device /usr/share/sounds/sf2/FluidR3_GM.sf2
