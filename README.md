# olsrd2CoreTB
Presentation on NinuxDay 2016 @  Florance, November 26 - 27 2016

Using testbed:
- Install Core Network simulator: https://www.nrl.navy.mil/itd/ncs/products/core
- Install OLSRd2: http://www.olsr.org/mediawiki/index.php/Olsrd2
- modify corennx/oonf.py to point right path for installation of oonf
- modify /etc/core/core.conf line "custom_services_dir = /foo/bar/corennx" to point provided folder
- start Core and load Olsr2TestBed.imn
- follow last slide
