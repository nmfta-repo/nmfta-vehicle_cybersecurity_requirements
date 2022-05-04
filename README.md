# NMFTA Heavy Duty Vehicle Cybersecurity Requirements (HDVCR)

Cybersecurity requirements for heavy duty vehicles developed in collaboration with motor freight carriers, OEMs and cybersecurity experts.

The cybersecurity requirements captured here are for use by fleets to include in their procurement process with OEMs. The requirements are intended to cover the following truck body configurations, which we intend to cover most of what LTL carriers need:
* North America "on highway" Class 7-8 trucks e.g. the classic truck w/ trailer or double as the  most common configuration
* and also the last mile delivery truck with a dry freight truck body that could include a lift gate


## How to Use the HD VCR

We recommend that fleets use these requirements by following some steps during the procurement process. We are open to feedback on how to improve the requirements and the process.

1. Fleets should ask OEMs to identify all the modules in the requested truck by the *Device Classes* below.
2. Fleets should prepare questionnaires to be completed by the OEMs based on the classes found.
3. OEMs complete the questionnaires, answering in the affirmative if all devices of the given class satisfy the requirement. Deviations and rationale can be noted in the provided cells of the questionnaires.


## Device Classes

The VCRWG analyzed several truck vehicle network architectures and performed a risk analysis to classify the known truck electronic components into a series of device classes. The cybersecurity requirements for procurement are assigned to these classes. Each device identified, its assigned class and the rationale for assigning that class are captured here in a truck order sheet view for ease of use by the fleets. This is also available in a word docx file here: [`resources/Truck_Component_Order_Sheet_Breakdown_for_Cybersecurity_Matrix_v0_DIST.docx`](resources/Truck_Component_Order_Sheet_Breakdown_for_Cybersecurity_Matrix_v0_DIST.docx).

> ENGINE

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------- |
| Engine Telematics (J1939 SA 249)                                                                                             | **0**                                | telematics device                   |
| Engine \#1 (aka Motor Control Module (MCM) / Engine Management System (EMS) / Engine Control Module (ECM)) (J1939 SA 00, 01) | **3**                                | medium total risk                   |
| Engine Cylinder Pressure Monitoring System                                                                                   | **3**                                | medium total risk                   |
| Engine \#2                                                                                                                   | **None** **Specified**               | no responses / not common component |

