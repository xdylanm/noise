import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    header_lines = 12
    read_count = 10000000
    avg_count = 1
    record_len = 0
    dt1 = 0
    data = np.zeros((read_count, 2))

    with open("./docs/source/data/PN.csv", "r") as hf:
        record_len = int(hf.readline().strip().split(":")[-1])
        dt1 = float(hf.readline().strip().split(":")[-1])
        for iha in range(header_lines - 2):
            hf.readline()

        for iln in range(read_count):
            a, b = hf.readline().strip().split(',')
            data[iln,:] = [float(a), float(b)]
    
    dta = avg_count*dt1
    nta = read_count // avg_count
    ta = np.linspace(0, (nta-1)*dta, nta)
    assert(len(ta) == nta)
    print(f"Found {record_len} records, sample interval {dt1}s, delta f={1/(nta*dta)}Hz")

    sliced_data = np.zeros((nta, avg_count))
    for ia in range(avg_count):
        sliced_data[:,ia] = data[ia:(len(data)-avg_count+ia+1):avg_count,1]

    freq = np.fft.fftfreq(nta, dta)
    resp = np.zeros_like(sliced_data, dtype=np.complexfloating)

    for ia in range(avg_count):
        resp[:,ia] = np.fft.fft(sliced_data[:,ia], norm="forward")

    avg_resp = np.average(resp, axis=1)
    avg_resp = avg_resp[0:(nta // 2)]
    freq = freq[0:(nta // 2)]

    with open(f"./docs/source/data/PN_spectrum_avg{avg_count}.npy","wb") as hf:
        np.save(hf, freq)
        np.save(hf, avg_resp)

    #print(f"max resp {np.max(np.abs(avg_resp))}")

    plt.semilogx(freq, 20*np.log10(np.abs(avg_resp)))
    plt.grid(True)
    plt.xlabel("frequency (Hz)")
    plt.ylabel("gain (dB)")
    plt.show()