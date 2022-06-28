## Duckietown 

Only available on linux, I have no clue if I can use on CPS computer. I don't have access to a laptop so unsure if this is viable option for me.

## Raspberry PI or Arduino 

Using distance sensor on GoPiGo, navigate the hallway/atrium autonimously. Maybe try to follow a set path.

## FRC/FTC

Same thing as a Raspberry PI just using the FRC or FTC platform.

# Planning Questions 

### What is it?

    Autonomous navigation of terrain using camera/distance sensor/tape. 

### What is the problem?

    The big problem is that robots are dumb if not human controlled (controller or program) so I am trying to make it "smarter".
    
### Why is this relevant? 

    It's very relevant in robotics because navigation of the playing field is super important. 

### What is considered a success?

    It'll be a success if it's able to navigate terrain without hitting said terrain. 
    
### Who is this for?

    It's for every robotics team ever.

### What will the final product be?

    The final product will look like a codebase able to take advantage of multiple different types of sensors to achieve this goal.

### How will it be tested?

    It'll first be put through simple system checks (turning, veering, collision detection, going straight)
    After it passes system checks then it'll be a process of trial and error until it's able to navigate any terrain it's deployed in.

# Technologies used 

- GoPiGo3
- GoPiGo OS / Dexeter OS and Python 

# Current difficulties faced 

- GoPiGo3 NEEDS wifi, cannot connect to the robot over ethernet
- Unclear if loaded GoPiGo OS / Dexeter OS allows for me to run pythons scripts, I only see jupyter 
- No MicroSD port on PCs, don't know if I can install Raspbian for Robots to allow for more control 
- Unclear if my project will be big enough to last me the 5/6 weeks. 