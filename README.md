Disclaimer:
#I DO NOT WARRANTY THIS CODE TO BE BUG FREE OR TO BE FIT FOR PURPOSE, RUNNING solO AGAINST A PROJECT DOES NOT GUARANTEE THAT THE PROJECT IS SECURE AND/OR BUG FREE

Would this be of any value for Solana projects/Audits if the code was written using Anchor?

- It pulls out all the Solana account definitions to make them visible to the researcher
- It can scan the code based on a easy template created by the researcher for any static vulnerabilities.

I would like to take it further to check the account definitions for safety eg. no Signer account, or highlight that the definition closes the account so its obvious, and use the anchor definitions to maybe add more information.

run the demo with `python3 solO.py . ./templates/`

# Example Project
---

# solO Report
- Running solO against directory: .
- Rules templates directory set as : ./templates/
## Rust files found:
   [^] lib.rs
### File: ./lib.rs
 ---
 #: Account Object found: SomeRandomType

*Struct has instuction inputs of : [instruction(inValOne: String, inValTwo: String)]* 

Anchor account member below has attributes: 
- init,
- seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
- bump,
- payer = initializer,
- space = DISCRIMINATOR + DemoState::INIT_SPACE

**demo_state of type Account<'info, DemoState>,**

Anchor account member below has attributes: 
- mut

**initializer of type Signer<'info>,**

**system_program of type Program<'info, System>,**

---
 #: Account Object found: SomeOtherType

*Struct has instuction inputs of : [instruction(inValOne:String)]* 

Anchor account member below has attributes: 
- mut
- mut,
- seeds = [inValOne.as_bytes(), initializer.key().as_ref()],
- bump,

**demo_state of type Account<'info, DemoState>,**

Anchor account member below has attributes: 
- mut

**initializer of type Signer<'info>,**

**system_program of type Program<'info, System>,**

---
 #: Account Object found: LastRandomType

*Struct has instuction inputs of : [instruction(inValOne: String)]* 

Anchor account member below has attributes: 
- mut
- mut,
- seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
- bump,
- close=initializer

**demo_state of type Account<'info, DemoState>,**

Anchor account member below has attributes: 
- mut

**initializer of type Signer<'info>,**

**system_program of type Program<'info, System>**

## Rule checks returned the list of code to check below:
### File: ./lib.rs
   #: Match found on : 1==1
   #: Found an random equivalency check

```
19-    ) -> Result<()> {
20:        if 1==1 {
21-            msg!("Welcome to the Demo");

```

