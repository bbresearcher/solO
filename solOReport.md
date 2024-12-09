# solO Report
- Running solO against directory: .
- Rules templates directory set as : ./templates/
## Rust files found:
   [^] lib.rs
### File: ./lib.rs
 ---
:large_blue_diamond: **#: Account Object found: SomeRandomType**

:arrow_right:  *Struct has instuction inputs of : [instruction(inValOne: String, inValTwo: String)]* 

:clipboard: Anchor account member below has attributes: 
- init,
- seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
- bump,
- payer = initializer,
- space = DISCRIMINATOR + DemoState::INIT_SPACE

:red_circle: **[STRUCT FIELD:] demo_state of type Account<'info, DemoState>,**

:clipboard: Anchor account member below has attributes: 
- mut

:red_circle: **[STRUCT FIELD:] initializer of type Signer<'info>,**

:red_circle: **[STRUCT FIELD:] system_program of type Program<'info, System>,**

---
:large_blue_diamond: **#: Account Object found: SomeOtherType**

:arrow_right:  *Struct has instuction inputs of : [instruction(inValOne:String)]* 

:clipboard: Anchor account member below has attributes: 
- mut
- mut,
- seeds = [inValOne.as_bytes(), initializer.key().as_ref()],
- bump,

:red_circle: **[STRUCT FIELD:] demo_state of type Account<'info, DemoState>,**

:clipboard: Anchor account member below has attributes: 
- mut

:red_circle: **[STRUCT FIELD:] initializer of type Signer<'info>,**

:red_circle: **[STRUCT FIELD:] system_program of type Program<'info, System>,**

---
:large_blue_diamond: **#: Account Object found: LastRandomType**

:arrow_right:  *Struct has instuction inputs of : [instruction(inValOne: String)]* 

:clipboard: Anchor account member below has attributes: 
- mut
- mut,
- seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
- bump,
- close=initializer

:red_circle: **[STRUCT FIELD:] demo_state of type Account<'info, DemoState>,**

:clipboard: Anchor account member below has attributes: 
- mut

:red_circle: **[STRUCT FIELD:] initializer of type Signer<'info>,**

:red_circle: **[STRUCT FIELD:] system_program of type Program<'info, System>**

## Rule checks returned the list of code to check below:
### File: ./lib.rs
   #: Match found on : 1==1
   #: Found an random equivalency check

```
19-    ) -> Result<()> {
20:        if 1==1 {
21-            msg!("Welcome to the Demo");

```
