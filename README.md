# 복학생의 가을 - Ren'Py 8.5 Prototype v0.1.3

## v0.1.3 수정
- Ren'Py의 대괄호 `[...]` 문자열 보간과 충돌하던 장면/루트 표기를 수정했습니다.
- `[월요일 / 복학 첫날]` 같은 표시용 문자열은 `【월요일 / 복학 첫날】`로 변경했습니다.
- 실제 변수 보간인 `[older_affection]`, `[friend_affection]`, `[junior_affection]`, `[config.name]`, `[slot]`은 유지했습니다.
- 한글 폰트 설정(SourceHanSansLite.ttf) 및 Korean line breaking 설정은 v0.1.2 수정사항을 유지합니다.

## 실행
기존 프로젝트에 덮어쓰지 말고 이 폴더를 Ren'Py 8.5 Launcher에 별도 프로젝트로 등록해 실행하세요.

# 복학생의 가을 - Ren'Py 8.5 Prototype v0.1.2

## 실행
1. Ren'Py 8.5 Launcher에서 이 폴더를 프로젝트로 등록합니다.
2. `Launch Project`를 실행합니다.
3. 기존 버전 폴더에 덮어쓰기보다는 이 폴더를 새 프로젝트로 등록하는 것을 권장합니다.

## v0.1.2 수정 사항
- 한국어가 네모/깨진 문자로 보이던 문제 수정.
- Ren'Py SDK에 포함된 `SourceHanSansLite.ttf`를 검색 경로에 추가.
- 대사, 캐릭터명, 메뉴, 버튼, 시스템 UI의 기본 폰트를 한국어 지원 폰트로 통일.
- `gui.language = "korean-with-spaces"` 적용.

## 참고
이 개발용 프로젝트는 Ren'Py 8.5 SDK의 `sdk-fonts/SourceHanSansLite.ttf`를 사용합니다.
Ren'Py Launcher를 통해 실행하면 별도 폰트 설치가 필요하지 않습니다.
