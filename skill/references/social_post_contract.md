# Chinese Social Post Contract

Generate a JSON and a Markdown version per Chinese course. The JSON uses this shape:

```json
{
  "topic": "…",
  "title_lines": ["第一行", "第二行"],
  "opening": "…",
  "second_paragraph": "…",
  "body": [{"heading": "一、…", "text": "…"}],
  "ending": "…",
  "hashtags": ["…"],
  "sources": [{"title": "…", "url": "…"}]
}
```

| Field | Requirement |
|---|---|
| `title_lines` | Exactly 2 lines; each 10–24 Chinese characters. |
| `opening` | 50–100 characters. |
| `second_paragraph` | 45–120 characters. |
| `body` | Exactly 4 sections; each section text 60–180 characters. |
| `ending` | 25–72 characters. |

Keep the Markdown wording exactly aligned with the final validated JSON. Cite authoritative sources in both versions when facts or product descriptions are included. Do not apply the Chinese-character count to English posts; keep the English version structurally parallel but write for natural English readers.
