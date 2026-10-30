import numpy as np
import matplotlib.pyplot as plt
import os 

step = 3


data_path = os.path.expanduser("~/Desktop/mfEvaluation/data/")

if step == 0:
    vel_field = np.load(os.path.join(data_path, "vel_0000.npy"))
    den_field = np.load(os.path.join(data_path, "den_0000.npy"))
elif step == 1:
    vel_field = np.load(os.path.join(data_path, "vel_0500.npy"))
    den_field = np.load(os.path.join(data_path, "den_0500.npy"))
elif step == 2:
    vel_field = np.load(os.path.join(data_path, "vel_1000.npy"))
    den_field = np.load(os.path.join(data_path, "den_1000.npy"))
elif step == 3:
    vel_field = np.load(os.path.join(data_path, "vel_1500.npy"))
    den_field = np.load(os.path.join(data_path, "den_1500.npy"))
else:
    vel_field = np.load(os.path.join(data_path, "vel_2000.npy"))
    den_field = np.load(os.path.join(data_path, "den_2000.npy"))

print(f"shape:  {vel_field.shape}")
print(f"dtype:  {vel_field.dtype}")
print(f"size:   {vel_field.size}")

print(f"shape:  {den_field.shape}")
print(f"dtype:  {den_field.dtype}")
print(f"size:   {den_field.size}")

print("density min/max:", den_field.min(), den_field.max())
print("velocity min/max:", vel_field.min(), vel_field.max())

#den_field[32] is a 64x64 slice in the middle of the cube
plt.imshow(den_field[32], cmap="gray")
plt.colorbar(label="density")
plt.title("Density, middle slice")
plt.show()

speed = np.linalg.norm(vel_field, axis=-1)
plt.imshow(speed[32], cmap="viridis")
plt.colorbar(label="speed")
plt.title("Speed, middle slice")
plt.show()

kin_energy = np.linalg.norm(vel_field, axis=-1)
kin_energy = kin_energy * 0.5
kin_energy = kin_energy * den_field
plt.imshow(kin_energy[32], cmap="viridis")
plt.colorbar(label="energy")
plt.title("energy, middle slice")
plt.show()