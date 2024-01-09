import os

os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
import torch

torch.backends.cudnn.benchmark = False
torch.use_deterministic_algorithms(True)
from diffusers import DDIMScheduler, StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
g = torch.Generator(device="cuda")

prompt = "A bear is playing a guitar on Times Square"

g.manual_seed(0)
result1 = pipe(prompt=prompt, num_inference_steps=50, generator=g, output_type="latent").images

g.manual_seed(0)
result2 = pipe(prompt=prompt, num_inference_steps=50, generator=g, output_type="latent").images

print("L_inf dist = ", abs(result1 - result2).max())