> ENGINE EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------- |
| Ignition Control Module \#2 (J1939 SA 57)                                                                                   | **2**              | large scope change risk                                     |
| Low-Voltage Disconnect (J1939 SA 49)                                                                                        | **2**              | large scope change risk                                     |
| Starter System (J1939 SA 00, 03)                                                                                            | **2**              | large scope change risk                                     |
| Thermal Management System Controller (J1939 SA 49)                                                                          | **2**              | large scope change risk                                     |
| Water Pump Controller (J1939 SA 57)                                                                                         | **2**              | large scope change risk                                     |
| Fuel Heater, In-Tank (J1939 SA 72)                                                                                          | **2**              | large scope change risk                                     |
| Oil Sensor (J1939 SA 00)                                                                                                    | **2**              | large scope change, safety, financial and operational risks |
| Engine Valve Controller (J1939 SA 0)                                                                                        | **3**              | medium operational risk                                     |
| Propulsion Battery Charger (J1939 SA 73)                                                                                    | **3**              | medium operational risk                                     |
| Retarder, Exhaust, Engine \#1                                                                                               | **3**              | medium operational and safety risks                         |
| Retarder, Exhaust, Engine \#2                                                                                               | **3**              | medium operational and safety risks                         |
| Aftertreatment \#1 system gas intake (J1939 SA 81)                                                                          | **3**              | medium total risk                                           |
| Aftertreatment \#2 system gas intake (J1939 SA 86)                                                                          | **3**              | medium total risk                                           |
| Diesel Particulate Filter Controller (aka Aftertreatment Control Module (ACM) / Exhaust Emission Controller) (J1939 SA 211) | **3**              | medium total risk                                           |
| Engine Exhaust Backpressure (J1939 SA 34)                                                                                   | **3**              | medium total risk                                           |
| Fan Drive Controller (aka Fan Hub) (J1939 SA 78)                                                                            | **3**              | medium total risk                                           |
| Idle Control System (J1939 SA 68)                                                                                           | **3**              | medium total risk                                           |
| Powertrain Control Module (aka Common Powertrain Controller Module (CPC)) (J1939 SA 90)                                     | **3**              | medium total risk                                           |
| Retarder - Engine (J1939 SA 15)                                                                                             | **3**              | medium total risk                                           |
| Radiator (aka Radiator Fan Control) (J1939 SA 78, 00, 255)                                                                  | **3**              | medium total risk                                           |
| Oil Pan Heater (J1939 SA 00)                                                                                                | **3**              | medium total risk                                           |
| Engine Injection Control Module (J1939 SA 00)                                                                               | **4**              | low total risk                                              |
| Aftertreatment \#1 system gas outlet (aka NoX Sensors ) (J1939 SA 82)                                                       | **5**              | min total risk                                              |
| Aftertreatment \#2 system gas outlet (J1939 SA 87)                                                                          | **5**              | min total risk                                              |
| Alternator/Electrical Charging System                                                                                       | **5**              | min total risk                                              |
| Battery Charger                                                                                                             | **5**              | min total risk                                              |
| Battery Pack Monitor \#1 (J1939 SA 243)                                                                                     | **5**              | min total risk                                              |
| Catalyst Fluid Sensor (aka DEF Quality Sensor) (J1939 SA 211)                                                               | **5**              | min total risk                                              |
| Engine Exhaust Gas Recirculation (J1939 SA 70)                                                                              | **5**              | min total risk                                              |
| Ignition Control Module \#1 (J1939 SA 52)                                                                                   | **5**              | min total risk                                              |
| Turbocharger (J1939 SA 02)                                                                                                  | **5**              | min total risk                                              |
| Turbocharger Compressor Bypass (J1939 SA 02)                                                                                | **5**              | min total risk                                              |
| Turbocharger Wastegate (J1939 SA 02)                                                                                        | **5**              | min total risk                                              |
| Air Intake System (J1939 SA 70)                                                                                             | **5**              | min total risk                                              |
| Filtration Control                                                                                                          | **5**              | min total risk                                              |
| Exhaust Emission Controller (J1939 SA 61)                                                                                   | **None Specified** | no responses / not common component                         |
| Air Compressor                                                                                                              | **None Specified** | no responses / not common component                         |

> TRANSMISSION

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------------------------------------- | ----- | -------------------------------------------------------------- |
| Transmission Telematics                                                | **0** | telematics device                                              |
| Clutch/Converter Unit (J1939 SA 78)                                    | **3** | high enough severy independent of low overal risk              |
| Power TakeOff - (Main or Rear) (J1939 SA 07)                           | **3** | medium total risk                                              |
| Power TakeOff (Front or Secondary) (J1939 SA 07)                       | **3** | large operational risk and directly connected to several ports |
| Retarder - Driveline (J1939 SA 16)                                     | **3** | medium total risk                                              |
| Transmission \#1 (aka Transmission Control Module (TCM)) (J1939 SA 03) | **3** | medium total risk                                              |
| Transmission \#2 (aka Auxiliary Transmission) (J1939 SA 16)            | **3** | high enough severy independent of low overal risk              |
| Electronic Clutch Actuator (J1939 SA 03)                               | **3** | medium total risk                                              |

> FRONT AXLE & EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------- |
| Steering Input Unit (aka Steering Angle Sensor (SAS))                                                                                    | **2**              | large operational risk              |
| Steering Controller (aka Front Axle Steering (FAS) / VDS / MCS) (J1939 SA 19)                                                            | **3**              | medium safety risk                  |
| Suspension - Steer Axle (aka Electronically Controlled Suspension (ECS) / Electronically Controlled Air Suspension (ECAS)) (J1939 SA 20) | **3**              | medium total risk                   |
| Suspension - System Controller \#1 (J1939 SA 47)                                                                                         | **3**              | medium total risk                   |
| Axle - Steering (J1939 SA 08)                                                                                                            | **5**              | min total risk                      |
| Brakes - Steer Axle (J1939 SA 13)                                                                                                        | **None Specified** | no responses / not common component |
| Suspension - System Controller \#2 (J1939 SA 64)                                                                                         | **None Specified** | no responses / not common component |

