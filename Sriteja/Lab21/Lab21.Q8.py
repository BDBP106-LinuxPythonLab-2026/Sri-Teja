"""Function protein_energy_temp() with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S by using
random or user-input ∆H, ∆S and returning stability (”stable" if ∆G < 0)"""

def protein_energy_temp():
    H = float(input("Enter Enthalpy:"))
    T = float(input("Enter temperature in Kelvin:"))
    S = float(input("Enter Entropy:"))

    def calculate_free_energy(H,T,S):
        return H-T*S
    G=calculate_free_energy(H,T,S)
    if G<0:
        return "stable"
    else:
        return "unstable"
print(protein_energy_temp())