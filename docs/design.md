# Design Notes

## Transistor Biasing

In the MFOS design, the noise-generating transistor is biased through a
pair of 470k resistors with a 1uF decoupling capacitor to attenuate
power supply ripple. This isn't required for a low-noise supply: both
verions published by Klein and Bergman use a single R to +12V. There are
few choices published here ranging from 47k (YuSynth version) to 130k
(Eddy Bergman).

-   lower values result in larger amplitude noise outputs and less
    asymmetry between positive and negative peak voltages
-   the noise is AC coupled, so the time average tends to 0V

In the end, I stuck with 100k, which in my test gave a difference of
about 0.5V between the absolute value of the negative and positive peak
voltages (e.g. $V_{min}\simeq -0.5V$ to $V_{max}\simeq 1.0V$) in the
first gain stage.

![First stage white noise signal output](./assets/images/G1.png){: width="800"}

## Gain

The MKI design uses a single gain stage. This has the disadvantage of
amplifying the "DC offset." Although there's a high-pass filter
between the collector and the opamp (corner frequency $\sim 0.7\mathrm{Hz}$), a
slow-varying mean (est. $\pm 1mV$) is amplified. I chose a first stage
gain of $\sim 20$ ($R_f=470k\Omega$, $R_g=22k\Omega$) and see a mean that
fluctuates around $\pm 20mV$ for a $1.5 V_{pp}$ output. This would
increase to $> \pm 100mV$ if the first stage gain were increased to give
a 10Vpp signal.

Adding a second stage with a second high-pass filter improves the
offset, but doesn't eliminate it: a +60mV mean is measured for the
signal at the second stage output. The second stage transfer function
(assuming an ideal opamp)

$$\begin{aligned}
\frac{V_i j\omega C_1}{1 + j\omega R_1 C_1} &= \frac{V_o}{R_f} \\
\to \frac{V_o}{V_i} &= \frac{j\omega R_f C_1}{1 + j\omega R_1 C_1} \\
\to |H| &= \frac{R_f}{R_1}\frac{1}{\sqrt{1 + \frac{\omega_{c1}^2}{\omega^2}}}
\end{aligned}$$

gives the corner frequency defined by the product
$\omega_{c1} = \frac{1}{R_1 C_1}$ and a gain of $\frac{R_f}{R_1}$.
Increasing $R_1$ and $C_1$ reduces the high-pass corner. Increasing
$R_f$ compensates for increasing $R_1$.

The gain used in the MFOS design to bring the white noise to
approximately 10Vpp seems to be too large as given in the schematic. To
fix this and also reduce the high-pass effect in the second stage,

-   Reduce the first stage gain to $~20$ ($R_f = 470k$, $R_n = 22k$)
-   Increase the block capacitor from 100n to 1u ($C_1$ in the high-pass
    circuit)
-   Increase the input resistor to the second stage opamp ($R_1$ in the
    high-pass circuit) from 10k to 22k
-   With that change, keep the trim pot in the second stage opamp
    feedback at 470k and adjust to obtain 10Vpp

*Aside:* this appears in Eddy Bergmans's notes, too. He suggests
reducing the range of the trim pot.

As described in the MFOS design ($R_1=10k$ and $C_1=100n$), the second
stage high-pass has a corner around 160Hz:

![Second stage 160Hz corner](./assets/images/G2_0U1.png){: width="800"}

Changing the high-pass and gain moves this corner below 10Hz:

![Second stage 8Hz corner](./assets/images/G2_1ULF.png){: width="800"}

The signal has a 10Vpp range with a 70mV mean and a bias of -1.5V
(negative peaks -5.5V, positive peaks 4.0V).

## Filters