> REAR AXLE & EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------------------- | ------------------ | ----------------------------------- |
| Differential Lock Controller (J1939 SA 138, 72, 39 ) | **2**              | large scope change risk             |
| Antilock Brake System (ABS) (J1939 SA 11)            | **2**              | large scope change risk             |
| Traction Control (J1939 SA 138, 39)                  | **2**              | large scope change risk             |
| Axle - Drive \#1 (J1939 SA 09)                       | **4**              | low total risk                      |
| Axle - Drive \#2 (J1939 SA 10)                       | **4**              | low total risk                      |
| Brakes - Drive axle \#1 (J1939 SA 13)                | **5**              | min total risk                      |
| Brakes - Drive Axle \#2 (J1939 SA 14)                | **5**              | min total risk                      |
| Electric Propulsion Control Unit \#1                 | **5**              | min total risk                      |
| Electric Propulsion Control Unit \#2                 | **None Specified** | no responses / not common component |
| Electric Propulsion Control Unit \#4                 | **None Specified** | no responses / not common component |
| Endurance Braking System                             | **None Specified** | no responses / not common component |

> ADDITIONAL AXLES

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------- | ----- | ------------------ |
| Lift Axle (J1939 SA 138, 71) | **3** | medium safety risk |

> REAR SUSPENSION

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| -------------------------------------------------- | ----- | ----------------------- |
| Suspension - Drive Axle \#1 (J1939 SA 138, 72, 39) | **2** | large scope change risk |
| Suspension - Drive Axle \#2 (J1939 SA 22)          | **2** | large scope change risk |
| Vehicle Dynamic Stability Controller (J1939 SA 62) | **3** | medium total risk       |

> TRAILER CONNECTIONS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| --------------------------------------------- | ----- | ----------------------- |
| Tractor/Trailer Bridge \#2 (J1939 SA 138, 39) | **2** | large scope change risk |
| Tractor-Trailer Bridge \#1 (J1939 SA 32)      | **2** | large scope change risk |

> TIRES & WHEELS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ----------------------------------------------------------------------------------- | ----- | ----------------------- |
| Tire Pressure Controller (aka Tire Pressure Monitoring System (TPMS)) (J1939 SA 51) | **2** | large scope change risk |
| Wheel End Monitoring                                                                | **2** | large scope change risk |

> FRAME & EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------- |
| Body-to-Vehicle Interface Control (aka VECU - Vehicle ECU) (J1939 SA 33)                                                                                                                                               | **2**              | large scope change risk             |
| Fifth Wheel Smart System (J1939 SA 138, 39)                                                                                                                                                                            | **2**              | large scope change risk             |
| Forward Road Image Processor (J1939 SA 232)                                                                                                                                                                            | **2**              | large scope change risk             |
| ADAS Lane Keep (aka LCS Side Sensor (blind spot only) / Lane Warning / Lane Departure Warning System / Bendix Fusion / Exterior Camera for Lane Departune Warning / Driver Assistance Camera (MPC)) (J1939 SA 232, 19) | **2**              | large scope change risk             |
| Automated Driving (L0-L2) (aka Bendix FLR and FLC (Forward looking Camera / Radar))                                                                                                                                    | **3**              | medium safety risk                  |
| Collision Avoidance (J1939 SA 42)                                                                                                                                                                                      | **3**              | medium total risk                   |
| Personnel Detection Device (aka Pedestrian Detection)                                                                                                                                                                  | **5**              | min total risk                      |
| Slope Sensor (aka Hill Start Assist)                                                                                                                                                                                   | **5**              | min total risk                      |
| Aerodynamic Control (J1939 SA 27)                                                                                                                                                                                      | **None Specified** | no responses / not common component |
| Electrical System (J1939 SA 30)                                                                                                                                                                                        | **None Specified** | no responses / not common component |
| Hitch Control (J1939 SA 35)                                                                                                                                                                                            | **None Specified** | no responses / not common component |
| Power Systems Manager (J1939 SA 91)                                                                                                                                                                                    | **None Specified** | no responses / not common component |

> FUEL TANK & EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| --------------------------- | ------------------ | ------------------------------------------------ |
| Fuel Actuator (J1939 SA 15) | **3**              | scope change high independent of low overal risk |
| Fuel System (J1939 SA 18)   | **None Specified** | no responses / not common component              |

