# Random Noise

![Faceplate](./assets/images/faceplate-dark.png#only-dark){: width="64", align=right}
![Faceplate](./assets/images/faceplate-light.png#only-light){: width="64", align=right}

Sources of white and coloured random noise based on Ray Wilson's [Noise Cornucopia](https://musicfromouterspace.com/analogsynth_new/NOISECORNREV01/NOISECORNREV01.php). 

* Module size: 4HP (20mm)
* Power: 10mA (+12V); 2mA (-12V)

!!! repository "Project Source"

    The project files, including schematic and layout, are available on [github](https://github.com/xdylanm/noise).

## Features

Random noise is a signal source module with multiple line-level audio outputs:

* White noise between 10Hz and 10kHz+ with a 10Vpp output
* Pink noise (10dB/dec fractional LPF) with 60Hz corner
* Blue noise (10dB/dec fractional HPF) with 10kHz corner* 
* Grains output with threshold control

The grains output consists of random positive and negative impulses, creating a static sound.

## Documentation

* [Design](design.md)
* [Assembly Guide](assembly.md)
* [Schematic](assets/schematic.pdf)

## References

1.  Ray Wilson, "Noise Cornucopia"
    [musicfromouterspace.com](https://musicfromouterspace.com/analogsynth_new/NOISECORNREV01/NOISECORNREV01.php)
2.  Eddy Bergman, "Synthesizer Build part-31: NOISE MODULE with 5 TYPES
    OF NOISE + Random Gates"
    [eddybergman.com](https://www.eddybergman.com/2020/05/synthesizer-build-part-31-noise-module.html)
3.  Moritz Klein, "Designing a white, pink & blue noise generator from
    scratch" [youtube.com](https://www.youtube.com/watch?v=0yB_h_wFkh4)
4.  Yves Usson, "Noise generator / Sample & Hold"
    [YuSynth](http://yusynth.net/Modular/EN/NOISE/index.html)
5.  Rene Schmitz, "White Noise Source"
    [schmitzbits.de](https://schmitzbits.de/noise.html)



