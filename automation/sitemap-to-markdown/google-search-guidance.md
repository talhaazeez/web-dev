# Google Search guidance for sitemap-to-Markdown workflow

## Design principles

1. Generate content for people first, not primarily to manipulate rankings. Google emphasizes helpful, reliable, original, comprehensive content and warns against mass-produced pages that add little value.
2. Use the existing webpage as the primary source. The workflow should extract the page title, headings, visible text, metadata, canonical URL, and links, then ask the model to improve or restructure only where it can add clear user value.
3. Require human review before publishing. The output is a draft and should include a review status, source URL, source fetch time, and a list of claims or sections that need verification.
4. Do not promise rankings or use a fixed word count. Use a target length only as a usability constraint and allow the topic and user intent to determine depth.
5. Add authorship and creation-method context where appropriate. If AI materially generated the draft, the Markdown front matter can disclose that fact and identify the human reviewer.
6. Create distinct titles and headings. Titles should be descriptive, concise, page-specific, non-boilerplate, and free from keyword stuffing. The first H1 should clearly identify the page topic.
7. Treat structured data as conditional. The workflow may recommend JSON-LD type and fields, but should not invent facts or add markup for information that is not visible on the page. Validate structured data after implementation.
8. Preserve canonical and internal-link signals. Each file should include the source/canonical URL and suggested crawlable internal links that are genuinely relevant.
9. Add quality gates. Reject or flag pages with thin extracted content, duplicate or near-duplicate text, missing source content, conflicting metadata, or unsupported factual claims.
10. Do not auto-publish. Save to Google Drive and/or provide downloadable Markdown files, with optional later publishing only after explicit approval.

## Suggested Markdown output

YAML front matter should contain: title, description, canonical, source_url, slug, language, page_type, target_audience, primary_topic, suggested_schema_type, generated_at, source_fetched_at, generation_method, review_status, and reviewer_notes.

The body should contain one H1, a concise introduction, useful H2/H3 sections, original value or recommendations, relevant internal links, source notes, and a review checklist. The workflow should not fabricate citations, statistics, prices, reviews, author credentials, or product claims.

## Source references

- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