> CAB EXTERIOR

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ---------------------------------------- | ------------------ | ------------------------------------------------- |
| Exterior Camera Telematics               | **0**              | telematics device                                 |
| Body Controller (aka Key-Lock Options)   | **3**              | high enough severy independent of low overal risk |
| Mirrors (J1939 SA 40)                    | **4**              | medium scope change risk                          |
| Body Controller \#2                      | **5**              | min total risk                                    |
| Door Controller (J1939 SA 236)           | **5**              | min total risk                                    |
| Door Controller \#1 (J1939 SA 237)       | **5**              | min total risk                                    |
| Door Controller \#2                      | **5**              | min total risk                                    |
| Door Controller \#3                      | **5**              | min total risk                                    |
| Door Controller \#4                      | **5**              | min total risk                                    |
| Roadway Information                      | **5**              | min total risk                                    |
| Vehicle Security (J1939 SA 29)           | **5**              | min total risk                                    |
| Forensic Exterior Cameras (J1939 SA 232) | **None Specified** | no responses / not common component               |

> CAB INTERIOR

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| --------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------- |
| Interior Camera Telematics                                                                                            | **0**              | telematics device                   |
| Cab Controller - Primary (aka SAM CAB) (J1939 SA 49)                                                                  | **2**              | large scope change risk             |
| Cab Controller - Secondary (J1939 SA 50)                                                                              | **2**              | large scope change risk             |
| Cruise Control (J1939 SA 17)                                                                                          | **2**              | large scope change risk             |
| Object Detection Display (aka Active Safety Components / Bendix Fusion (Display))                                     | **2**              | large scope change risk             |
| Safety Restraint System (SRS) (J1939 SA 83)                                                                           | **3**              | medium safety risk                  |
| Throttle (J1939 SA 0)                                                                                                 | **3**              | medium safety risk                  |
| Vehicle Navigation (J1939 SA 84)                                                                                      | **3**              | medium safety risk                  |
| Power TakeOff (PTO) Switches (J1939 SA 07)                                                                            | **3**              | medium total risk                   |
| Lighting - Operator Controls (J1939 SA 71)                                                                            | **4**              | medium scope change risk            |
| Transmission Display - Primary (J1939 SA 59)                                                                          | **4**              | low total risk                      |
| Trip Recorder (J1939 SA 24)                                                                                           | **4**              | low total risk                      |
| Switch Field (aka Additional Switches / Modular Switch Field (MSF)) (J1939 SA 138)                                    | **4**              | medium scope change risk            |
| Cab Display \#1                                                                                                       | **5**              | min total risk                      |
| Passenger-Operator Climate Control \#1 (aka LECM (Living Environment Control Module) / HVAC / HVAC FCU) (J1939 SA 25) | **5**              | min total risk                      |
| Passenger-Operator Climate Control \#2 (aka HVAC \#2 / HVAC ACU)                                                      | **5**              | min total risk                      |
| Retarder Display (J1939 SA 23)                                                                                        | **5**              | low total risk                      |
| Seat Control \#1                                                                                                      | **5**              | min total risk                      |
| Shift Console - Primary (aka Gearshift ECU) (J1939 SA 05)                                                             | **5**              | low total risk                      |
| Shift Console - Secondary (J1939 SA 06)                                                                               | **5**              | min total risk                      |
| Steering Column Unit (aka Turn Signal Control)                                                                        | **5**              | min total risk                      |
| Transmission Display - Secondary (J1939 SA 60)                                                                        | **5**              | min total risk                      |
| Radio (aka Head Unit / Infotainment) (J1939 SA 76, 84)                                                                | **5**              | low total risk                      |
| Steering Wheel Switches (J1939 SA 77)                                                                                 | **5**              | low total risk                      |
| Cab Display \#2                                                                                                       | **None Specified** | no responses / not common component |
| Driver Impairment Device (J1939 SA 94)                                                                                | **None Specified** | no responses / not common component |
| On-board axle group display                                                                                           | **None Specified** | no responses / not common component |
| On-board axle group scale                                                                                             | **None Specified** | no responses / not common component |
| Safety Restraint System \#2 (aka Seat SRS)                                                                            | **None Specified** | no responses / not common component |
| Seat Control \#2                                                                                                      | **None Specified** | no responses / not common component |
| Tachograph                                                                                                            | **None Specified** | no responses / not common component |
| User Interface System                                                                                                 | **None Specified** | no responses / not common component |
| Virtual Terminal                                                                                                      | **None Specified** | no responses / not common component |
| Interior Cameras                                                                                                      | **None Specified** | no responses / not common component |

