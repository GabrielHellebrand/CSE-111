import math

radius = (6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10)

heights = (10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11)

efficency = []

def main():
    for i in range(0, len(radius)):
        efficency.append(storage_efficency(radius[i], heights [i]))

    print(efficency)

def compute_volume(r , h):
    return math.pi * (r ** 2) * h

def compute_surface_area(r , h):
    return 2 * math.pi * (r + h)

def storage_efficency(r , h):
    return compute_volume (r , h) / compute_surface_area (r , h)
main()