---
layout: project
type: project
image: images/FRCLogo.png
title: First Robotics Competition
permalink: projects/project1.md
date: 2014-01-01 - 2017-05-01
labels:
  - Robotics
  - C++
  - Electrical
  - Systems
summary: A seasonal robotics competition driven by the engineering design process.
---
The First Robotics Competition is a seasonal robotics competition dedicated to providing students with a vehicle to help develop their life skills. This global neo-sport emphasizes not only the importance of the engineering design process but also self-confidence, communication, leadership, and most importantly gracious professionalism.

```js
byte ADCRead(byte ch)
{
    word value;
    ADC1SC1 = ch;
    while (ADC1SC1_COCO != 1)
    {   // wait until ADC conversion is completed   
    }
    return ADC1RL;  // lower 8-bit value out of 10-bit data from the ADC
}
```
For more information, visit the [First Robotics Competition website]. (https://www.firstinspires.org/about/vision-and-mission)
