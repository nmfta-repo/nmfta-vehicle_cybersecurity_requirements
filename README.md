# NMFTA Heavy Duty Vehicle Cybersecurity Requirements (HDVCR)

Cybersecurity requirements for telematics systems developed in collaboration with motor freight carriers, OEMs and cybersecurity experts.

The cybersecurity requirements captured here are for use by fleets to include in their procurement process with OEMs. The requirements are intended to cover the following truck body configurations, which we intend to cover most of what LTL carriers need:
* North America "on highway" Class 7-8 trucks e.g. the classic truck w/ trailer or double as the  most common configuration
* and also the last mile delivery truck with a dry freight truck body that could include a lift gate


## How to Use the HD VCR

We recommend that fleets use these requirements by following some steps during the procurement process. We are open to feedback on how to improve the requirements and the process.

1. Fleets should ask OEMs to identify all the modules in the requested truck by the *Device Classes* below.
2. Fleets should prepare questionnaires to be completed by the OEMs based on the classes found.
3. OEMs complete the questionnaires, answering in the affirmative if all devices of the given class satisfy the requirement. Deviations and rationale can be noted in the provided cells of the questionnaires.


## Device Classes

TODO

There are specifications of cybersecurity requirements for each of the following device classes here in this project. The device class examples should be used by fleets and OEMs to determine the class membership of modules from a particular truck first and the characteristics second.

