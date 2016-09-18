# MazeFinder

### 본 프로그램은 대정령님의 도트액션 플레이 영상을 보다가 미로 찾기가 귀찮아서 만들었습니다.

##미로 그림을 받아서, 시작점부터 목적지점 까지의 경로를 구해줍니다.

## 받는 입력은 다음과 같습니다 (색깔은 모두 RGB로 3번에 나눠서 받습니다)
	- 미로 그림파일 경로
	- 길인 부분의 색깔로 지정할 수 <= n
	- n개의 길 색깔
	- 결과로 표시될 길의 색깔
	- 시작 위치
	- 도착 위치

## MazeFinder 클래스 안에 적당히 지정된 상수
	- colorAllowOffset : 그 곳이 길인지 판별할때 쓰는, RGB각 값마다의 허용 오차
	- nextOffsets : 어떤 픽셀의 다음 픽셀이 될 수 있는 픽셀간의 Offset들 ex) 바로 붙어있는 상하좌우 픽셀 => ((1,0),(-1,0),(0,1),(0,-1))
	- resultColorAlpha : 결과로 표시될 길 색깔의 alpha값
	- resultThickness : 결과로 표시될 길의 굵기

## Test
	- 대정령님의 방송 녹화본 중 한 장면을 가져와서(miro1.png) 테스트에 써볼 수 있습니다.
	- 맨 아래에서 mazeFinder.run() 대신, mazeFinder.testrun()으로 바꿔서 실행 하시면 됩니다.

## Dependency
	- numpy
	- PIL

