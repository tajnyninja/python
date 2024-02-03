from pylab import plot, show, title, xlabel, ylabel

# średnie roczne temperatury w Nowym Jorku
title("Średnie roczne temperatury w NY")
xlabel("X label")
ylabel("Y label")
nyc_t = [12.17, 13.5, 13.56, 11.89, 12.5, 13.22, 13.78, 12.78, 12.94, 12.22, 13.72, 13.56, 14.06]
years = range(2000, 2013)

plot(years, nyc_t, marker='o')

# Renderuje wykres
show()