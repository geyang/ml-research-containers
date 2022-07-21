# Container Image with Ravens Environment

Used for transporter net [^1]

## Development Logs

Logs for the Dockerfile:
- realized that the way I was using multiple base images was incorrect
- realized that the cuda version needs to be less or equal than the host machine, so downgrading to 11.2
- realized that different unix python packages occupy different binary names. python2 is python, python3.6 is python3, and 3.8 is python3.8.
- realized that the distro utilities and pip needs to be installed separately.
- fixed a bug where the apt install of the pycurl dependencies fails if it happens after ravens installation (reasons is not clear)

[^1]: Zeng, Andy et al. “Transporter Networks: Rearranging the Visual World for Robotic Manipulation.” CoRL (2020). 
