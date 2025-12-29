# Assembly Guide

!!! Note

    The collector lead of Q1 should be cut off at the case before installing.

* Diodes D3 & D4
* Horizontal resistors R1 (or ferrite), R16, R27, R28, & R30
* Sockets for U1 & U2
* Ceramic capacitors: C3-C5, C9-C11, C17-C22 (no C15 or C16)
* BJT Q1 - ensure collector lead is cut
* Trim pots RV1 & RV3
* Film capacitors for the filter network: C6-C8 & C12-C14
* Remaining resistors (R2 may be a ferrite to match R1 if desired; no R12 or R23)
* IDC header J1
* Mono jacks J2-J6
* Grain potentiometer RV2

As a final step, attach the faceplate.

## Calibration

* Adjust RV1 to get 10Vpp at the white noise output (rare excursions above 10Vpp are likely OK).
* Adjust RV3 to balance the grain outputs between positive and negative spikes. In my experience biasing it towards 2/3 negative and 1/3 positive is good.

## BOM

[Download (.csv)](assets/bom.csv)

!!! Note

    All resistors are 5% tolerance. All capacitors are ceramic except for the 2 10uF decoupling capacitors (electrolytic). RV1 and RV3 are 6mm trim pots. 

{%include-markdown "assets/bom.md"%}
