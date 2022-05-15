# Simple FIM
 File Integrity Monitoring proof of concept.

Option A will create a new baseline with contents hashed in SHA512 if no baseline found in path, otherwise it will overwite.

When using option B (must have baseline created), script will alert of the following<br />
-Alert user if file has been created in green<br />
-Alert user if file has changed in yellow<br />
-Alert user if file has been deleted in red
