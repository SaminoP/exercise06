import signal_plot_ops as sp


signal = sp.load_signal_from_txt("ekg_signal.txt")

priemer = sp.signal_avg(signal)

print("Priemer signalu:", priemer)

sp.plot_signal(signal)