In the MFOS-inspired designs, a first order LPF (20dB/dec., 6dB/oct.) is
used to generate low-pass noise. The YuSynth version and the design from
MKI both use a "shelf" filter with 3 poles to approximate a 10dB/dec.
(3dB/oct.) slope, which is characteristic of [pink
noise](https://en.wikipedia.org/wiki/Colors_of_noise#Pink_noise).

There are a few references on fractional filter design, including
Valsa2013, that give a procedure for generating R and C values. Using
that as a guide (see details in the [fractional filter theory](./theory.md) 
section and associated [notebook](./freq_resp.ipynb)), I implement a similar
-10dB/dec. filter to the YuSynth and MKI designs, using a 60Hz corner
frequency. In the figure below, I compare

-   the ideal fractional filter response (-10dB/dec)
-   the simulated response for the filter using Valsa's method to
    generate a fractional capacitor
-   the measured response of the filter to a frequency-swept sine input
-   the measured spectrum of the filtered noise

The implemented filter leaves out the additional R & C that Valsa
defines to improve the phase response and force roll-off at high
frequencies, so the topology is the same as the usual approximations
with three branches.

![Fractional LPF design and measurement.](./assets/images/PN_filter_response.png){: width="800"}

The measurement of the filtered noise was done on the buffered output of
the filter (unity gain), so an offset is applied in the figure above to
align the curves. In the implementation, the same gain as in MKI's
design is used to restore the pink noise to approximately 10Vpp. The
measured pink noise is an average of 50 traces, and the scope's
(Siglent SDS-1104X-E) FFT is used to generate the spectrum, which was
then digitized using [WebPlotDigitizer](https://apps.automeris.io/wpd4/)
to extract the values from the image.

![Pink noise measurement](./assets/images/PN.png){: width="800"}

For the blue noise, the elements of the LPF are exchanged to implement a
fractional HPF (FHPF) with approximately 10dB/dec of slope and a corner
frequency of approximately 40kHz. To adjust the corner frequency, it's
easiest just to change the resistor and compensate with gain in the
output buffer. The design response and measured noise spectrum are
plotted below (amplitudes are adjusted to give a visual fit).

![Fractional HPF design and measurement.](./assets/images/BN_filter_response.png){: width="800"}

## Grainy Noise

This is a great feature from the Noise Cornucopia (MFOS), but is quite
sensitive. It seems to naturally have a bias towards negative pulses,
with positive pulses only kicking in with the control near maximum (as
both thresholds approach 0V). This is used in the MFOS design to reduce
the rate of triggering for random gates. The sign of the pulse does not
have an audible impact.

-   Add a trim pot to set the balance between the negative and positive
    threshold.
    -   This works well, but requires a scope and tuning is sensitive.
    -   This may be useful if the positive pulses are specifically
        required (e.g. positive edge to trigger or sync on).
-   Tried an LM393 comparator
    -   Even with threshold adjustment, this never gave an even
        distribution of positive and negative pulses.
    -   It is much more sensitive and almost always generates negative
        pulses with the default max/min thresholds. Need to increase the
        maximum thresholds (reduce the size of the tail resistors to
        e.g. 22k) to enable turning off the grains.
-   Tuning with the 100k graininess control pot is very sensitive (TL07x
    as comparator; in parallel with 220k)
    -   it has a large deadband (0-80% of the range does nothing): the
        TL07x doesn't trip for offsets above about 2V
    -   it goes from a few ticks to dense static in a very small range
        (a few %)

To address the last behaviour, I reduce the bridging resistor to 100k.
Ideally, with the control pot at maximum, $R_{eq} = 100k || 100k = 50k$.
For thresholds $V_{thr,+} > 2V$ and $V_{thr,-} < -2V$, the comparator is
not triggered (even though the input voltage from the random noise
signal goes above and below these thresholds). Increasing the biasing
resistors to 120k sets the maximum threshold to approximately $\pm 2V$.
This results in more range and less sensitivity for the control pot.



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
6.  Juraj Valsa and Jiri Vlach, "RC models of a constant phase
    element," *Intl. J. Circuit Th. and App.* **41** p59 (2013)
    [doi](https://doi.org/10.1002/cta.785)
