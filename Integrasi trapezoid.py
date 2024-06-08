import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Trapezoid untuk integrasi numerik
def trapezoid_integration(f, a, b, N):
    h = (b - a) / N
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Fungsi untuk menghitung galat RMS
def rms_error(approx, exact):
    return np.sqrt((approx - exact)**2)

# Fungsi utama untuk menjalankan pengujian dengan berbagai N dan mengukur waktu eksekusi
def main():
    # Nilai referensi pi
    pi_reference = 3.14159265358979323846
    
    # Variasi nilai N
    N_values = [10, 100, 1000, 10000]
    
    for N in N_values:
        start_time = time.time()
        pi_approx = trapezoid_integration(f, 0, 1, N)
        end_time = time.time()
        
        error = rms_error(pi_approx, pi_reference)
        exec_time = end_time - start_time
        
        print(f"N = {N}")
        print(f"Pi Approximation: {pi_approx}")
        print(f"RMS Error: {error}")
        print(f"Execution Time: {exec_time} seconds\n")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
