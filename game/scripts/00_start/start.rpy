label start:

    
    $ user=renpy.input("What is your username?",length=16)

    while user == "":
        $ user=renpy.input("What is your username?",length=16)


    scene bg start
    play music "audio/groove.wav" loop
    a "Err guys."

    a "Is it just me.."
    a "or is there water on the floor?"
    b "Um yeah."
    b "Have you never seen water before?"
    a "..."
    a "Ok smartass."
    a "Why is the water level rising then?"
    c "What?"
    c "Have you never seen a flood before?"
    a "..."
    a "What about the streamer?"
    a "Are they going to be ok??"
    d "Staged"
    e "Def staged"
    b "Yeah fake"
    a "What if it isn't???"
    c "Staged"
    f "Unemployed isn't wrong."
    f "Streamer isn't awake to stage anything."
    a "Wake up streamer!"
    b "Nah don't."

    menu:
        "Wake them up!":
            jump wakeup01
        "Not your problem":
            jump sleep01
        
