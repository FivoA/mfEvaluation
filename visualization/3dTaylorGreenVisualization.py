import numpy as np
import matplotlib.pyplot as plt

step = 1

if step == 0:
    vel_field = np.load('../data/vel_0000.npy')
    density_field = np.load('../data/den_0000.npy')
elif step == 1:
    vel_field = np.load('../data/vel_0250.npy')
    density_field = np.load('../data/den_0250.npy')
elif step == 2:
    vel_field = np.load('../data/vel_0500.npy')
    density_field = np.load('../data/den_0500.npy')
elif step == 3:
    vel_field = np.load('../data/vel_1080.npy')
    density_field = np.load('../data/den_1080.npy')
else:
    vel_field = np.load('../data/vel_1400.npy')
    density_field = np.load('../data/den_1400.npy')

print(f"shape:  {vel_field.shape}")
print(f"dtype:  {vel_field.dtype}")
print(f"size:   {vel_field.size}")

print(f"shape:  {density_field.shape}")
print(f"dtype:  {density_field.dtype}")
print(f"size:   {density_field.size}")

print("density min/max:", density_field.min(), density_field.max())
print("velocity min/max:", vel_field.min(), vel_field.max())

#density_field[32] is a 64x64 slice in the middle of the cube
plt.imshow(density_field[32], cmap="gray")
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
kin_energy = kin_energy * density_field
plt.imshow(kin_energy[32], cmap="viridis")
plt.colorbar(label="energy")
plt.title("energy, middle slice")
plt.show()