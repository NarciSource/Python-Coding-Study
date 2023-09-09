import sys
n = int(sys.stdin.readline())
squres = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

iou_max = -1
for i in range(n):
    for j in range(i+1,n):
        ix,iy,iw,ih = squres[i]
        jx,jy,jw,jh = squres[j]
        ix,iw,jx,jw = (ix,iw,jx,jw) if ix<jx else (jx,jw,ix,iw)
        iy,ih,jy,jh = (iy,ih,jy,jh) if iy<jy else (jy,jh,iy,ih)

        w = min(ix+iw, jx+jw) - min(ix+iw, jx)
        h = min(iy+ih, jy+jh) - min(iy+ih, jy)
        iou = w*h/(iw*ih + jw*jh - w*h)

        if iou > iou_max:
            iou_max = iou
            squre_pair = i+1,j+1
print(*squre_pair)