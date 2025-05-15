#Medir velocidade
import speedtest
test = speedtest.Speedtest()
down = test.download()
up = test.upload()
# pip install speedtest
print({down})
print({up})