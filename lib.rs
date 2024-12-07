use anchor_lang::prelude::*;
use anchor_spl::token::{mint_to, MintTo, Mint, TokenAccount, Token};
use anchor_spl::associated_token::AssociatedToken;

declare_id!("YOUR_GENERATED_KEY");
//NB Giving the correct credit for the structure of this file below!!
//This file was adapted to just have a basic structure for demonstartion purposes as a generic file 
//based on the Solana Website Tutorial file at https://solana.com/developers/courses/onchain-development/anchor-pdas#lab
 
#[program]
pub mod solo-demo{
    use super::*;
 
    pub fn justAFunction(
        ctx: Context<SomeRandomType>,
        inValOne: String,
        inValTwo: String,
        inValThree: u8
    ) -> Result<()> {
        if 1==1 {
            msg!("Welcome to the Demo");
            }
     
        Ok(())
    }
}

#[account]
#[derive(InitSpace)]
pub struct DemoState {
    pub SomeUser: Pubkey,
    pub inValThree: u8,
    pub inValOne: String,
    pub inValTwo: String,
}
 
const DISCRIMINATOR: usize = 8;

#[derive(Accounts)]
#[instruction(inValOne: String, inValTwo: String)]
pub struct SomeRandomType<'info> {
    #[account(
        init,
        seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
        bump,
        payer = initializer,
        space = DISCRIMINATOR + DemoState::INIT_SPACE
    )]
    pub demo_state: Account<'info, DemoState>,
    #[account(mut)]
    pub initializer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
#[instruction(inValOne:String)]
pub struct SomeOtherType<'info> {
    #[account(
        mut,
        seeds = [inValOne.as_bytes(), initializer.key().as_ref()],
        bump,
    )]
    pub demo_state: Account<'info, DemoState>,
    #[account(mut)]
    pub initializer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
#[instruction(inValOne: String)]
pub struct LastRandomType<'info> {
    #[account(
        mut,
        seeds=[inValOne.as_bytes(), initializer.key().as_ref()],
        bump,
        close=initializer
    )]
    pub demo_state: Account<'info, DemoState>,
    #[account(mut)]
    pub initializer: Signer<'info>,
    pub system_program: Program<'info, System>
}
