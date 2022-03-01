The following is a test plan used by NMFTA CTSRP to complete onsite vehicle tests that have evolved over time. We expect that it could be used as a starting point for the development of a test plan for acceptance testing of vehicles against the HC VCR.

---

Summary of testing activities:

* PLC4TRUCKS/J2497 tractor devices and features present
* PLC4TRUCKS/J2497 trailer devices and features present
* PLC4TRUCKS/J2497 REDACTED testing
* PLC4TRUCKS/J2497 leakage testing
* J1708 presence on RP1226 connector
* J1708 tractor brake diagnostic service valve control captures
* PLC4TRUCKS presence on RP1226 connector
* difference between RP1226 CAN segments and OBD connector segments
* collection of cellular devices on the tractor and/or trailer

We won't save any logs other than the diagnostic sessions noted here and then only with your permission.

We will share a set of testing notes and any conclusions by EOD TBD.


### Schedule

TBD


### Equipment Shipped

TBD


### Fleet Services Shop Assistance Requested:

1. Access to a truck & trailer, at least one. Additional pairs are useful, but would only be requested time-permitting.
2. The ability to key-on: run in accessory and start the tractor. There is no planned motion of the tractor; we will need to start it just to recharge air supplies and battery sometimes.
3. an extension cable that can reach the cab of the truck under test, expected power draw 200W / ~2A
4. between 8-12 'traffic cones' (the tall ones are preferred, but any will do)
5. The ability to connect to the RP1226 port in the tractor. This could be in the berth or in the dash. So this could required opening up a panel or two. We would like to be able to disconnect anything installed to the RP1226 connector but if that is not OK please let us know and we will use my crocodile and/or backprobes only
6. The ability to connect to the OBD port in the tractor. We would like to be able to disconnect anything installed there but if that is not OK please let us know and we can try to use my crocodile and/or backprobes instead
7. The ability to disconnect the trailer from the tractor
8. A battery cart to power the trailer separately sometimes
9. (optional) ladder for getting to top of cab and trailer
10. (optional) creeper for easier access to trailer underbody
11. Good weather -- if you can swing it ;)


## Tests in Brief

* Test A1: trailer J2497 devices present
* Test A2 (multiple): other tractor J2497 segments (OBD & RP1226 & other)
* Test A3 (multiple): J2497 segmentation
* Test B1: tractor J1708 devices present, OBD
* Test B2: tractor J1708 devices present, RP1226
* Test B3: J2497 bridging from J1708
* Test B4: J1708 bridging from J2497
* Test C1: passive CAN analysis on all tractor segments (OBD pins & RP1226 pins)
* Test C2: active CAN scan on all tractor segments (OBD pins & RP1226 pins)
* Test D1: sweep tractor and trailer for cellular signals
* Test E1: PLC4TRUCKS/J2497 REDACTED
* Test E2: PLC4TRUCKS/J2497 leakage testing
* Test F1: J1708 tractor brake diagnostic service valve control captures


### Test Execution Order (for prioritization)

A1, E1, F1

B1, B2, A2, B3, B4, A3, E2

C1, C2, D1


## Test Details

### Test A1: trailer J2497 devices present
1. connect to tractor-trailer J2497 segment
2. log traffic for 2 mins; collect all MIDs
3. make note of MIDs, discard log
4. (optional) run j1587map to active scan the devices present
5. make note of MIDs, PIDs supported and other j1587 features supported, discard log

Motivation: We expect to find both trailer and tractor ABS units. Comparing expectations to reality


### Test A2 (multiple): other tractor J2497 segments

For OBD port, RP1226 port and any telematics power lines (if there are any that are different):

1. repeat A1 steps


### Test A3 (multiple): J2497 segmentation

For any J2497 telematics-connected segment found (test each power pin individually):

1. Connect a PLC transmitter to the telematics-connected segment
2. Send trailer chuff commands using PLC testcon
3. If chuff is observed then connectivity is confirmed, else:
4. Connect a SDR to trailer powerlines and look at 100-400KHz spectrum to estimate power required to bypass segmentation
5. Send trailer chuff commands using GPIO method
6. repeat 3.
7. repeat 4.

Motivation:  We do expect to find some segments are filtered; however, filtering might actually be insufficient for security guarantees.


### Test B1: tractor J1708 devices present, OBD

At the OBD port, if J1708 is present:

1. connect to OBD J1708 pins
2. repeat A1 steps 2.-5.


### Test B2: tractor J1708 devices present, RP1226

At the RP1226 port:

1. connect to RP1226 J1708 pins
2. repeat A1 steps 2.-5.


### Test B3: J2497 bridging from J1708

For each J1708 segment (could be both OBD and RP1226 but those are probably the same segment):