> INSTRUMENTS & CONTROLS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| -------------------------------------------------------------- | ------------------ | ----------------------------------- |
| ADAS Adaptive Cruise Control (aka Bendix Fusion) (J1939 SA 42) | **2**              | large scope change risk             |
| Ammeter (J1939 SA 23, 39)                                      | **2**              | large scope change risk             |
| Headway Controller (J1939 SA 42)                               | **3**              | medium safety risk                  |
| Instrument Cluster \#1 (aka Gauges) (J1939 SA 23)              | **4**              | medium scope change risk            |
| Engine Display                                                 | **4**              | low total risk                      |
| Pyrometer                                                      | **5**              | low total risk                      |
| Instrument Cluster \#2 (aka Auxiliary Gauges)                  | **None Specified** | no responses / not common component |

> INFORMATION & COMMUNICATION SYSTEMS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------- |
| OEM Telematics (aka Telematics GateWay (TGW) / Off Vehicle Gateway / Communications Unit / Communications Telematics (CTP-FB)) (J1939 SA 249, 251) | **0**              | telematics device                   |
| Onboard Diagnostics Connector Gateway (aka Gateway (CGW)) (J1939 SA 39, 17, 44, 49, 50, 77)                                                        | **1**              | gateway device                      |
| 3rd Party Equipment Gateway (J1939 SA 249)                                                                                                         | **1**              | gateway device                      |
| Telematics Interface Gateway                                                                                                                       | **1**              | gateway device                      |
| On Board Diagnostic Unit (aka OEM Factory & Service tool) (J1939 SA 250)                                                                           | **2**              | large scope change risk             |
| Predictive Cruise Control (aka E-Horizon / Intelligent Predictive Powertrain Control (IPPC)) (J1939 SA 75)                                         | **2**              | large scope change risk             |
| On-Board Data Logger (J1939 SA 251)                                                                                                                | **3**              | medium total risk                   |
| Information System Controller \#1                                                                                                                  | **None Specified** | no responses / not common component |
| On Board Diagnostic Unit \#2                                                                                                                       | **None Specified** | no responses / not common component |

> CYBERSECURITY SYSTEMS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| --------------------------- | ----- | ------------------------------------ |
| Intrusion Detection System  | **3** | multi-homed and a security component |
| Intrusion Prevention System | **3** | multi-homed and a security component |

> LIGHTS & SIGNALS

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ------------------------------------------------------ | ----- | ------------------------------------------------ |
| Adaptive Front Lighting System (J1939 SA 71)           | **3** | medium safety risk                               |
| Chassis Controller \#2 (J1939 SA 72)                   | **3** | scope change high independent of low overal risk |
| Chassis Controller \#1 (aka SAM Chassis) (J1939 SA 71) | **5** | min total risk                                   |

> AIR EQUIPMENT

| **Component Reference Name**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | **Cybersecurity Requirements Class** | **Class Assignment Rationale**      |
| ------------------------------------------------------------------------ | ------------------ | ----------------------------------- |
| Brake Telematics                                                         | **0**              | telematics device                   |
| Brakes - System Controller (J1939 SA 11)                                 | **2**              | large scope change risk             |
| Parking Brake Controller (J1939 SA 80)                                   | **2**              | large scope change risk             |
| Pneumatic - System Controller (J1939 SA 48)                              | **3**              | medium safety risk                  |
| Auxiliary Valve Control or Engine Air System Valve Control (J1939 SA 34) | **5**              | min total risk                      |
| Brake Stroke Alert                                                       | **None Specified** | no responses / not common component |

All of the devices identified by the VCRWG are captured below, organized by their device class. This list can be useful when a particular device can not be found in the order sheet view above. If the device the fleet and OEM are interested in classifying cannot be found here then some device class characteristics are provided for determining membership of such unknown (to the VCRWG) devices.

