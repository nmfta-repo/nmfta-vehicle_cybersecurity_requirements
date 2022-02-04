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
| Telematics      | Truck modules that connect to cellular, satellite or other Wide Area Networks (WANs) or wireless networks, or the internet         | ELDs, Trailer Trackers, Trailer Telematics, Brake Telematics, Engine Telematics, Transmission Telematics, Tire Telematics, Reefer Telematics, Remote Diagnostics, Remote Emissions Monitoring |
| Vehicle Gateway | Truck modules intended to transport, translate, transform, filter or encapsulate data between two or more vehicle network segments | Telematics Interface Gateways, Diagnostics Interface Gateways TODO                                                                                                                            |
| Multi Segment   | Truck modules that are not intended to be *Vehicle Gateways* but nonetheless are connected to one or more vehicle network segments | TODO                                                                                                                                                                                          |
| Class 1         | Truck modules found to have a 'high' overall fleet risk                                                                            | TODO                                                                                                                                                                                          |
| Class 2         | Truck modules found to have a 'medium' overall fleet risk                                                                          | TODO                                                                                                                                                                                          |
| Class 3         | Truck modules found to have a 'low' overall fleet risk                                                                             | TODO                                                                                                                                                                                          |
| Class 4         | Truck modules found to have a _minimum_ overall fleet risk                                                                         | TODO                                                                                                                                                                                          |


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
