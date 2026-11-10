# tools

## thumb5.py — 썸네일 표준 v5

```bash
# 준비 (한 번)
python3 -m venv .venv && .venv/bin/pip install pillow
mkdir -p .font && (cd .font && npm pack pretendard@1.3.9 && tar xzf pretendard-*.tgz)

# 생성: 원본사진 출력경로(확장자 없이) 세로오프셋 제목1줄 제목2줄 폰트폴더
.venv/bin/python tools/thumb5.py clinic-photo-profile.webp images/buldang-thumb-NN-slug 0 \
  "40대 잇몸 내려앉음, 원인과" "자가진단 7가지·치료 기준" .font/package/dist/public/static
```

- 사진 프리셋: 정보·예방·치과공포증 = `clinic-photo-profile.webp` / 시술·재교정·잇몸이식·임플란트 = `clinic-photo-clinic.webp`
- 결과: 1200×675, `.webp`(워드프레스, q76 m6) + `.jpg`(스레드)
- 한 줄 1080px 넘으면 에러로 멈춤 → 제목을 줄이세요