| Class           | Characteristics                                                                                                                    | Examples                                                                                                                                                                                      |
| --------------- | ---------------                                                                                                                    | ---------                                                                                                                                                                                     |
| 0 Telematics      | Truck modules that connect to cellular, satellite or other Wide Area Networks (WANs) or wireless networks, or the internet         | ELDs, Trailer Trackers, Trailer Telematics, Brake Telematics, Engine Telematics, Transmission Telematics, Tire Telematics, Reefer Telematics, Remote Diagnostics, Remote Emissions Monitoring Engine Telematics (J1939 SA 249), Transmission Telematics, Exterior Camera Telematics, Interior Camera Telematics, OEM Telematics (aka Telematics GateWay (TGW) / Off Vehicle Gateway / Communications Unit / Communications Telematics (CTP-FB)) (J1939 SA 249, 251), Brake Telematics |
| 1 Vehicle Gateway | Truck modules intended to transport, translate, transform, filter or encapsulate data between two or more vehicle network segments | Telematics Interface Gateways, Diagnostics Interface Gateways Onboard Diagnostics Connector Gateway (aka Gateway (CGW)) (J1939 SA 39, 17, 44, 49, 50, 77), 3rd Party Equipment Gateway (J1939 SA 249), Telematics Interface Gateway                                                                                                                            |
| 2 Multi Segment   | Truck modules that are not intended to be *Vehicle Gateways* but nonetheless are connected to one or more vehicle network segments | Ignition Control Module #2 (J1939 SA 57), Low-Voltage Disconnect (J1939 SA 49), Oil Sensor (J1939 SA 00), Starter System (J1939 SA 00,  03), Thermal Management System Controller (J1939 SA 49), Water Pump Controller (J1939 SA 57), Fuel Heater, In-Tank (J1939 SA 72), Steering Input Unit (aka Steering Angle Sensor (SAS)), Differential Lock Controller (J1939 SA 138, 72, 39 ), Antilock Brake System (ABS) (J1939 SA 11), Traction Control (J1939 SA 138, 39), Suspension - Drive Axle #1 (J1939 SA 138, 72, 39), Suspension - Drive Axle #2 (J1939 SA 22), Tractor/Trailer Bridge #2 (J1939 SA 138, 39), Tractor-Trailer Bridge #1 (J1939 SA 32), Tire Pressure Controller (aka Tire Pressure Monitoring System (TPMS)) (J1939 SA 51), Wheel End Monitoring, Body-to-Vehicle Interface Control (aka VECU - Vehicle ECU) (J1939 SA 33), Fifth Wheel Smart System (J1939 SA 138, 39), Forward Road Image Processor (J1939 SA 232), ADAS Lane Keep (aka LCS Side Sensor (blind spot only) / Lane Warning / Lane Departure Warning System / Bendix Fusion / Exterior Camera for Lane Departune Warning / Driver Assistance Camera (MPC)) (J1939 SA 232, 19), Cab Controller - Primary (aka SAM CAB) (J1939 SA 49), Cab Controller - Secondary (J1939 SA 50), Cruise Control (J1939 SA 17), Object Detection Display (aka Active Safety Components / Bendix Fusion (Display)), ADAS Adaptive Cruise Control (aka Bendix Fusion) (J1939 SA 42), Ammeter (J1939 SA 23, 39), On Board Diagnostic Unit (aka OEM Factory & Service tool) (J1939 SA 250), Predictive Cruise Control (aka E-Horizon / Intelligent Predictive Powertrain Control (IPPC)) (J1939 SA 75), Brakes - System Controller (J1939 SA 11), Parking Brake Controller (J1939 SA 80)                                                                                                                                                                                          |
| Class 3         | Truck modules found to have a 'high' overall fleet risk                                                                            | Engine #1 (aka Motor Control Module (MCM) / Engine Management System (EMS) / Engine Control Module (ECM)) (J1939 SA 00, 01), Engine Cylinder Pressure Monitoring System, Aftertreatment #1 system gas intake (J1939 SA 81), Aftertreatment #2 system gas intake (J1939 SA 86), Diesel Particulate Filter Controller (aka Aftertreatment Control Module (ACM) / Exhaust Emission Controller) (J1939 SA 211), Engine Exhaust Backpressure (J1939 SA 34), Engine Valve Controller (J1939 SA 0), Fan Drive Controller (aka Fan Hub) (J1939 SA 78), Idle Control System (J1939 SA 68), Powertrain Control Module (aka Common Powertrain Controller Module (CPC)) (J1939 SA 90), Propulsion Battery Charger (J1939 SA 73), Retarder - Engine (J1939 SA 15), Retarder, Exhaust, Engine #1, Retarder, Exhaust, Engine #2, Radiator (aka Radiator Fan Control) (J1939 SA 78, 00, 255), Oil Pan Heater (J1939 SA 00), Clutch/Converter Unit (J1939 SA 78), Power TakeOff - (Main or Rear) (J1939 SA 07), Power TakeOff (Front or Secondary) (J1939 SA 07), Retarder - Driveline (J1939 SA 16), Transmission #1 (aka Transmission Control Module (TCM)) (J1939 SA 03), Transmission #2 (aka Auxiliary Transmission) (J1939 SA 16), Electronic Clutch Actuator (J1939 SA 03), Steering Controller (aka Front Axle Steering (FAS) / VDS / MCS) (J1939 SA 19), Suspension - Steer Axle (aka Electronically Controlled Suspension (ECS) / Electronically Controlled Air Suspension (ECAS)) (J1939 SA 20), Suspension - System Controller #1 (J1939 SA 47), Lift Axle (J1939 SA 138, 71), Vehicle Dynamic Stability Controller (J1939 SA 62), Automated Driving (L0-L2) (aka Bendix FLR and FLC (Forward looking Camera / Radar)), Collision Avoidance (J1939 SA 42), Fuel Actuator (J1939 SA 15), Body Controller (aka Key-Lock Options), Safety Restraint System (SRS) (J1939 SA 83), Throttle (J1939 SA 0), Vehicle Navigation (J1939 SA 84), Power TakeOff (PTO) Switches (J1939 SA 07), Headway Controller (J1939 SA 42), On-Board Data Logger (J1939 SA 251), Adaptive Front Lighting System (J1939 SA 71), Chassis Controller #2 (J1939 SA 72), Pneumatic - System Controller (J1939 SA 48)                                                                                                                                                                                          |
| Class 4         | Truck modules found to have a 'medium' overall fleet risk                                                                          | Engine Injection Control Module (J1939 SA 00), Axle - Drive #1 (J1939 SA 09), Axle - Drive #2 (J1939 SA 10), Mirrors (J1939 SA 40), Lighting - Operator Controls (J1939 SA 71), Transmission Display - Primary (J1939 SA 59), Trip Recorder (J1939 SA 24), Switch Field (aka Additional Switches / Modular Switch Field (MSF)) (J1939 SA 138), Instrument Cluster #1 (aka Gauges) (J1939 SA 23), Engine Display                                                                                                                                                                                          |
| Class 5         | Truck modules found to have a 'low' overall fleet risk                                                                             | Aftertreatment #1 system gas outlet (aka NoX Sensors ) (J1939 SA 82), Aftertreatment #2 system gas outlet (J1939 SA 87), Alternator/Electrical Charging System, Battery Charger, Battery Pack Monitor #1 (J1939 SA 243), Catalyst Fluid Sensor (aka DEF Quality Sensor) (J1939 SA 211), Engine Exhaust Gas Recirculation (J1939 SA 70), Ignition Control Module #1 (J1939 SA 52), Turbocharger (J1939 SA 02), Turbocharger Compressor Bypass (J1939 SA 02), Turbocharger Wastegate (J1939 SA 02), Air Intake System (J1939 SA 70), Filtration Control, Axle - Steering (J1939 SA 08), Brakes - Drive axle #1 (J1939 SA 13), Brakes - Drive Axle #2 (J1939 SA 14), Electric Propulsion Control Unit #1, Personnel Detection Device (aka Pedestrian Detection), Slope Sensor (aka Hill Start Assist), Body Controller #2, Door Controller (J1939 SA 236), Door Controller #1 (J1939 SA 237), Door Controller #2, Door Controller #3, Door Controller #4, Roadway Information, Vehicle Security (J1939 SA 29), Cab Display #1, Passenger-Operator Climate Control #1 (aka LECM (Living Environment Control Module) / HVAC / HVAC FCU) (J1939 SA 25), Passenger-Operator Climate Control #2 (aka HVAC #2 / HVAC ACU), Retarder Display (J1939 SA 23), Seat Control #1, Shift Console - Primary (aka Gearshift ECU) (J1939 SA 05), Shift Console - Secondary (J1939 SA 06), Steering Column Unit (aka Turn Signal Control), Transmission Display - Secondary (J1939 SA 60), Radio (aka Head Unit / Infotainment) (J1939 SA 76, 84), Steering Wheel Switches (J1939 SA 77), Pyrometer, Chassis Controller #1 (aka SAM Chassis) (J1939 SA 71), Auxiliary Valve Control or Engine Air System Valve Control (J1939 SA 34)                                                                                                                                                                                          |


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
* a picture of 'typical' Class 7-8 truck networks, circa 2021
* a list of common components/modules/devices names and aliases -- mapped to the J1939 names wherever possible
* a risk analysis of components/modules/devices in those networks as it pertains to fleets (aka fleet risk)
* the assignment of the components/modules/devices to *Device Classes* as captured above

The (large) spreadsheet work product of this activity is available in this repo under the `resources/` folder.

Some preliminary work on capturing security (and functional) requirements for vehicle gateways performed during the Nov 2021 CTSRP meeting was done in the https://github.com/nmfta-repo/vcr-experiment where the [`strictdoc`](https://github.com/strictdoc-project/strictdoc) requirements format was assessed.

The test plan used by the CTSRP for onsite vehicle testing is provided as a starting point for an eventual acceptance test plan for these requirements; available here: [`resources/heavy vehicle testing plan.md`](resources/heavy_vehicle_testing_plan.md)