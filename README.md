# RL Docker Images

A list of community-maintained docker images for deep reinforcement learning research.

Our experience has shown that docker and singularity-based workflow works really well, to the extent that you only need to install your packages once, in a docker image, and you can deploy it directly via singularity anywhere.

## Why Upload Singularity Images

In some of the HPC systems, the file system is locked, causing images that are built within to fail.

```bash
mkdir -p /state/partition1/user/$USER  

export TMPDIR=/state/partition1/user/$USER  
singularity pull --docker-login docker://alpine 
this works fine. And then the following line breaks:

singularity exec --nv alpine_latest.sif bash -c 'echo "hey"'
```

Actual behavior

```
INFO:    Could not find any nv files on this host!
WARNING: passwd file doesn't exist in container, not updating
WARNING: group file doesn't exist in container, not updating
```

## Considerations for Building Singulairity Images

- https://stackoverflow.com/questions/61143522/file-ownership-and-permissions-in-singularity-containers

## Model-free Deep Reinforcement Learning

This image includes mujoco-py, gym, and DeepMind control. The Singularity image is built on Canon.




