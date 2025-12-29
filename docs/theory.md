# Noise and Filter Theory

## Noise Spectra

### References

1. Wikipedia contributors, "White noise," *Wikipedia, The Free Encyclopedia*, [wikipedia.org](https://en.wikipedia.org/wiki/White_noise)
2. Wikipedia contributors, "Colors of noise", *Wikipedia, The Free Encyclopedia*, [wikipedia.org](https://en.wikipedia.org/wiki/Colors_of_noise)

### White Noise

White noise is a random signal with a constant power spectral density and the same intensity at all frequencies. Consequently, there is an equal amount of power in a frequency interval, but an increasing amount of power in an octave: the noise power doubles when moving to the next octave.

### Coloured Noise

Pink noise has a $1/f$ power spectral density (decreasing at 10dB/decade or 3.01dB/octave) such that equal power is contained in frequency intervals that are *proportionally* wide. Therefore, a pink noise signal has equal power in each octave. Blue noise is the opposite of pink noise: its power spectral density increases at 10dB/decade (3.01dB/octave). Completing the colored noise spectra are Brownian noise (or Brown noise), decreasing at 20dB/decade (i.e. a first order LPF applied to white noise) and violet/purple noise increasing at 20dB/decade (i.e. a first order HPF applied to white noise).

## Fractional Order Filters

### References

1. <a name="Valsa2013"></a>Juraj Valsa and Jiri Vlach, "RC models of a constant phase element," *Intl. J. Circuit Th. and App.* **41** p59 (2013) [doi](https://doi.org/10.1002/cta.785)
2. <a name="Said2018"></a>Lobna Said, et al., "Fractional-Order Filter Design," p358 [doi](https://doi.org/10.1016/B978-0-12-816152-4.00012-1)

### Low Pass Filter

A first order low pass filter (LPF) has a transfer function of the form

$$
H(s) = \frac{\omega_0}{s + \omega_0} = \frac{1}{s/\omega_0 + 1}
$$

As the frequency $s$ increases, for $s \gg \omega_0$, $H(10s) / H(s) \to 1/10$, which is equivalent to a slope of $-20dB/dec$ (in intensity units $20dB \equiv 10 \log |10|^2 = 20\log |10|$). A first order LPF can be realized as an RC circuit whose transfer function is 

$$
H(j\omega)=\frac{1}{j\omega RC + 1}
$$

substituting $s\to j\omega$ with $\omega_0 = 1/RC$.  The magnitude and phase of this transfer function are 

$$
\begin{align*}
|H(j\omega)| &= \frac{\omega_0}{\sqrt{\omega^2 + \omega_0^2}}\\
\angle H(j\omega)&= \tan^{-1}\left(-\frac{\omega}{\omega_0}\right)
\end{align*}
$$

Generally, the LPF can be written ([Said2018](#Said2018))

$$
H(s)=\frac{\omega_0}{s^\alpha + \omega_0} = \frac{1}{(s / \omega^{1/\alpha}_0)^\alpha + 1} 
$$

with magnitude

$$
|H(j\omega)|=\frac{\omega_0}{\sqrt{\omega^{2\alpha}+2\omega_0\cos(\alpha\pi/2)\omega^\alpha+\omega_0^2}}
$$

as $\omega \to \infty$ , $|H(j\omega)|\to \omega_0/\omega^\alpha$ such that the slope is

$$
20\log \left(\frac{\omega_0}{10^\alpha \omega^\alpha}\right)-20\log \left(\frac{\omega_0}{ \omega^\alpha}\right)=20 \log 10^{-\alpha} = -20\alpha
$$

To obtain a slope of $-10dB/dec$ ($-3dB/oct$), $\alpha = 1/2$ and 

$$
H(s) = \frac{1}{\sqrt{s/\omega^2_0} + 1}
$$

The general corner frequency is found when 

$$
\begin{align*}
\frac{1}{\sqrt{2}} = |H(j\omega)| &= \frac{1}{\sqrt{\frac{\omega^{2\alpha}}{\omega_0^2}+2\cos(\alpha\pi/2)\frac{\omega^\alpha}{\omega_0}+1}} \\
\to 2 &= \frac{\omega^{2\alpha}}{\omega_0^2} + 2\cos(\alpha\pi/2)\frac{\omega^\alpha}{\omega_0} + 1 \\
\to 0 &= \omega^{2\alpha} + 2\cos(\alpha\pi/2)\omega_0 \omega^\alpha  - \omega_0^2 \\
\to \omega^{\alpha} &= -\cos(\alpha\pi/2)\omega_0 \pm \frac{1}{2}\sqrt{\cos^2(\alpha\pi/2)\omega^2_0 + 4\omega^2_0} \\
&= \left[-\cos(\alpha\pi/2) + \frac{1}{2}\sqrt{\cos^2(\alpha\pi/2) + 4}\right]\omega_0\\
\to \omega_c &= \left[-\cos(\alpha\pi/2) + \frac{1}{2}\sqrt{\cos^2(\alpha\pi/2) + 4}\right]^{-\alpha}\omega_0^{-\alpha}
\end{align*}
$$

### Fractional Capacitor

To obtain an impedance proportional to $1/\sqrt{j\omega}$, define $Z_{CF}(j\omega)$ as 

$$
\begin{align*}
Z_{CF}(j\omega)&\equiv\frac{\psi}{\sqrt{j\omega}}=\frac{\psi}{\sqrt{\omega}(\cos \pi/4 + j \sin\pi/4)}=\frac{\psi\sqrt{2}}{(1 + j)\sqrt{\omega}}=\psi\sqrt{\frac{1}{2\omega}}(1-j)
\end{align*}
$$

### Fractional Low Pass Filter
In series with a resistor $R$ (and output across $Z_{CF}$), the transfer function becomes

$$
\begin{align*}
\to H(j\omega) &= \frac{1}{R/Z_{CF}(j\omega) + 1} = \frac{1}{\frac{R\sqrt{\omega}}{\psi}e^{j\pi/4} + 1} = \frac{1}{\sqrt{\omega / \omega'_0 }(1+j) + 1}\\
\sqrt{\frac{\omega}{\omega'_0} }(1+j) &= \frac{R}{\psi\sqrt{2}}(1 + j)\sqrt{\omega} \to \omega'_0 = \frac{2\psi^2}{R^2}
\end{align*}
$$

This yields the location of the corner frequency ($|H(j\omega_0)| = 1/\sqrt{2}$):

$$
\begin{align*}
|H(j\omega)| &= \left|\frac{1}{(1 + \sqrt{\omega/\omega'_0}) + j\sqrt{\omega/\omega'_0}} \right|
\to \left| (1 + \underbrace{\sqrt{\omega/\omega'_0}}_a) + j\sqrt{\omega/\omega'_0}\right| = \sqrt{2} \\
\to |(1 + a) + ja|^2 &= [(1+a) + ja][(1+a) - ja] = 1 + 2a + 2a^2 = 2 \\
\to a^2 + a - 1/2 &=0 \to a = \sqrt{\frac{\omega}{\omega'_0}} = \frac{-1+\sqrt{3}}{2} \\
\to \omega_0 &= \left(\frac{-1+\sqrt{3}}{2}\right)^2\omega'_0 = \left(\frac{-1+\sqrt{3}}{2}\right)^2\frac{2\psi^2}{R^2}
\end{align*}
$$

Given a target $\omega_0$ and one of $R$ or $\psi$, the other impedance can be chosen. 

### Fractional High Pass Filter
In series with a resistor $R$ (and output across $R$), the transfer function becomes

$$
\begin{align*}
\to H(j\omega) &= \frac{R/Z_{CF}(j\omega)}{R / Z_{CF}(j\omega)  + 1} = \frac{\sqrt{\omega / \omega'_0 }(1+j)}{\sqrt{\omega / \omega'_0 }(1+j) + 1},\quad \omega'_0 = \frac{2\psi^2}{R^2}
\end{align*}
$$

as above. The corner frequency ($|H(j\omega_0)| = 1/\sqrt{2}$) is then

$$
\begin{align*}
\frac{1}{\sqrt{2}} = \left|H(\omega_c)\right| &= \left| \frac{\sqrt{\omega_c / \omega'_0 }(1+j)}{\sqrt{\omega_c / \omega'_0 }(1+j) + 1}\right| \\
\to \sqrt{2} &= \left|1 + \frac{1}{\sqrt{\omega_c / \omega'_0 }(1+j)}\right| =\left|1 + \frac{1-j}{2\sqrt{\omega_c / \omega'_0 }}\right| \\
&= \left|\frac{(1+2\sqrt{\omega_c / \omega'_0 }) - j}{2\sqrt{\omega_c / \omega'_0 }}\right| = \left|\frac{(1+2a) - j}{2a}\right| \\
&= \sqrt{\left(1 + \frac{1}{2a}\right)^2 + \left(\frac{1}{2a}\right)^2} \\
\to b \equiv \frac{1}{2a},\quad 2&= (1+b)^2 + b^2 \to 0 = 2b^2 + 2b - 1 \to b = \frac{-1+\sqrt{3}}{2} \\
\to a = \sqrt{\omega_c / \omega'_0 } &= \frac{1}{-1 + \sqrt{3}} \to \omega_c = \left(\frac{1}{-1 + \sqrt{3}}\right)^2\frac{2\psi^2}{R^2}
\end{align*}
$$

### Filter Approximation

Details on the filter implementation are in the [notebook](./freq_resp.ipynb), including an implementation of the method described in [Valsa2013](#Valsa2013). Effectively, Valsa's method generates a similar structure to the shelf-filter approximation with an extra low-pass pole at a higher frequency (at the expense of an extra RC pair). After some simulations and testing, I chose to keep the shelf-filter approximation.