| Class             | Characteristics                                                                                                                    | Examples                                                                                                                                                                                      |
| ----------------- | ---------------                                                                                                                    | ---------                                                                                                                                                                                     |
| 0 Telematics      | Truck modules that connect to cellular, satellite or other Wide Area Networks (WANs) or wireless networks, or the internet         | ELDs <br/> Trailer Trackers <br/> Trailer Telematics <br/> Brake Telematics <br/> Engine Telematics <br/> Transmission Telematics <br/> Tire Telematics <br/> Reefer Telematics <br/> Remote Diagnostics <br/> Remote Emissions Monitoring Engine Telematics (J1939 SA 249) <br/> Transmission Telematics <br/> Exterior Camera Telematics <br/> Interior Camera Telematics <br/> OEM Telematics (aka Telematics GateWay (TGW) / Off Vehicle Gateway / Communications Unit / Communications Telematics (CTP-FB)) (J1939 SA 249, 251) <br/> Brake Telematics |
| 1 Vehicle Gateway | Truck modules intended to transport, translate, transform, filter or encapsulate data between two or more vehicle network segments | Telematics Interface Gateways <br/> Diagnostics Interface Gateways Onboard Diagnostics Connector Gateway (aka Gateway (CGW)) (J1939 SA 39, 17, 44, 49, 50, 77) <br/> 3rd Party Equipment Gateway (J1939 SA 249) <br/> Telematics Interface Gateway                                                                                                                            |
| 2 Multi Segment   | Truck modules that are not intended to be *Vehicle Gateways* but nonetheless are connected to one or more vehicle network segments | Ignition Control Module \#2 (J1939 SA 57) <br/> Low-Voltage Disconnect (J1939 SA 49) <br/> Oil Sensor (J1939 SA 00) <br/> Starter System (J1939 SA 00,  03) <br/> Thermal Management System Controller (J1939 SA 49) <br/> Water Pump Controller (J1939 SA 57) <br/> Fuel Heater, In-Tank (J1939 SA 72) <br/> Steering Input Unit (aka Steering Angle Sensor (SAS)) <br/> Differential Lock Controller (J1939 SA 138, 72, 39 ) <br/> Antilock Brake System (ABS) (J1939 SA 11) <br/> Traction Control (J1939 SA 138, 39) <br/> Suspension - Drive Axle \#1 (J1939 SA 138, 72, 39) <br/> Suspension - Drive Axle \#2 (J1939 SA 22) <br/> Tractor/Trailer Bridge \#2 (J1939 SA 138, 39) <br/> Tractor-Trailer Bridge \#1 (J1939 SA 32) <br/> Tire Pressure Controller (aka Tire Pressure Monitoring System (TPMS)) (J1939 SA 51) <br/> Wheel End Monitoring <br/> Body-to-Vehicle Interface Control (aka VECU - Vehicle ECU) (J1939 SA 33) <br/> Fifth Wheel Smart System (J1939 SA 138, 39) <br/> Forward Road Image Processor (J1939 SA 232) <br/> ADAS Lane Keep (aka LCS Side Sensor (blind spot only) / Lane Warning / Lane Departure Warning System / Bendix Fusion / Exterior Camera for Lane Departune Warning / Driver Assistance Camera (MPC)) (J1939 SA 232, 19) <br/> Cab Controller - Primary (aka SAM CAB) (J1939 SA 49) <br/> Cab Controller - Secondary (J1939 SA 50) <br/> Cruise Control (J1939 SA 17) <br/> Object Detection Display (aka Active Safety Components / Bendix Fusion (Display)) <br/> ADAS Adaptive Cruise Control (aka Bendix Fusion) (J1939 SA 42) <br/> Ammeter (J1939 SA 23, 39) <br/> On Board Diagnostic Unit (aka OEM Factory & Service tool) (J1939 SA 250) <br/> Predictive Cruise Control (aka E-Horizon / Intelligent Predictive Powertrain Control (IPPC)) (J1939 SA 75) <br/> Brakes - System Controller (J1939 SA 11) <br/> Parking Brake Controller (J1939 SA 80)                                                                                                                                                                                          |
| Class 3           | Truck modules found to have a 'high' overall fleet risk                                                                            | Engine \#1 (aka Motor Control Module (MCM) / Engine Management System (EMS) / Engine Control Module (ECM)) (J1939 SA 00, 01) <br/> Engine Cylinder Pressure Monitoring System <br/> Aftertreatment \#1 system gas intake (J1939 SA 81) <br/> Aftertreatment \#2 system gas intake (J1939 SA 86) <br/> Diesel Particulate Filter Controller (aka Aftertreatment Control Module (ACM) / Exhaust Emission Controller) (J1939 SA 211) <br/> Engine Exhaust Backpressure (J1939 SA 34) <br/> Engine Valve Controller (J1939 SA 0) <br/> Fan Drive Controller (aka Fan Hub) (J1939 SA 78) <br/> Idle Control System (J1939 SA 68) <br/> Powertrain Control Module (aka Common Powertrain Controller Module (CPC)) (J1939 SA 90) <br/> Propulsion Battery Charger (J1939 SA 73) <br/> Retarder - Engine (J1939 SA 15) <br/> Retarder, Exhaust, Engine \#1 <br/> Retarder, Exhaust, Engine \#2 <br/> Radiator (aka Radiator Fan Control) (J1939 SA 78, 00, 255) <br/> Oil Pan Heater (J1939 SA 00) <br/> Clutch/Converter Unit (J1939 SA 78) <br/> Power TakeOff - (Main or Rear) (J1939 SA 07) <br/> Power TakeOff (Front or Secondary) (J1939 SA 07) <br/> Retarder - Driveline (J1939 SA 16) <br/> Transmission \#1 (aka Transmission Control Module (TCM)) (J1939 SA 03) <br/> Transmission \#2 (aka Auxiliary Transmission) (J1939 SA 16) <br/> Electronic Clutch Actuator (J1939 SA 03) <br/> Steering Controller (aka Front Axle Steering (FAS) / VDS / MCS) (J1939 SA 19) <br/> Suspension - Steer Axle (aka Electronically Controlled Suspension (ECS) / Electronically Controlled Air Suspension (ECAS)) (J1939 SA 20) <br/> Suspension - System Controller \#1 (J1939 SA 47) <br/> Lift Axle (J1939 SA 138, 71) <br/> Vehicle Dynamic Stability Controller (J1939 SA 62) <br/> Automated Driving (L0-L2) (aka Bendix FLR and FLC (Forward looking Camera / Radar)) <br/> Collision Avoidance (J1939 SA 42) <br/> Fuel Actuator (J1939 SA 15) <br/> Body Controller (aka Key-Lock Options) <br/> Safety Restraint System (SRS) (J1939 SA 83) <br/> Throttle (J1939 SA 0) <br/> Vehicle Navigation (J1939 SA 84) <br/> Power TakeOff (PTO) Switches (J1939 SA 07) <br/> Headway Controller (J1939 SA 42) <br/> On-Board Data Logger (J1939 SA 251) <br/> Adaptive Front Lighting System (J1939 SA 71) <br/> Chassis Controller \#2 (J1939 SA 72) <br/> Pneumatic - System Controller (J1939 SA 48)                                                                                                                                                                                          |
| Class 4           | Truck modules found to have a 'medium' overall fleet risk                                                                          | Engine Injection Control Module (J1939 SA 00) <br/> Axle - Drive \#1 (J1939 SA 09) <br/> Axle - Drive \#2 (J1939 SA 10) <br/> Mirrors (J1939 SA 40) <br/> Lighting - Operator Controls (J1939 SA 71) <br/> Transmission Display - Primary (J1939 SA 59) <br/> Trip Recorder (J1939 SA 24) <br/> Switch Field (aka Additional Switches / Modular Switch Field (MSF)) (J1939 SA 138) <br/> Instrument Cluster \#1 (aka Gauges) (J1939 SA 23) <br/> Engine Display                                                                                                                                                                                          |
| Class 5           | Truck modules found to have a 'low' overall fleet risk                                                                             | Aftertreatment \#1 system gas outlet (aka NoX Sensors ) (J1939 SA 82) <br/> Aftertreatment \#2 system gas outlet (J1939 SA 87) <br/> Alternator/Electrical Charging System <br/> Battery Charger <br/> Battery Pack Monitor \#1 (J1939 SA 243) <br/> Catalyst Fluid Sensor (aka DEF Quality Sensor) (J1939 SA 211) <br/> Engine Exhaust Gas Recirculation (J1939 SA 70) <br/> Ignition Control Module \#1 (J1939 SA 52) <br/> Turbocharger (J1939 SA 02) <br/> Turbocharger Compressor Bypass (J1939 SA 02) <br/> Turbocharger Wastegate (J1939 SA 02) <br/> Air Intake System (J1939 SA 70) <br/> Filtration Control <br/> Axle - Steering (J1939 SA 08) <br/> Brakes - Drive axle \#1 (J1939 SA 13) <br/> Brakes - Drive Axle \#2 (J1939 SA 14) <br/> Electric Propulsion Control Unit \#1 <br/> Personnel Detection Device (aka Pedestrian Detection) <br/> Slope Sensor (aka Hill Start Assist) <br/> Body Controller \#2 <br/> Door Controller (J1939 SA 236) <br/> Door Controller \#1 (J1939 SA 237) <br/> Door Controller \#2 <br/> Door Controller \#3 <br/> Door Controller \#4 <br/> Roadway Information <br/> Vehicle Security (J1939 SA 29) <br/> Cab Display \#1 <br/> Passenger-Operator Climate Control \#1 (aka LECM (Living Environment Control Module) / HVAC / HVAC FCU) (J1939 SA 25) <br/> Passenger-Operator Climate Control \#2 (aka HVAC \#2 / HVAC ACU) <br/> Retarder Display (J1939 SA 23) <br/> Seat Control \#1 <br/> Shift Console - Primary (aka Gearshift ECU) (J1939 SA 05) <br/> Shift Console - Secondary (J1939 SA 06) <br/> Steering Column Unit (aka Turn Signal Control) <br/> Transmission Display - Secondary (J1939 SA 60) <br/> Radio (aka Head Unit / Infotainment) (J1939 SA 76, 84) <br/> Steering Wheel Switches (J1939 SA 77) <br/> Pyrometer <br/> Chassis Controller \#1 (aka SAM Chassis) (J1939 SA 71) <br/> Auxiliary Valve Control or Engine Air System Valve Control (J1939 SA 34)                                                                                                                                                                                          |


