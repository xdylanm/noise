# Assembly Guide

Step by step instructions for assembly

## Calibration

* Adjust RV1 to get 10Vpp at the white noise output (rare excursions above 10Vpp are likely OK).
* Adjust RV3 to balance the grain outputs between positive and negative spikes. In my experience biasing it towards 2/3 negative and 1/3 positive is good.

## BOM

[Download (.csv)](assets/bom.csv)

!!! Note

    All resistors are 5% tolerance. All capacitors are ceramic except for the 2 10uF decoupling capacitors (electrolytic). RV1 and RV3 are 6mm trim pots. 

!!! Note

    The collector lead of Q1 should be cut off at the case before installing.

{%include-markdown "assets/bom.md"%}
