# GEO: AI가 우리 글을 가져가 인용하게 만들기

SEO가 "검색 결과에 뜨기"라면, GEO는 **ChatGPT·Claude·퍼플렉시티가 답변할 때 우리 글을 인용하게 만들기**입니다.

| 할 일 | 파일 | 상태 |
|---|---|---|
| 1. 학습봇만 막고, 인용봇은 열기 | `robots.txt` | 바로 올리면 됨 |
| 2. 사이트 핵심을 AI가 빨리 읽게 정리 | `llms.txt` | `{{ }}` 칸 채운 뒤 올리기 |
| 3. 남이 인용·링크하게 만들기 | 아래 체크리스트 | 계속 |

## AI 봇 두 종류

- **학습용 봇**: 다음 모델을 학습시키려고 글을 가져감. 출처 링크가 남지 않음.
  `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `Bytespider`, `Meta-ExternalAgent`
- **인용·답변용 봇**: 질문이 들어올 때 실시간으로 페이지를 읽고 **출처 링크를 달아** 답함.
  `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`

> `Google-Extended`를 막아도 **구글 검색 노출에는 영향 없습니다.**
> 네이버(`Yeti`), 다음(`Daum`), 구글(`Googlebot`), 빙(`Bingbot`)은 `User-agent: *`로 모두 열려 있습니다.

## 워드프레스에 올리는 법

**robots.txt**
- Rank Math: 일반 설정 → robots.txt 편집 → 내용 전체 붙여넣기
- Yoast: 도구 → 파일 편집기 → robots.txt
- 플러그인이 없으면 호스팅 파일관리자로 사이트 최상위 폴더(`wp-config.php` 있는 곳)에 업로드
- `Sitemap:` 주소가 실제로 열리는지 확인 (Rank Math·Yoast는 `sitemap_index.xml`, 플러그인 없으면 `wp-sitemap.xml`)

**llms.txt**
1. `{{ }}` 칸을 모두 채움
2. 사이트 최상위 폴더에 업로드 → `https://dreamdentist.kr/llms.txt`가 열리면 끝

## 새 글 발행할 때마다

- [ ] 중요 주제면 `llms.txt`에 한 줄 추가: `- [글 제목](주소): 이 글이 답하는 질문`
- [ ] 글 맨 앞 2~3문장에 **답을 먼저** (AI는 앞부분을 가장 많이 인용)
- [ ] 숫자·기준은 구체적으로
- [ ] 원장 저자 카드 넣기
- [ ] 썸네일 대체텍스트를 **한국어 문장**으로

## 남이 인용하게 만들기 (가장 중요)

AI는 "본인 소개"보다 **"남이 인용한 글"을 훨씬 믿습니다.**

- [ ] 병원만의 기준을 이름 붙여 공개 (예: "불당드림치과 잇몸 자가진단 7가지")
- [ ] 스레드·인스타 게시물 댓글에 원문 링크
- [ ] 네이버 플레이스·구글 비즈니스 프로필에 사이트 주소 연결
- [ ] 정보 카드 이미지 하단에 사이트 주소 표기
