# status.hsp.sh

This is setup as a mixture of smaller services that provide a dashboard via monitoror and spaceapi as proxy to whois.at.hsp.sh
It is hosted on an external host provided by mikr.us.

## Design

* Pull data from public services about hackerspace.
* Push data to it from internal network.

This should enable secure service that doesn't expose internal network while informing what works in the DMZ.