# Cybersecurity Requirements

This is still a work in progress. The WG expects the cybersecurity requirements to be similar to the Telematics Security Requirements Matrix https://github.com/nmfta-repo/nmfta-telematics_security_requirements but will incorporate more requirements pertaining specifically to vehicle components. The WG started with a small subset of the requirements to prove methods and tools in the https://github.com/nmfta-repo/vcr-experiment.

If you would like to join the working group please contact ben.gardiner@nmfta.org


# License

All files are Copyright (c) 2022 National Motor Freight Traffic Association, Inc. and are made available under the MIT license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# Other Resources and History

The previous work on cybersecurity requirements by the NMFTA CTSRP (then, HVCS) was to create the Telematics Security Requirements Matrix https://github.com/nmfta-repo/nmfta-telematics_security_requirements . These requirements were ported to this project and re-applied where possible. The questionnaires for those requirements and also contract template language was captured in the https://github.com/nmfta-repo/nmfta-rfp_templates repo.

The initial work to create these requirements started with a vehicle network architecture survey in collaboration with OEMs. The results were:
* a picture of 'typical' Class 7-8 truck networks, circa 2021 -- can be found in the "degrees of separation" captured in the [`resources/Component_Class_Assignment_v16_DIST.xlsx`](resources/Component_Class_Assignment_v16_DIST.xlsx)
* a list of common components/modules/devices names and aliases -- mapped to the J1939 names wherever possible -- can be found in the "reference names" captured in the [`resources/Component_Class_Assignment_v16_DIST.xlsx`](resources/Component_Class_Assignment_v16_DIST.xlsx)
* a risk analysis of components/modules/devices in those networks as it pertains to fleets (aka fleet risk)
* the assignment of the components/modules/devices to *Device Classes* as captured above -- can be found in the "proposed device class" captured in the [`resources/Component_Class_Assignment_v16_DIST.xlsx`](resources/Component_Class_Assignment_v16_DIST.xlsx)

Some preliminary work on capturing security (and functional) requirements for vehicle gateways performed during the Nov 2021 CTSRP meeting was done in the https://github.com/nmfta-repo/vcr-experiment where the [`strictdoc`](https://github.com/strictdoc-project/strictdoc) requirements format was assessed.

The test plan used by the CTSRP for onsite vehicle testing is provided as a starting point for an eventual acceptance test plan for these requirements; available here: [`resources/heavy vehicle testing plan.md`](resources/heavy_vehicle_testing_plan.md)
