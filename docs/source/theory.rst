Theory of Operation
===================

References
----------

1. Moritz Klein, "Designing a white, pink & blue noise generator from scratch" [youtube](https://www.youtube.com/watch?v=0yB_h_wFkh4)
2. Ray Wilson, "Noise cornucopia rev-1" [MFOS](https://musicfromouterspace.com)
3. Eddy Bergman, "Synthesizer Build part-31: NOISE MODULE with 5 TYPES OF NOISE + Random Gates" [eddybergman.com][https://www.eddybergman.com/2020/05/synthesizer-build-part-31-noise-module.html)
4. Juraj Valsa and Jiri Vlach, "RC models of a constant phase element", *Intl. J. Circuit Th. and App.* **41** p59 (2013) [doi](https://doi.org/10.1002/cta.785)
5. Wikipedia contributors, "White noise," *Wikipedia, The Free Encyclopedia*, [wikipedia.org](https://en.wikipedia.org/wiki/White_noise)
6. Wikipedia contributors, "Colors of noise", *Wikipedia, The Free Encyclopedia*, [wikipedia.org](https://en.wikipedia.org/wiki/Colors_of_noise)

Noise Spectra
-------------

White noise is a random signal with a constant power spectral density and the same intensity at all frequencies. Consequently, there is an equal amount of power in a frequency interval, but an increasing amount of power in an octave: the noise power doubles when moving to the next octave.

Pink noise has a $1/f$ power spectral density (decreasing at 10dB/decade or 3.01dB/octave) such that equal power is contained in frequency intervals that are *proportionally* wide. Therefore, a pink noise signal has equal power in each octave. Blue noise is the opposite of pink noise: its power spectral density increases at 10dB/decade (3.01dB/octave). Completing the colored noise spectra are Brownian noise (or Brown noise), decreasing at 20dB/decade (i.e. a first order LPF applied to white noise) and violet/purple noise increasing at 20dB/decade (i.e. a first order HPF applied to white noise).

Transistor Noise
----------------



Fractional Order Filters
------------------------

A first order low pass filter (LPF) has a transfer function of the form
$$
H(s) = \frac{\omega_0}{s + \omega_0}
$$
As the frequency $s$ increases, for $s \gg \omega_0$, $H(10s) / H(s) \to 1/10$, which is equivalent to a slope of $-20dB/dec$ (in intensity units $20dB \equiv 10 \log |10|^2$). A first order LPF can be realized as an RC circuit whose transfer function is 
$$
H(j\omega)=\frac{1}{j\omega RC + 1}
$$
with $\omega_0 = 1/RC$.  The magnitude and phase of this transfer function are 
$$
\begin{align*}
|H(j\omega)| &= \frac{\omega_0}{\sqrt{\omega^2 + \omega_0^2}}\\
\angle H(j\omega)&= \tan^{-1}\left(-\frac{\omega}{\omega_0}\right)
\end{align*}
$$
Generally, the LPF can be written
$$
H(s)=\frac{\omega_0}{s^\alpha + \omega_0}
$$
 with magnitude
$$
|H(j\omega)|=\frac{\omega_0}{\sqrt{\omega^{2\alpha}+2\omega_0\cos(\alpha\pi/2)\omega^\alpha+\omega_0^2}}
$$
as $\omega \to \infty$ , $|H(j\omega)|\to \omega_0/\omega^\alpha$ such that the slope is
$$
20\log \left(\frac{\omega_0}{10^\alpha \omega^\alpha}\right)-20\log \left(\frac{\omega_0}{ \omega^\alpha}\right)=20 \log 10^{-\alpha} = -20\alpha
$$


### LPF with Fractional Capacitor

Circuit is a series R(CF), e.g. shelf filters
$$
\begin{align*}
Z_{CF}(j\omega)&=\frac{1}{\sqrt{j\omega\psi}}=\frac{1}{\sqrt{\omega\psi}(\cos \pi/4 + j \sin\pi/4)}=\frac{\sqrt{2}}{(1 + j)\sqrt{\omega\psi}}=\sqrt{\frac{1}{2\omega\psi}}(1-j)\\
\to H(j\omega) &= \frac{1}{R/Z_{CF}(j\omega) + 1} = \frac{1}{R\sqrt{\omega\psi}e^{j\pi/4} + 1} = \frac{1}{\sqrt{\omega / \omega'_0 }(1+j) + 1},\quad \omega'_0 = \frac{2}{R^2\psi}\\
|H(j\omega)| &= \left|\frac{1}{(1 + \sqrt{\omega/\omega'_0}) + j\sqrt{\omega/\omega'_0}} \right| = \left|\frac{(1 + \sqrt{\omega/\omega'_0}) - j\sqrt{\omega/\omega'_0}}{(1 + \sqrt{\omega/\omega'_0})^2 + \omega/\omega'_0}\right| = \left|\frac{(1+a)-ja}{1+2a + 2a^2}
\right| \\
&= \frac{1}{\sqrt{1+2a+2a^2}} \to 1 + 2a + 2a^2 = 2\to a^2 + a - 1/2 =0 \to a = \frac{-1+\sqrt{3}}{2}
\end{align*}
$$
 







* $\alpha = 1/2$
* show phase = $-\pi/4$
* Valsa design for $\phi_{av} = -\pi/4$, $\Delta \phi = \pm 2^o$? $\omega_{max}/\omega_{min} = 10^4$ and $\omega_{min} = 10Hz$  
  * $\omega_{min} = 10Hz \to R_1=15k, C_1=1u$ 
  * $ab=\frac{0.24}{1 +\Delta \phi}=0.06$ for $\Delta\phi =  3$ 
  * $\phi_{av}=45=\frac{90 \log a}{\log ab} \to \frac{\log 0.06}{2} = \log a \to a=0.245, b=0.245$
  * $m = 1 - \frac{log(\omega_{max}/\omega_{min})}{\log ab}=1-\frac{4}{-1.22} = 4$ 
  * $R_k = R_1a^{k-1}$ and $C_k=C_1b^{k-1}$
  * $R_p = R_1\frac{1-a}{a}$ and $C_p = C_1 \frac{b^m}{1-b}$



