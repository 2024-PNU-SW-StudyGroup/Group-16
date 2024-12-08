ahi, ami, asi, ahf, amf, asf  = map(int,input().split())
bhi, bmi, bsi, bhf, bmf, bsf  = map(int,input().split())
chi, cmi, csi, chf, cmf, csf  = map(int,input().split())

aw = -(ahi*3600+ami*60+asi)+(ahf*3600+amf*60+asf)
bw = -(bhi*3600+bmi*60+bsi)+(bhf*3600+bmf*60+bsf)
cw = -(chi*3600+cmi*60+csi)+(chf*3600+cmf*60+csf)

awh = aw//3600
awm = (aw%3600)//60
aws = (aw%3600)%60

bwh = bw//3600
bwm = (bw%3600)//60
bws = (bw%3600)%60

cwh = cw//3600
cwm = (cw%3600)//60
cws = (cw%3600)%60

print(awh, awm, aws)
print(bwh, bwm, bws)
print(cwh, cwm, cws)    