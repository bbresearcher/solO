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
