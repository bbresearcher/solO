Disclaimer:
#I DO NOT WARRANTY THIS CODE TO BE BUG FREE OR TO BE FIT FOR PURPOSE, RUNNING solO AGAINST A PROJECT DOES NOT GUARANTEE THAT THE PROJECT IS SECURE AND/OR BUG FREE

Would this be of any value for Solana projects/Audits if the code was written using Anchor?

- It pulls out all the Solana account definitions to make them visible to the researcher
- It cam scan the code based on a easy template created by the researcher for any static vulnerabilities.

I would like to take it further to check the account definitions for safety eg. no Signer account, or highlight that the definition closes the account so its obvious, and use the anchor definitions to maybe add more information.

run the demo with `python3 solO.py . ./templates/`
