import math

def temperature(start,end,step):
    print(f"{'цельсий':<10} | {'фарингейт':<10}")
    print("-"*25)

    for celsius in range(start,end - 1,step):
        fahrenheit = celsius * 1.8 +32
        print(f"{celsius:<10} | {fahrenheit:<10.1f}")

temperature(100,0,-10)