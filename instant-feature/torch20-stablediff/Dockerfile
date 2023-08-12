# A Dockerfile that sets up a full Gym install with test dependencies
FROM episodeyang/instant-feature-t20

RUN pip install accelerate==0.17.1
RUN pip install addict==2.4.0
RUN pip install basicsr==1.4.2
RUN pip install bitsandbytes==0.35.4
RUN pip install clip
RUN pip install cmake==3.25.2
RUN pip install controlnet-aux==0.0.6
RUN pip install decord==0.6.0
RUN pip install deepspeed==0.8.0
RUN pip install diffusers==0.14.0
RUN pip install easydict==1.10
RUN pip install einops==0.6.0
RUN pip install ffmpy==0.3.0
RUN pip install ftfy==6.1.1
RUN pip install moviepy==1.0.3
RUN pip install numpy==1.24.2
RUN pip install omegaconf==2.3.0
RUN pip install opencv-python==4.7.0.68
RUN pip install pandas==1.5.3
RUN pip install pillow==9.4.0
RUN pip install scikit-image==0.19.3
RUN pip install scipy==1.10.1
RUN pip install tensorboard==2.12.0
RUN pip install tensorboard-data-server==0.7.0
RUN pip install tensorboard-plugin-wit==1.8.1
RUN pip install termcolor==2.2.0
RUN pip install thinc==8.1.10
RUN pip install timm==0.6.12
RUN pip install tokenizers==0.13.2
RUN pip install tqdm==4.64.1
RUN pip install transformers==4.26.1
RUN pip install wandb==0.13.10
RUN pip install xformers==0.0.16
RUN pip install modelcards
RUN pip install triton==2.0.0.post1
RUN pip install positional_encodings==6.0.1
RUN pip install mediapipe==0.10.0
RUN pip install termcolor==2.2.0

# A Dockerfile that sets up a full Gym install with test dependencies
FROM episodeyang/instant-feature-t20

RUN python <<EOF
print('run this')
EOF

RUN pip install pycurl
#RUN pip install imageio==2.25.1 # ml-logger requires 2.27.0
#RUN pip install imageio-ffmpeg==0.4.8
RUN pip install jaynes ml_logger waterbear params-proto functional_notations cloudpickle==1.3.0
