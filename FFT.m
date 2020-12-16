fs = 4000;
Ts = 1/fs;
f0 = 500;
A = sqrt(2);
N = 1024;
n = 0:N-1;
x = A*sin(2*pi*f0*n*Ts) + 0.1*randn(1,N);

nfft = N;
%window = rectwin(nfft);
window = hanning(nfft);
[pxx,f]=pwelch(x,window,0,nfft,fs);
PdB_Hz =10*log10(pxx*fs/nfft)

plot(f,PdB_Hz)