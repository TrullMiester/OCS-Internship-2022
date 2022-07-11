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
- Raspbian for Robots
- Debian Shell

# Current difficulties faced 

- GoPiGo3 NEEDS wifi, cannot connect to the robot over ethernet. **Solution** Setup wifi using ethernet, use chromebook for rest 
- Unclear if loaded GoPiGo OS / Dexeter OS allows for me to run pythons scripts, I only see jupyter. **Solution** Use RfR OS
- No MicroSD port on PCs, don't know if I can install Raspbian for Robots to allow for more control. **Solution** Acquired MicroSD reader
- Unclear if my project will be big enough to last me the 5/6 weeks. 
    - Current idea is to just write a program that will use the distance sensor and simply drive around any obstacles while still being close to them.
    - Another idea is to add a camera and livestream it while also doing that.
    - Need to research other possible sensors if first 2 are too simple.

# Locomotion

By default, the robot will veer to the right. Therefore, with my PID (Just P at the moment) controller, I will overcompensate for the right motor. After lots of trial and error, I had an overcompensation constant that resulted in mostly straight movement. 

The provided turn_degrees method works well, there's some error that builds up but it shouldn't be a concern since I won't need precise turning. The amount of degrees turned will be decided by an algorithm using inputs from the distance sensor.

Using the provided encoders I could provide an estimate of distance travelled, but there's the veering and subsequent overcompensation. As a result, I don't think it'll be very accurate and so I don't think I could make the bot know it's location relative to the start point.

Forward function takes advantage of encoders and just tells motors to turn a certain amount of degrees, stopping as soon as it reaches it. This should result in forward motion as straight as possible.

To make the robot turn without moving, there basically is just 1 solution to this problem. Therefore my implementation and the given implementation are equivalent, mine is superior only because I am able to tweak the constants for a more precise turn.

To make the robot estimate its own position, I need distance travelled from last measurement and the orientation of the robots. I can store these in variables either by editing the class or just putting these in a testing function. I think the second option is best because this is just an estimate, the robot doesnt drive perfectly straight and the turns aren't perfect either. 

# Perception

There are currently 2 sensors on the robot, encoders on the motors and a distance sensor. The distance sensor has a range of 5 mm to 2300 mm and will return a value of 3000 if there is nothing in its range. The encoders tell me how many degrees the motors have rotated, allowing me to use proportional control to improve its driving and precisely instruct the motors how much to rotate for accurate turns.

After an epiphany I wrote another function to move the robot forward, this uses the encoders and basically what happens is I instruct the motors to rotate a certain amount, then use encoder readings to make sure they stop rotating as soon as they hit that amount. This allows for very straight movement as I am not relying on the motors at all. I control everything.

Currently my autonomous function will make the robot go forwards until it reaches an obstacle. Then, it will scan the area and choose to go parallel to the spot where the robot is closest too. This works fine in avoiding collisions, but it will also go off into space and not really follow the obstructions. To fix this I think I should periodically check surroundings, not only when the distance sensor says something is close. 

Another option I have is making the distance sensor face 1 side of the robot and then trying to follow the path such that distance is minimized. I believe this could work. but I would have to have another sensor to look forward so the robot won't collide. The other possibility would be to use 3 distance sensors and just use that to determine where walls are.
