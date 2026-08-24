# clinic-content

병원 콘텐츠 저장소. 썸네일과 스레드 원고를 여기 한 곳에 모읍니다.
병원이 늘어도 **저장소를 새로 만들지 말고 폴더로 나눕니다.**

```
images/   썸네일. .jpg = 스레드·인스타용, .webp = 워드프레스 특성 이미지용
원고/     스레드 발행용 원고 (━━━ 헤더 ━━━ 형식)
```

## 이 저장소가 공개인 이유

스레드와 인스타는 이미지를 **자기 서버가 직접 주소로 가져갑니다.** 그래서
이미지가 있는 저장소는 공개여야 발행이 됩니다. 비공개로 두면 사진을 못 읽어
발행이 실패합니다.

공개하기 곤란한 원고가 있으면 원고만 비공개 저장소에 두고 토큰으로 읽어오면 됩니다.

## 발행

`~/Desktop/DEV/social-publisher`의 `publish.mjs`가 이 저장소를 읽습니다.

```bash
node publish.mjs 원고/21-sedation.txt --from-github        # 미리보기
node publish.mjs 원고/21-sedation.txt --from-github --go   # 실제 발행
```

## 썸네일 만들기

`~/Desktop/DEV/thumbnail-maker`에서 생성한 뒤 `images/`에 넣습니다.
파일명 규칙: `buldang-thumb-NN-english-slug`, 수정본은 `-v2`, `-v3`.
