# 페인트 면적 계산기

# 한 캔으로 칠할 수 있는 면적  5제곱미터.
# 필요한 캔의 개수를 구하는 방법 => 벽의 폭 X 벽의 높이 / 5(제곱미터)
# ex) 폭 2m, 높이가 4m인 경우 (2 X 4)/5
# => 위의 경우 1.6캔이지만 분할 판매는 하지않기 때문에 올림해줘야한다.
import math

test_h = int(input("벽의 높이 : "))
test_w = int(input("벽의 폭 : "))
coverage = 5

def paint_calc(height,width,cover):
    can = height*width/cover
    print(f"{math.ceil(can)}캔이 필요합니다.")
    
    
paint_calc(height = test_h, width = test_w, cover = coverage)