# Scripts for the NMFTA Heavy Duty Vehicle Cybersecurity Requirements (HDVCR)

## `import-tsrm.py`

For importing a release of the https://github.com/nmfta-repo/nmfta-telematics_security_requirements

Save the release excel as `tsrm.xls` and run `import-tsrm.py`. The results will be files:
* `out/mobile_app_tsrm.sdoc`
* `out/vehicle_connection_tsrm.sdoc`
* `out/connectivity_tsrm.sdoc`
* `out/cloud_tsrm.soc`

For now, incorporating `*.sdoc` into the HDVCR is a manual process after that.