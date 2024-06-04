
# Werwolf
### A  fun youth group game

## Development plan

In order to develop the game, we need to cover the following steps:
- [X] Write down the game rules
    - done in prompts/rules.md
- [X] Write down a detailed playbook, that covers
    - who (which role)
    - does what 
    - when (step by step)
    - ... keep specifying steps until the game completes the first round of the the main-loop
- [X] Structure game rules and playbook as "cards" that fit nicely into an embedding
- [X] Encode the cards using "voyage-large-2-instruct" (1024 dimensions) and save to pinecone
- [ ] Scaffold a system-prompt that gives the bot general instructions on how to determine the respective next step
- [ ] Script a game-loop based off of the example "example-agent.ipynb" that
    - Welcomes the user with an info-screen
    - Asks for the number of real and simulated players
    - Starts a game
        - determine next action using the system-prompt
        - retrieve rules and playbook from pinecone
        - send context and action to llm
        - display the result