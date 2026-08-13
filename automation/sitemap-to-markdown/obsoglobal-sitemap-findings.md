# obsoglobal.com sitemap test findings

Input URL: https://obsoglobal.com/sitemap_index.xml

The URL is publicly accessible. It is a sitemap index rather than a direct URL-set sitemap. It lists child sitemap files including post-sitemap.xml, page-sitemap.xml, part-sitemap1.xml through part-sitemap62.xml, part-category-sitemap.xml, brand-sitemap.xml, and local-sitemap.xml. The current sitemap-to-Markdown workflow's simple `<loc>` parser would treat those child sitemap URLs as webpage URLs, so it needs recursive child-sitemap handling before it can correctly generate Markdown pages from this input.

Observed child sitemap count: 68 URLs, based on the extracted index content.

Safe test recommendation: process a small limit such as 3 to 5 page URLs from one or more child sitemaps, keep outputMode=download, and review drafts before any Google Drive upload or publication.
