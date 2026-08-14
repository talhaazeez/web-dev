# Ask Sibe

## Purpose

The `/ask/` endpoint provides a natural-language information interface for the public Sibe CAD website. It answers common questions about cloud CAD management for SolidWorks, the free trial, version control, BOM workflows, browser collaboration, security, pricing, migration, and contact options.

This endpoint is informational only. It does not create accounts, submit purchases, change subscriptions, or expose private workspace data.

## WebMCP tools

The page exposes a declarative WebMCP form named `askSibe` and a guarded imperative `document.modelContext.registerTool` implementation when the browser supports WebMCP.

The input parameter is `question`, a natural-language question about the published Sibe CAD resources. Commercial and plan-specific answers should be confirmed on the official Sibe pricing or demo page.

## Published resources

- [Sibe homepage](https://sibe-cad.vercel.app/)
- [Cloud CAD management](https://sibe-cad.vercel.app/cloud-cad-management/)
- [Sibe Open Knowledge Format bundle](https://sibe-cad.vercel.app/okf/index.md)
- [Contact Sibe](https://sibe-cad.vercel.app/contact/)
- [Official pricing](https://www.sibe.io/pricing)
- [Official demo](https://www.sibe.io/demo)

## OKF companion

The page-specific [Open Knowledge Format concept](https://sibe-cad.vercel.app/okf/concepts/ask-sibe.md) carries the structured, frontmatter-based knowledge representation for this page.