1. connect a truck duck to J1708 segment
2. connect a plctestcon to J2497 segment
3. observe J1708 traffic
4. start logging J1708 traffic
5. send scan of MIDs and PIDs from J2497, avoiding MIDs already present to prevent dynamic address claim changes
6. analyze j1708 traffic for signs of bridging, make note of MIDs and/or PIDs which are passed.
7. discard log file


### Test B4: J1708 bridging from J2497

For each J1708 segment (could be both OBD and RP1226 but those are probably the same segment):

1. repeat B3 steps 1-6 but swap the role of J2497 and J1708 segments


### Test C1: passive CAN analysis on all tractor segments (OBD pins & RP1226 pins)

Connect to the CAN pairs -- including OEM reserved pins -- and collect and analyze the traffic (all passive)

1. connect a truck duck to each pin pair in OBD port and RP1226, for each:
2. observe J1939 traffic, capture logs
3. analyze logs and make note of which segments are identical and which segments share messages
4. discard logs


### Test C2: active CAN scan on all tractor segments (OBD pins & RP1226 pins)

Connect to CAN pairs of interest (based on C1) and scan for available UDS services.

1. connect a truck duck to interesting pin pairs in OBD port and RP1226, for each:
2. start CAN logging
3. using cmap or similar tool to send UDS service requests
4. analyze logs and make note of which segments are identical and which segments share services
5. discard logs


### Test D1: sweep tractor and trailer for cellular signals

Sweep the truck and trailer for cellular transmitters, making note of locations and (possibly) any markings of the transmitters.

1. tune sensitivity of field detector on cell phone and wireless hot spot
2. sweep cab interior
3. sweep cab exterior (as much as possible, height could be limited)
4. sweep trailer front panel
5. sweep trailer underbody
6. make note of location and strength of any signals found
7. make note of any visible markings of transmitter
8. (optionally) observe location with SDR to characterize transmitter


### Test E1: PLC4TRUCKS/J2497 REDACTED


### Test E2: PLC4TRUCKS/J2497 leakage testing

We've prepared a couple ELDs to test how much J2497 they leak from their MCU GPIO pins, if at all.

1. connect BBB powered by 5V to a modified ELD connected to the vehicle
2. send bitbanged J2497 via the modified ELD
3. measure amplitude of leaked J2497 using oscilloscope and SDR


### Test F1: J1708 tractor brake diagnostic service valve control captures

We would like to capture some traffic of the diagnostics tools interacting with tractor brake controllers over J1708.

1. work with local experts to understand diagnostics features available
2. iteratively capture traffic in parallel with local experts diagnostic software performing interesting diagnostics feature


# Appendix A: Truck Onsite Equipment Checklist

## Direct Connect Stuff

- [ ] a notepad
- [ ] coveralls
- [ ] gloves
- [ ] headlamp
- [ ] power squid
- [ ] mini screwdriver
- [ ] pinout paper printouts of RP1226 and OBD
- [ ] paper printouts of diag commands
- [ ] custom umbilical cable
- [ ] dg tech plctestcon
- [ ] db-15 to deutsch 2-pin power adapter
- [ ] a deutsch-9 connected truck duck (for OBD)
- [ ] a gpio modded truck duck
- [ ] inline pin-to-banana leads and a banana-jack truck duck (for RP1226)
- [ ] banana pigtails for J1708 to Truck Duck
- [ ] dupont male-male cables for interconnect
- [ ] backprobes to banana
- [ ] oscilloscope & SMA->MCX adapter
- [ ] electrical tape
- [ ] breakout for CAN CROC / J1708 CROC
- [ ] OBD2 breakout (for Volvo / Mack)

- [ ] 3.3V j2497 leakage test adapter (inline mini)
- [ ] 1.8V j2497 leakage test adapter (ELD)

### Optional Direct Connect Stuff

- [ ] a dc-block (SMA connector) for custom umbilical
- [ ] a j1708 crocodile
- [ ] a CAN crocodile
- [ ] SDR+ upconverter OR
- [ ] direct-sampling SDR with enough DR for 50mVPP
- [ ] attenuators
- [ ] EMF field meters
- [ ] ethernet switch & cables

## Plus J2497 REDACTED


# Appendix B: Tools Check

- [ ] logging j1708 with `j1708dump`
- [ ] analyze j1708 logs for MIDs and PIDs
- [ ] passive scan of j1708 segment with `j1587map`
- [ ] active scan of j1708 segment with `j1587map`
- [ ] send sentinels and/or fuzzing search with `j1708send`
- [ ] logging j1939 with `candump`
- [ ] scanning j1939 with `cmap`
- [ ] EMF meter validation quick check
