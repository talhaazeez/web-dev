# Sitemap to Google-Friendly Markdown Drafts

This directory contains an n8n workflow framework that accepts either a sitemap URL or an uploaded sitemap XML file, fetches the listed webpages, and generates reviewable Markdown drafts. The workflow is intentionally **inactive and review-first**: it does not publish content automatically.

## Included files

| File | Purpose |
| --- | --- |
| `sitemap_to_markdown_workflow.js` | n8n Workflow SDK source used to create the workflow. |
| `google-search-guidance.md` | Design safeguards based on current Google Search documentation. |

## Workflow behavior

The workflow now includes a single browser-friendly **front-door form** for normal use. Open the `Sitemap URL or XML File Form` node in n8n, copy its Test URL while testing or its Production URL after activation, and open that link in your browser. On the form, use either the URL field or the file-upload field, not both.

| Input method | Where to enter it |
| --- | --- |
| Sitemap URL | Paste the complete public URL, such as `https://example.com/sitemap.xml`, into `Sitemap URL`. |
| XML file | Select the local `sitemap.xml` file in `Upload sitemap.xml`. |
| Output choice | Select `download` to return a Markdown file or `drive` to upload it to Google Drive. |

The form automatically routes URL submissions and uploaded XML submissions to the correct branch. It also handles a sitemap index such as `https://obsoglobal.com/sitemap_index.xml`: child sitemap files are fetched first, then their actual webpage URLs are expanded. The older separate URL and upload forms remain available as alternatives, and the webhook endpoints remain available for programmatic calls.

For the current obsoglobal test, paste `https://obsoglobal.com/sitemap_index.xml` into the **Sitemap URL** field, set **Maximum pages** to 3–5, and choose `download` for the first review run. Do not begin with the entire index because it contains many child sitemaps and a large number of product and content URLs.


| Form | Purpose |
| --- | --- |
| `sitemap-to-markdown/form/url` | Enter a sitemap URL, maximum page count, and output mode. |
| `sitemap-to-markdown/form/upload` | Upload an XML sitemap file, maximum page count, and output mode. |

The forms provide these fields:

| Field | Meaning |
| --- | --- |
| `sitemapUrl` | Public sitemap URL for URL mode. |
| `sitemapFile` | XML sitemap upload for file mode. |
| `maxPages` | Maximum pages to process, capped at 100. |
| `outputMode` | `download` returns the Markdown file; `drive` uploads it to Google Drive. |

The workflow exposes two POST webhook inputs:

| Input | Path | Payload |
| --- | --- | --- |
| Sitemap URL | `/webhook/sitemap-to-markdown/url` | JSON containing `sitemapUrl`, optional `maxPages`, and `outputMode`. |
| Uploaded XML | `/webhook/sitemap-to-markdown/upload` | Multipart upload with the XML in binary field `data`, plus optional JSON fields. |

Use `outputMode: "download"` to return the generated `.md` file to the caller. Use `outputMode: "drive"` to upload the file to Google Drive. The default limit is 10 pages, and the workflow caps a single request at 100 pages to reduce accidental bulk generation.

Example URL request:

```bash
curl -X POST 'https://YOUR_N8N_HOST/webhook/sitemap-to-markdown/url' \
  -H 'Content-Type: application/json' \
  -d '{"sitemapUrl":"https://example.com/sitemap.xml","maxPages":5,"outputMode":"download"}' \
  -o generated-page.md
```

Example uploaded-file request:

```bash
curl -X POST 'https://YOUR_N8N_HOST/webhook/sitemap-to-markdown/upload' \
  -F 'data=@sitemap.xml' \
  -F 'outputMode=drive' \
  -F 'maxPages=5'
```

## n8n setup

Import or create the workflow from `sitemap_to_markdown_workflow.js`. Attach an OpenAI credential to the generation node and a Google Drive OAuth credential to the Drive upload node. The HTTP Request nodes do not require credentials for public sitemap and webpage URLs; private websites should be configured separately with an approved authentication method.

Before first production use, test with one or two URLs, inspect the extracted source content, verify the generated Markdown, and confirm the Google Drive folder. Keep the workflow inactive until credentials, rate limits, access permissions, and review steps are confirmed.

## Markdown quality controls

The generated drafts should be treated as editorial drafts. The prompt requires page-specific titles, a single clear H1, useful sections, no keyword stuffing, no invented claims, and a `needs_review` status when source evidence is thin. Human reviewers should verify facts, authorship, canonical URLs, internal links, schema recommendations, images, and any claims that could affect health, finance, safety, or other high-impact decisions.

The workflow uses the existing webpage as its primary evidence source. It does not promise rankings, use fixed word-count padding, or automatically publish pages. Google-friendly means people-first, accurate, accessible, crawlable, and useful; it does not mean content is guaranteed to rank.

## References

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Influencing title links in Google Search](https://developers.google.com/search/docs/appearance/title-link)
- [Introduction to structured data markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
